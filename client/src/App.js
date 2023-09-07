import React, { useState, useEffect } from 'react';

const App = () => {

  // fetches data from backend
  const [data, setData] = useState([{}])

  // fetch the data from the backend then update the data useState
  useEffect(() => {
    fetch("/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div>

    </div>
  );
}

export default App;
