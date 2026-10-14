# 游戏规则与图片维护指南

本仓库既是官网，也是客户端的**线上规则与图片源**。改这里的规则/图片，用户不用升级客户端就能生效（客户端启动时会拉一次规则）。

## 1. 文件都在哪

| 内容 | 仓库路径 | 线上地址 |
| --- | --- | --- |
| 游戏规则 | `public/gamerules.json` | <https://next.astral.fan/gamerules.json> |
| 游戏图标 / 封面 | `public/games/<游戏 id>/icon.png`<br>`public/games/<游戏 id>/grid.png` | <https://next.astral.fan/games/<游戏 id>/icon.png> |
| 下载页数据 | `public/downloads.json` | <https://next.astral.fan/downloads.json> |

Astro 会把 `public/` 原样发布到站点根目录，所以：

- JSON 里写图片路径时**相对 `public/`，不带前导斜杠**，例如 `games/valheim/icon.png`；
- 线上实际地址就是 `https://next.astral.fan/games/valheim/icon.png`。

客户端侧对应的两个常量：规则地址 `kAstralGameRulesUrl`、图片基准 `kAstralGameMediaBaseUrl`（都在客户端的 `lib/data/models/game_catalog.dart`）。

## 2. 新增一个游戏（5 步）

1. 建目录 `public/games/<游戏 id>/`，放两张图：
   - `icon.png`：方形图标（列表、徽标用）
   - `grid.png`：竖版封面（选择器卡片用）
   - 尺寸/风格直接参考现有目录，例如 `public/games/stardew_valley/`。
2. 在 `public/gamerules.json` 的 `games[]` 里加一条（模板见下）。**`id` 必须和目录名完全一致。**
3. 把顶层的 `version` 加 1。
4. 本地预览：`npm install` → `npm run dev`，打开 `/game` 看图标、中文名、排序是否符合预期。
5. 提 PR（改规则只需这一个文件 + 图片）。

最小模板（无特殊规则的游戏，只需要"固定端口发现"）：

```json
{
  "id": "example_game",
  "name": "Example Game",
  "name_zh": "示例游戏",
  "description": "选择器里显示的一行短说明",
  "color": "#3B6EA5",
  "icon": "sports_esports_outlined",
  "steam_app_id": 123456,
  "icon_asset": "games/example_game/icon.png",
  "grid_asset": "games/example_game/grid.png",
  "show_in_picker": true,
  "sort": 200,
  "platforms": {
    "windows": {
      "lan_game_discover": { "type": "static_port", "port": 24642 }
    }
  }
}
```

## 3. 字段说明

### 游戏级字段

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `id` | 是 | 主键，必须与 `public/games/<id>/` 目录名一致 |
| `name` | 是 | 英文名 |
| `name_zh` | 建议 | 中文名；有值则 UI 优先显示 |
| `description` | 否 | 选择器里标题下方的短说明 |
| `color` | 否 | 主题色，`#RRGGBB` 或 `#AARRGGBB`，默认 `#6B7280` |
| `icon` | 否 | Material Icons 名称（如图标文件缺失时的兜底），默认 `sports_esports_outlined` |
| `icon_asset` | 否 | 方形图标路径；不写则按 `games/<id>/icon.png` 推断 |
| `grid_asset` | 否 | 竖版封面路径；不写则按 `games/<id>/grid.png` 推断 |
| `steam_app_id` | 否 | Steam AppID（脚本用它解析 SteamGridDB id） |
| `sgdb_game_id` | 否 | SteamGridDB 游戏 id（无 Steam 的游戏，如 Minecraft，直接写这个） |
| `show_in_picker` | 否 | 默认 `true`；`false` 表示不出现在建房选择器里 |
| `sort` | 否 | 排序，越小越靠前，默认 `100` |
| `platforms` | 否 | 按系统分组的规则，见下 |

### `platforms.<系统>` 下的规则块（按需添加）

系统键目前是 `windows`（其它系统留空即可）。

#### `network` — 网络标志

