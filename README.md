# 大学编程导师 · 跨平台版

面向大学生的 C、C++、Java、Python 编程教育 Skill：检查代码、解释错误、梳理知识，并把一次调试转化为能够迁移的理解。

A Chinese-first, platform-independent programming tutor with a portable chat prompt and an Agent Skills package for code review, debugging, and structured learning.

适用于豆包、DeepSeek、WorkBuddy、Grok、Claude，以及 Codex 等工具的接入场景。通用提示词与标准 Skill 从同一份核心规范生成；不同平台分别配置，不承诺共享安装、记忆或执行环境。

版本：`0.2.0`。提供接入材料与文档核对；跨平台实机效果尚未逐一验证。

## 能做什么

| 场景 | 交付内容 |
| --- | --- |
| 代码检查与调试 | 问题位置、触发条件、根因、影响、最小修复与验证结果 |
| 知识点梳理 | 先修关系、核心概念、易错点、最小示例和典型题型 |
| 跨语言学习 | 比较参数传递、相等与身份、整数除法、生命周期等语义差异 |
| 教学与练习 | 按需提供提示或完整解答，支持出题、批改和错题归纳 |

诊断结论区分 **运行复现、静态确定、待验证**。无法运行时明确说明，不将编译成功或少量测试等同于完整正确性证明。

## 最快开始：普通聊天

1. 下载本仓库并解压。
2. 打开 [`dist/chat-starter.txt`](dist/chat-starter.txt)，复制全文作为新聊天的第一条消息发送。
3. 接着发送题目、代码和课程约束，例如“请检查下面的 C17 代码，只给下一步提示”。
4. 需要完整语言检查项和知识资料时，使用 [`dist/chat-full.txt`](dist/chat-full.txt)。它已合并参考内容，不要求聊天产品读取本地目录。若不能上传 TXT，直接复制文本；长度受限时先用精简版，再补充相关资料。

普通聊天使用自然语言提出任务，不要求输入 Codex 的 `$` 命令。是否跨会话保留设定，取决于平台的具体产品功能。

## 按平台接入

| 平台 / 产品 | 本项目提供的接入方式 |
| --- | --- |
| 豆包 | 通用聊天提示词；有智能体设定入口时可保存核心规范 |
| DeepSeek | 通用聊天提示词；开发者可将规范放入 API 的 system 消息 |
| WorkBuddy | 通过技能页的“添加技能 → 上传技能”导入技能包；通用提示词备用 |
| Grok 网页 / App / Bot | 通用提示词或当前产品的技能创建入口；尚未验证通用 ZIP 的网页导入 |
| Grok Build | 将标准 Skill 文件夹放入 `~/.grok/skills/` 或项目 `.grok/skills/` |
| Claude 网页 / Cowork | 在支持自定义技能的账户中导入 Skill ZIP 并启用；通用提示词备用 |
| Claude Code | 将标准 Skill 文件夹放入 `~/.claude/skills/` 或项目 `.claude/skills/` |
| Codex | 将标准 Skill 文件夹放入 `~/.agents/skills/` |

原生技能包：[`dist/university-programming-tutor-skill.zip`](dist/university-programming-tutor-skill.zip)。各产品的具体步骤、核对来源和未验证项见 [平台接入说明](docs/platforms.md)。

### Codex 的本地安装

1. 下载并解压本仓库，或使用 Git 克隆。
2. 将整个 [`skills/university-programming-tutor`](skills/university-programming-tutor) 文件夹复制到个人 Skill 目录：

   | 系统 | 个人 Skill 目录 |
   | --- | --- |
   | Windows | `%USERPROFILE%\.agents\skills\` |
   | macOS / Linux | `~/.agents/skills/` |

3. 确保最终结构为 `.agents/skills/university-programming-tutor/SKILL.md`，避免重复嵌套目录。若已有同名 Skill，先备份并比较修改。
4. 在 Codex 对话中输入 `$university-programming-tutor`。若尚未显示，可重启 Codex 后再检查。

默认允许按任务自动选择，也支持显式调用。目录约定与发现机制参见 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。其他产品按上面的对应接入方式配置。

## 使用示例

以下为各平台通用的任务文本；先完成提示词配置或原生 Skill 安装。Codex 用户也可以在任务前加 `$university-programming-tutor`。

### 检查代码

````text
请检查下面的 C 代码。课程使用 C17，只允许使用数组和函数。
请给出错误位置、触发输入、根因和最小修复；能运行就验证，不能运行请说明。

题目：……
有效输入范围：……
期望结果与实际报错：……
```c
// 在此粘贴代码
```
````

### 整理知识与练习

```text
我学过 C，刚开始学 C++。请梳理指针、引用、const 和对象生命周期，
用最小示例比较，最后给我 3 道练习，先不展示答案。
```

### 跨语言比较

```text
比较 Java 的 == 和 equals、Python 的 is 和 ==，讲清对象身份与逻辑相等。
```

### 按教材复习

```text
按下面的 Python 课程目录整理复习提纲，列出先修知识、易错点和典型题型。
课程目录：……
已学基础：……
```

提供目标语言版本、完整题意、输入范围、实际报错和课程限制，有助于减少误判。没有题目时仍可检查语言层面的问题，但无法确认算法是否符合题意。

## 项目结构

```text
.
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── docs/                         各平台接入与效果评测说明
├── evals/cases.json              跨平台共用的测试题和判定标准
├── scripts/build_bundle.py       从核心规范生成各类交付文件
├── dist/                         精简提示词、完整提示词和 Skill ZIP
└── skills/
    └── university-programming-tutor/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
            ├── code-review.md
            ├── language-checks.md
            ├── curriculum.md
            └── teaching.md
```

[`SKILL.md`](skills/university-programming-tutor/SKILL.md) 保留职责、路由与质量要求。参考文件按任务加载，分别处理代码诊断、语言语义、知识体系和教学流程。

## 能力与验证范围

这是可复用的指令和参考资料，不是独立训练的模型，也不自带编译器、解释器或执行沙箱。实际检查能力取决于所使用的模型、提供的上下文和当前执行环境。

发布材料的格式与构建检查不等同于平台效果评测。各平台的安装、触发和教学效果需分别验证；目前没有“所有平台均已实测通过”的结论。参见 [跨平台测试方法](docs/testing.md) 和共用测试集。不承诺发现所有错误或保证课程成绩。

## 重新生成分发材料

在仓库根目录运行（Python 3.10+，仅标准库，不调用模型或联网）：

```text
python scripts/build_bundle.py
```

生成精简提示词、合并四份参考的完整提示词、带许可的标准 Skill ZIP 以及校验清单。教学规则只维护在 `skills/university-programming-tutor/`；不要手工修改 `dist` 中的生成文件。

## 定制与贡献

- 将长期通用的教学偏好写入 `SKILL.md`。
- 按教材修改 `references/curriculum.md`，保留先修关系和可检验的学习目标。
- 单次作业的版本、禁用库或指定算法直接在对话中说明。
- 欢迎提交可复现的误报、漏报、语义纠正和教学改进；参见 [贡献指南](CONTRIBUTING.md)。

## 许可证

本项目采用 [MIT License](LICENSE)。文档中的外部链接内容遵循各自的许可条款。
