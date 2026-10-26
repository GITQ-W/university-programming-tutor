# 平台接入说明

文档核对日期：2026-10-25。本文说明可采用的接入路线；未逐一在真实账户完成导入或行为测试。产品版本、套餐和管理员配置可能改变入口，应以当前账户实际功能为准。

## 选择交付文件

| 文件 | 用途 |
| --- | --- |
| [`dist/chat-starter.txt`](../dist/chat-starter.txt) | 精简核心规范，直接复制到新聊天，最少依赖平台功能 |
| [`dist/chat-full.txt`](../dist/chat-full.txt) | 核心规范与四份参考的合并文本，可复制或作为实际可解析的资料上传 |
| [`dist/university-programming-tutor-skill.zip`](../dist/university-programming-tutor-skill.zip) | 以一个同名目录为顶层的标准 Skill 包，附 MIT 许可 |
| [`skills/university-programming-tutor`](../skills/university-programming-tutor) | 可按宿主规则放置的原生 Skill 源文件夹 |

精简提示词和完整提示词由同一套规范生成。它们不会给聊天平台新增终端、联网、编译器或永久记忆。普通消息的作用范围由会话上下文决定；项目设定、智能体、原生技能等持久配置需要在对应产品中另行保存。

## 豆包

先将 `chat-starter.txt` 全文发到一个新聊天，再提交代码和题目。若当前版本有智能体创建入口，可将核心规范保存为智能体设定。官方介绍确认存在定制智能体能力，但本文不假定所有账户都显示同一入口，也未确认其能直接导入标准 Skill ZIP。

完整参考文本只有在实际粘贴或被平台解析后才可用；模型口头说“已读取”不算读取证据。

来源：[豆包官方功能介绍](https://www.doubao.com/legal/feature_intro)。

## DeepSeek

聊天产品使用通用提示词，并在同一会话中继续提交任务。未验证该聊天产品的原生 Skill ZIP 导入方式，不把 API 功能当成网页产品功能。

对开发者，官方 Chat Completions API 支持 `system` 消息，可将核心规范作为其内容，学生任务放入 `user` 消息。模型、权限、上下文和工具由调用方另行配置；本项目不包含密钥或已连接的 API 客户端。

来源：[DeepSeek 官方 API 文档](https://api-docs.deepseek.com/api/create-chat-completion/)。

## WorkBuddy

官方文档提供“专家·技能·连接器 → 技能 → 添加技能 → 上传技能”路线。选择本项目的标准 Skill 包，按客户端提示导入并检查已安装列表。

本项目已准备 ZIP 结构，但尚未在 WorkBuddy 实机导入；若客户端对包格式有额外要求，以其提示为准，并记录错误用于适配。自定义技能包应走上传入口，不能将“对话搜索技能市场”当成任意 GitHub 包的自动安装。

来源：[WorkBuddy 官方技能文档](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

## Grok

### 网页、App 与 Grok Bot

通用提示词可用于普通聊天。Grok 官方也介绍了自定义技能；在具备相应入口的产品中，可请它将提供的规范保存成“大学编程导师”技能，检查保存内容后再测试。尚未验证本项目 ZIP 能直接在 Grok 网页导入。

Grok Bot 的保存技能和启用入口按其产品文档操作，不与 Grok Build 的本地目录安装混用。

来源：[Grok Skills 官方介绍](https://x.ai/news/grok-skills)、[Grok Bot 技能文档](https://docs.x.ai/grok-bot/skills-routines-and-automations)。

### Grok Build

官方说明支持从 `~/.grok/skills/` 和项目 `.grok/skills/` 发现 `SKILL.md`。将源文件夹复制进去，确保最终路径为 `.grok/skills/university-programming-tutor/SKILL.md`，可按产品支持方式使用 `/university-programming-tutor`。Windows 中 `~` 指当前用户目录。

来源：[Grok Build 官方技能文档](https://docs.x.ai/build/features/skills-plugins-marketplaces)。

## Claude

### 网页 / Cowork

在账户具备自定义技能能力时，通过 Skills 管理入口上传标准 Skill ZIP 并启用。该 ZIP 包含顶层 `university-programming-tutor/`，其下一层就是 `SKILL.md`，符合官方的包装示例。导入能力和运行工具仍受当前产品配置限制。

来源：[Claude 官方自定义技能指南](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

### Claude Code

将源文件夹复制到 `~/.claude/skills/` 或项目 `.claude/skills/`，通过 `/university-programming-tutor` 调用。Claude Code 本地路径和网页/Cowork 的账户技能配置不是同一条安装路径。

来源：[Claude Code 官方技能文档](https://code.claude.com/docs/en/skills)。

## Codex

将源文件夹复制到 `~/.agents/skills/`，在对话中用 `$university-programming-tutor` 调用；未被发现时重新启动后检查。`agents/openai.yaml` 仅提供这个宿主的界面元数据，教学核心并不依赖它。

来源：[OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

## 验证状态

本次完成分发文件生成、ZIP 层级、内容一致性、相对链接和 Skill 格式检查。上述第三方产品的账户导入、触发、代码执行与教学效果均仍需实测；文档存在某项功能，不等于本项目已在该产品测试通过。

首次使用时先运行 [共用测试](testing.md)，记录产品名称、模型、版本、接入方式与可用工具。出现差异时优先修正平台说明或能力判断，不为迎合某个平台删去通用的证据要求。
