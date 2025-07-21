// vite.config.js
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  base: '/arthursvz.github.io/', // Remplace par le nom de ton repo
  plugins: [svelte()]
});
