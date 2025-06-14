import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetch('http://localhost:5000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
  }, [])

  return <h1>{message || "Loading..."}</h1>
}

export default App
