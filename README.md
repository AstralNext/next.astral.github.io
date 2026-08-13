# Astral

通用组网与游戏联机。暂不含完整文档——教程继续使用 [astral.fan](https://astral.fan/)。

- 站点：[https://next.astral.fan](https://next.astral.fan)
- 本地仓库：`next.astral.github.io`

## 页面

| 路径 | 说明 |
|------|------|
| `/` | 首页分流 |
| `/astral/` | 通用版 |
| `/game/` | 游戏版 |
| `/j/` | 房间邀请落地（跳转 `astralgame://`） |
| `/download/` | 下载 |

下载与仓库 URL 集中在 [`src/site.ts`](src/site.ts)。

## 开发

```bash
npm install
npm run dev
```

打开终端提示的本地地址（默认 `http://localhost:4321`）。

```bash
npm run build    # 输出到 dist/
npm run preview  # 预览生产构建
```

## 部署

1. 推送到 GitHub 后，仓库 **Settings → Pages → Build and deployment → Source** 选 **GitHub Actions**（不要选 Deploy from a branch，否则会走 Jekyll）。
2. 推送 `master`/`main` 会触发 `.github/workflows/deploy.yml`：`npm run build` → 发布 `dist/`。
3. 自定义域名：Pages 设置中填 `next.astral.fan`，DNS 加 CNAME 指向 GitHub Pages。
4. `astro.config.mjs` 中已设置 `site: 'https://next.astral.fan'`。

## 相关链接

- 旧文档：https://astral.fan/
- AML：https://aml.astral.fan/
- 通用版仓库：https://github.com/AstralNext/Astral
