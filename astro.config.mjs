// https://astro.build/config
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://next.astral.fan',
  output: 'static',
  compressHTML: true,
  integrations: [sitemap()],
});
