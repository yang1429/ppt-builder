# ppt-builder

一个用于制作 PowerPoint 的 WorkBuddy Skill：先写大纲，再出稿，然后做机械校验和渲染检查，最后交付。

## 能做什么

- 从主题、大纲、Word/Markdown 文档或已有材料生成 PPTX
- 给生成结果施加统一的版式、字体、配色规范
- 检查已有 PPTX 的空页、超长文本、缺标题、文本过密问题
- 只输出大纲，不生成文件

## 安装

把整个`ppt-builder` 目录放到以下任一位置：

- 个人可用：`~/.workbuddy/skills/ppt-builder/`
- 团队共享：项目根目录下的 `.workbuddy/skills/ppt-builder/`

重启 WorkBuddy 会话后生效。

## 用法

直接说需求即可，例如：

> 帮我做一份 12 页的季度汇报 PPT，受众是管理层，要突出成本和交付周期。

或只要求大纲：

> 用 ppt-builder 给这个方案列一个 PPT 大纲，先不要做文件。

检查已有文件：

> 用 ppt-builder 检查这份 PPT 有没有空页和文字溢出。

## 目录结构

```
ppt-builder/
├── SKILL.md                    触发条件、工作流决策树、六个步骤
├── references/
│   └── design-spec.md          版式、字体、颜色、图表规范
├── assets/
│   └── outline-template.md     先填大纲再做事
└── scripts/
    └── validate_pptx.py        零依赖 PPTX 结构检查器
```

## 校验器

```bash
python scripts/validate_pptx.py path/to/deck.pptx
```

输出 JSON，包含页数、图片数、errors 和 warnings。退出码 0 表示无错误，1 表示有错误，2 表示用法错误。不依赖任何第三方包，直接解 PPTX 的 zip 并解析 slide XML。

## 自定义

- 改 `description` 里的触发词，决定什么请求会用到它
- 改 `references/design-spec.md`，换成你自己的品牌规范
- 在 `assets/` 放入你的模板 PPT，让结果直接套版

## 版本

版本号维护在 `SKILL.md` frontmatter 的 `version` 字段。当前版本见该文件。

## 许可

MIT License.
