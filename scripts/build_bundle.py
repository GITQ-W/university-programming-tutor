#!/usr/bin/env python3
"""Build portable prompts and a native Skill ZIP, using only the standard library."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "university-programming-tutor"
SKILL_ROOT = ROOT / "skills" / SKILL_NAME
DIST = ROOT / "dist"
REFERENCES = (
    ("代码诊断与验证", "code-review.md"),
    ("语言易错点与跨语言比较", "language-checks.md"),
    ("大学编程知识体系", "curriculum.md"),
    ("教学与练习", "teaching.md"),
)
LINK = re.compile(r"\]\(([^)]+)\)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_local_links(path: Path, allowed_root: Path) -> None:
    for match in LINK.finditer(read(path)):
        target = match.group(1)
        if target.startswith(("https://", "http://", "#")):
            continue
        resolved = (path.parent / target.split("#", 1)[0]).resolve()
        require(resolved.is_relative_to(allowed_root.resolve()), f"Escaping link in {path.name}: {target}")
        require(resolved.exists(), f"Missing link in {path.name}: {target}")


def core_body() -> str:
    text = read(SKILL_ROOT / "SKILL.md")
    match = re.fullmatch(r"---\n(.*?)\n---\n(.*)", text, flags=re.S)
    require(match is not None, "SKILL.md must contain YAML frontmatter")
    front, body = match.groups()
    require(re.search(rf"(?m)^name: {re.escape(SKILL_NAME)}$", front) is not None, "Skill name mismatch")
    desc = re.search(r'(?m)^description: (".*")$', front)
    require(desc is not None, "Expected a quoted description")
    require(0 < len(json.loads(desc.group(1))) <= 200, "Description must fit the cross-platform 200-character limit")
    # Native hosts can load files lazily; a chat-only host must not depend on a router.
    start = body.find("## 按任务加载参考\n")
    require(start >= 0, "Reference router heading missing")
    end = body.find("\n## ", start + 1)
    require(end >= 0, "Reference router must be followed by another section")
    body = body[:start] + body[end + 1:]
    native_sentence = "标准 Skill 模式按下方相对路径读取参考；普通聊天仅使用用户粘贴或平台实际解析到的资料。"
    require(native_sentence in body, "Capability adaptation sentence missing")
    body = body.replace(native_sentence, "仅使用当前消息和平台实际解析到的资料；本对话无需访问任何本地相对路径。", 1)
    return body.strip() + "\n"


def describe_file(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def write_zip(files: list[Path], output: Path) -> None:
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for source in files:
            relative = source.relative_to(SKILL_ROOT).as_posix()
            info = ZipInfo(f"{SKILL_NAME}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
        license_info = ZipInfo(f"{SKILL_NAME}/LICENSE", date_time=(1980, 1, 1, 0, 0, 0))
        license_info.compress_type = ZIP_DEFLATED
        license_info.create_system = 3
        license_info.external_attr = 0o100644 << 16
        archive.writestr(license_info, (ROOT / "LICENSE").read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    with ZipFile(output) as archive:
        require(archive.testzip() is None, "ZIP integrity check failed")
        require(len(archive.namelist()) == len(files) + 1, "Unexpected ZIP member count")
        for source in files:
            name = f"{SKILL_NAME}/{source.relative_to(SKILL_ROOT).as_posix()}"
            require(archive.read(name) == source.read_bytes(), f"ZIP content mismatch: {name}")


def main() -> None:
    version = read(ROOT / "VERSION").strip()
    require(re.fullmatch(r"\d+\.\d+\.\d+", version) is not None, "Invalid VERSION")
    files = sorted(path for path in SKILL_ROOT.rglob("*") if path.is_file())
    require(all(not path.is_symlink() for path in files), "Skill source must not contain symlinks")
    for path in files:
        if path.suffix == ".md":
            validate_local_links(path, SKILL_ROOT)
    body = core_body()
    preface = (
        f"# 大学编程导师 · 通用对话规范 v{version}\n\n"
        "请在当前会话中按以下规范帮助我学习编程。先简短确认，然后等待我的题目或代码；"
        "不自行编造待审代码，也不声称永久安装、拥有工具或跨会话记忆。\n\n"
    )
    starter = preface + body
    full = preface + body + "\n# 按任务使用的参考资料\n"
    for title, filename in REFERENCES:
        content = read(SKILL_ROOT / "references" / filename).strip()
        content = re.sub(r"(?m)^(#{1,5}) ", r"#\1 ", content)
        full += f"\n## 附录：{title}\n\n{content}\n"
    for output in (starter, full):
        for match in LINK.finditer(output):
            require(match.group(1).startswith(("https://", "http://", "#")), "Portable prompt retains a local file dependency")
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / "chat-starter.txt").write_text(starter, encoding="utf-8", newline="\n")
    (DIST / "chat-full.txt").write_text(full, encoding="utf-8", newline="\n")
    write_zip(files, DIST / f"{SKILL_NAME}-skill.zip")
    artifacts = ("chat-starter.txt", "chat-full.txt", f"{SKILL_NAME}-skill.zip")
    source_files = files + [ROOT / "LICENSE", ROOT / "VERSION"]
    manifest = {
        "schema_version": 1,
        "version": version,
        "sources": {path.relative_to(ROOT).as_posix(): describe_file(path) for path in source_files},
        "artifacts": {name: describe_file(DIST / name) for name in artifacts},
    }
    (DIST / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Built v{version}: {len(artifacts)} artifacts; {len(files) + 1} ZIP members; 4 embedded references.")
    print("Packaging checks passed. No platform imports or model behavior evaluations were performed.")


if __name__ == "__main__":
    main()
