import { useState, useEffect } from 'react'
import './App.css'

interface CounterResponse {
  counter: number
}

function App({ isAuthenticated, counterUrl, incrementUrl, csrfmiddlewaretoken }: {
  isAuthenticated: boolean
  counterUrl: string
  incrementUrl: string
  csrfmiddlewaretoken: string
}) {
  const [count, setCount] = useState(0)
  const [error, setError] = useState()

  useEffect(() => {
    let mounted = true
    fetch(counterUrl).then(
      resp => resp.json()
    ).then(
      ({ counter} : CounterResponse) => {
        if (mounted) {
          setCount(counter)
        }
      }
    )
    return () => {
      mounted = false
    }
  }, [counterUrl])

  async function handleIncrement() {
    console.log('handleIncrement...')

    const form = new FormData()
    form.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

    const response = await fetch(incrementUrl, {
      credentials: 'include',
      body: form,
      method: 'POST',
    })

    const data = await response.json()

    // if an error occured
    if (response.status > 299) {
      setError(data.detail)
      return
    }

    setError(undefined)
    setCount((data as CounterResponse).counter)
  }

  console.log(isAuthenticated)

  return (
    <div className="App">
      <h1>{count}</h1>
      {isAuthenticated && (
        <button
          className="btn btn-primary"
          onClick={handleIncrement}
        >
          Increment
        </button>
      )}
      {error && (
        <div className="alert alert-warning">
          {error}
        </div>
      )}
    </div>
  )
}

export default App
