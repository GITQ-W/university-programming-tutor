# 大学编程导师 · University Programming Tutor

面向大学生的 C、C++、Java、Python 编程教育 Skill：检查代码、解释错误、梳理知识，并把一次调试转化为能够迁移的理解。

A Chinese-first agent skill for university programming education, code review, debugging, and structured learning across C, C++, Java, and Python.

## 能做什么

| 场景 | 交付内容 |
| --- | --- |
| 代码检查与调试 | 问题位置、触发条件、根因、影响、最小修复与验证结果 |
| 知识点梳理 | 先修关系、核心概念、易错点、最小示例和典型题型 |
| 跨语言学习 | 比较参数传递、相等与身份、整数除法、生命周期等语义差异 |
| 教学与练习 | 按需提供提示或完整解答，支持出题、批改和错题归纳 |

诊断结论区分 **运行复现、静态确定、待验证**。无法运行时明确说明，不将编译成功或少量测试等同于完整正确性证明。

## 安装到 Codex

1. 下载并解压本仓库，或使用 Git 克隆。
2. 将整个 [`skills/university-programming-tutor`](skills/university-programming-tutor) 文件夹复制到个人 Skill 目录：

   | 系统 | 个人 Skill 目录 |
   | --- | --- |
   | Windows | `%USERPROFILE%\.agents\skills\` |
   | macOS / Linux | `~/.agents/skills/` |

3. 确保最终结构为 `.agents/skills/university-programming-tutor/SKILL.md`，避免重复嵌套目录。若已有同名 Skill，先备份并比较修改。
4. 在 Codex 对话中输入 `$university-programming-tutor`。若尚未显示，可重启 Codex 后再检查。

默认允许按任务自动选择，也支持显式调用。目录约定与发现机制参见 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。其他支持 Agent Skills 的工具需按各自的安装方式配置，尚未逐一验证。

## 使用示例

### 检查代码

````text
$university-programming-tutor
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
$university-programming-tutor
我学过 C，刚开始学 C++。请梳理指针、引用、const 和对象生命周期，
用最小示例比较，最后给我 3 道练习，先不展示答案。
```

### 跨语言比较

```text
$university-programming-tutor
比较 Java 的 == 和 equals、Python 的 is 和 ==，讲清对象身份与逻辑相等。
```

### 按教材复习

```text
$university-programming-tutor
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

初版已完成 Skill 格式检查、本地参考链接检查及若干 Python 语义抽查；尚未完成独立、系统的教学与代码诊断效果评测，也未对 C、C++、Java 示例统一编译执行。不承诺发现所有错误或保证课程成绩。

## 定制与贡献

- 将长期通用的教学偏好写入 `SKILL.md`。
- 按教材修改 `references/curriculum.md`，保留先修关系和可检验的学习目标。
- 单次作业的版本、禁用库或指定算法直接在对话中说明。
- 欢迎提交可复现的误报、漏报、语义纠正和教学改进；参见 [贡献指南](CONTRIBUTING.md)。

## 许可证

本项目采用 [MIT License](LICENSE)。文档中的外部链接内容遵循各自的许可条款。
