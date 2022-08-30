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
    // console.log('handleIncrement...')

    const form = new FormData()
    form.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

    try {
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
      setCount((data as CounterResponse).counter)
      setError(undefined)

    } catch (error) {
      console.error(error)
    }

  }

  // console.log(isAuthenticated)

  return (
    <div className="App container-fluid d-flex flex-column align-items-center mt-2">

      <h1 className="m-5">Button Press Web</h1>

      <h1 className="display-1">{count}</h1>

      {isAuthenticated && (
        <button
          className="btn btn-primary"
          onClick={handleIncrement}
        >
          PRESS ME
        </button>
      )}

      {error && (
        <div className="alert alert-warning container-fluid mt-2" role="alert">
          {error}
        </div>
      )}

    </div>
  )
}

export default App
