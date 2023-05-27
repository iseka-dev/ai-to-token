import { defineConfig } from 'vite'


export default defineConfig({
  input: './templates/index.html',
  build: {
    // generate manifest.json in outDir
    manifest: true,
    outDir: './static/dist',
    rollupOptions: {
      // overwrite default .html entry
      // input: './templates/index.html'
      input: ['./static/js/index.js', './static/js/web3.js'],
    }
  },
  server: {
      open: './templates/index.html'
  }
})
