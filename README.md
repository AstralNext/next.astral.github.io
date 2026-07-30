# Astral Next 产品门户

下一代 Astral 官方门户：**一套站、两种用户**（通用版 / 游戏版）。暂不含完整文档——教程继续使用 [astral.fan](https://astral.fan/)。

- 站点域名（规划）：[https://next.astral.fan](https://next.astral.fan)
- 本地仓库：`next.astral.github.io`

## 页面

| 路径 | 说明 |
|------|------|
| `/` | 品牌首页 + 通用 / 游戏分流 |
| `/astral/` | 通用版介绍与下载 |
| `/game/` | 游戏版介绍与下载 |
| `/download/` | 双产品下载并列 |

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

1. 将本仓库推送到 GitHub（例如 `AstralNext/next.astral.github.io` 或组织自定义名）。
2. 开启 **GitHub Pages**：Source 选 GitHub Actions，或把 `dist/` 发到 `gh-pages` 分支。
3. 自定义域名：在仓库 Pages 设置中填 `next.astral.fan`，并在 DNS 添加 CNAME 指向 GitHub Pages。
4. `astro.config.mjs` 中已设置 `site: 'https://next.astral.fan'`。

示例 GitHub Actions（可选，自行添加 `.github/workflows/deploy.yml`）：

```yaml
name: Deploy
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

## 相关链接

- 旧文档：https://astral.fan/
- AML：https://aml.astral.fan/
- 通用版仓库：https://github.com/AstralNext/Astral
