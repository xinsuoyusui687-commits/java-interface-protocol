# 发布到 GitHub

## 选择仓库

建议创建专门的 `java-interface-protocol` 仓库，也可以将 `skills/java-interface-protocol/` 放入现有 skills 集合仓库。后者需合并 README、许可和检查配置，避免覆盖已有文件。

本包采用“仓库说明 + skills 子目录”结构。`SKILL.md` 是 skill 的入口，GitHub 本身不要求专用 skill 清单；本包也不需要 `package.json`、npm 发布或助手插件 marketplace 清单。

## 上传

1. 在 GitHub 创建仓库，建议默认分支使用 `main`。
2. 上传本包根目录内的文件和文件夹，让 `README.md`、`LICENSE`、`skills/`、`.github/` 位于仓库根目录，不再套一层本地发布包目录。
3. 确保 `.github/workflows/validate.yml`、`.gitignore` 和 `.gitattributes` 也被提交。普通网页上传可能遗漏隐藏文件；使用 Git 客户端更容易保留完整结构。
4. 将 README 中的 `OWNER/REPO` 改为真实仓库地址。确认 MIT 许可及 copyright 行符合实际权利归属；当前沿用原 skill 的 MIT 声明，未替发布者确认第三方权利。
5. 建议仓库描述：`Evidence-based Java API documentation skill with nested object tables.`；可选 topics：`agent-skills`、`java`、`api-documentation`、`codex`。

如使用命令行，先在本包根目录执行本地检查，然后按自己的 Git 身份和仓库操作：

```bash
git init -b main
git add .
git commit -m "Prepare java-interface-protocol skill"
git remote add origin https://github.com/OWNER/REPO.git
git push -u origin main
```

这些是发布者操作示例，本次整理未执行远程创建、推送或发布。

## 验证与版本

- 查看 GitHub Actions 的 `Validate skill` 是否成功；本地已通过不等于远程工作流已经运行。
- 在独立测试目录运行 `npx skills add OWNER/REPO --list`，确认列出 `java-interface-protocol`，再按 README 安装并检查参考文件齐全。
- 在目标助手用示例源码尝试生成文档，确认入口能发现，字段与引用符合预期。不同助手的自动触发与显示效果以实际验证为准。
- 检查完成后，再为提交打 `v0.2.0` 标签并创建 GitHub Release，可复用 CHANGELOG 的版本说明。
- 后续改动同步 skill 的 `metadata.version` 和 CHANGELOG；功能或语义变化应重新核对相关示例和参考文件。

无需因为上传 GitHub 就声称已经进入官方目录或 skills.sh 搜索结果；是否被收录与索引以相应服务的实际状态为准。

## 规范来源与核对范围

本次整理读取了当前本机技能创建及 GitHub 安装说明，并于 2026-11-27 读取 [Vercel Skills CLI README](https://github.com/vercel-labs/skills/blob/main/README.md)，核对 GitHub 来源安装、`--skill`、项目级默认安装和 Node.js 版本要求。

[Agent Skills 规范](https://agentskills.io/specification)与[OpenAI Skills 仓库](https://github.com/openai/skills)是后续维护参考；本次网络访问未能成功重新读取这两个远程入口，不将它们写作已完成最新在线核验。当前格式与本机官方 skill 创建/安装工具保持一致。
