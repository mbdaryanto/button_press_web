import React, { ComponentProps } from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'


const config = (window as any).config as ComponentProps<typeof App>

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App {...config} />
  </React.StrictMode>
)
