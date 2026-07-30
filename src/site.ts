/** Site-wide links and product metadata. Change here when repos move. */
export const site = {
  name: 'Astral',
  tagline: '一套内核，两种用法',
  url: 'https://next.astral.fan',
  docsLegacy: 'https://astral.fan/',
  aml: 'https://aml.astral.fan/',
  githubOrg: 'https://github.com/AstralNext',
} as const;

export const products = {
  general: {
    id: 'astral',
    name: 'Astral',
    label: '通用版',
    path: '/astral/',
    blurb: '面向配置与多实例的 EasyTier 管理客户端',
    ctaHome: '我要通用组网',
    downloadLabel: '下载通用版',
    releases: 'https://github.com/AstralNext/Astral/releases',
    repo: 'https://github.com/AstralNext/Astral',
    accent: 'teal',
    logo: '/logos/astral-general.svg',
    logoDark: '/logos/astral-general-dark.svg',
    mark: '/logos/astral-general-mark.svg',
  },
  game: {
    id: 'game',
    name: 'Astral Game',
    label: '游戏版',
    path: '/game/',
    blurb: '面向房间联机的轻量客户端',
    ctaHome: '我要游戏联机',
    downloadLabel: '下载游戏版',
    releases: 'https://github.com/ldoubil/astral/releases',
    repo: 'https://github.com/ldoubil/astral',
    accent: 'amber',
    logo: '/logos/astral-game.svg',
    logoDark: '/logos/astral-game-dark.svg',
    mark: '/logos/astral-game-mark.svg',
  },
} as const;
