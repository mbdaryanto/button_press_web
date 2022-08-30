import { resolve } from 'path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base: '/static/',
  build: {
    emptyOutDir: true,
    manifest: true,
    outDir: '../counter/static/',
    // publicDir: 'static/',
    // lib: {
    //   entry: resolve(__dirname, 'src/main.tsx'),
    //   name: 'counter',
    //   // the proper extensions will be added
    //   fileName: 'counter'
    // },
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        lib: resolve(__dirname, 'src/main.tsx')
        // counter: resolve(__dirname, 'counter.html'),
      }
    }
  },
  plugins: [react()]
})