| 字段 | 说明 |
| --- | --- |
| `protocol` | `tcp` / `udp`，不写默认 `udp` |
| `enable_udp_broadcast_relay` | `true` 时给该游戏开启 UDP 广播中继（如 Raft、Valheim、FA） |

#### `lan_game_discover` — 局域网发现（对象或数组，写了即启用）

| 字段 | 说明 |
| --- | --- |
| `type` | `static_port` / `udp_multicast` / `udp_probe` / `udp_broadcast` / `process_udp` |
| `port` | 游戏监听/发现端口 |
| `multicast` | 组播地址 `host:port`（`udp_multicast` 用，如 `224.0.2.60:4445`） |
| `parser` | 解析器：`minecraft_motd` / `mindustry_server` / `scfa_lan` / `raft_lan` / `valheim_lan` … |
| `probe` | `udp_probe` 的探测包十六进制，如 `fe01` |
| `title` | 房间标题模板，支持 `{player}` `{game}` `{label}` `{motd}` `{map}` |
| `label` | 固定标签 |
| `process` | `process_udp`：进程名列表，如 `["game.exe"]` |
| `window` | `process_udp`：窗口标题关键字 |
| `beacon_port` | `process_udp`：本机代答发现口（FA 默认 15000） |

#### `forwards` — TCP 端口转发（数组）

`listen` → `target` 一对一转发；**目前自研转发只支持 `tcp`**，非 tcp 会被跳过。

| 字段 | 说明 |
| --- | --- |
| `listen` | 本机监听地址，如 `127.0.0.1:2456` |
| `target` | 目标地址，通常是房主虚拟 IP，如 `10.126.126.1:2456` |
| `proto` | 默认 `tcp`（仅 `tcp` 生效） |
| `host_only` | 默认 `true`，表示只有房主启动这条转发 |

#### `magic_wall` — 进程级防火墙规则（对象：`exe` → 规则数组）

```json
"magic_wall": {
  "GTA5.exe": [
    { "action": "allow", "protocol": "udp", "direction": "both",
      "local_ip": "10.126.126.0/24", "remote_ip": "10.126.126.0/24" },
    { "action": "block", "protocol": "udp", "direction": "both", "remote_port": "3478" }
  ]
}
```

规则字段：`action`（`allow` / `block`）、`protocol`（`udp` / `tcp`）、`direction`（`both` / `in` / `out`）、`local_ip` / `remote_ip`（CIDR）、`local_port` / `remote_port`（端口或 `起始-结束` 区间）。

#### `inject` — 进房后自动注入插件

目前仅支持 `mono`（Unity 游戏）。

| 字段 | 说明 |
| --- | --- |
| `type` | 固定 `mono` |
| `process` | 进程名列表 |
| `window` | 窗口标题关键字（可选） |
| `dll` | 注入的 DLL 文件名，如 `AstralRaftNet.dll`（客户端安装后在 `native/<游戏 id>/`） |
| `namespace` / `class` / `method` | 注入入口，默认 `Init` |
| `delay_seconds` | 发现进程后等几秒再注入，默认 5，避免游戏没起来就注入导致崩溃 |

## 4. 图片约定

- 每个游戏一个目录：`public/games/<id>/`
- 两个固定文件名：`icon.png`（方形图标）、`grid.png`（竖版封面）
- JSON 里的写法：`"icon_asset": "games/<id>/icon.png"`（相对 `public/`，无前导斜杠）
- **不写 `icon_asset` / `grid_asset` 也能用**：客户端会按 `games/<id>/icon.png`、`games/<id>/grid.png` 自动推断，先试本地内置资源，再走线上 CDN。

## 5. 提交前自检

- [ ] `id` 与 `public/games/<id>/` 目录名一致（含大小写）
- [ ] JSON 能解析：`python -m json.tool public/gamerules.json > $null`（或 `npx prettier --check`）
- [ ] 顶层 `version` 已 +1
- [ ] 图片文件名是 `icon.png` / `grid.png`
- [ ] 本地 `/game` 页面预览过：图标、中文名、排序都对
