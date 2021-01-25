
import './App.css';
import { API } from "./backend";
import React, {useState, useEffect} from 'react';

// export const getProducts = () => {
//   return fetch(`${API}product`, { method: "GET" })
//     .then((response) => {
//       return response.json();
//     })
//     .catch((err) => console.log(err));
// };


export default function App() {

  // useState hook returns an array with 2 elements, the current state and the set state function
  let [responseData, setResponseData] = useState('');


  // useEffect hook takes 2 parameters, a function and an array and returns nothing
  // the function it takes will be executed every render cycle

  // The useEffect hook takes a second argument, which controls if the function should be executed.
  // It is an array of values, and the useEffect function will only be executed if one of the values in the array changes.

  // useEffect takes in an empty array in the second argument. In this case, since there is 
  // no value in the array, the function will not be called again.

  useEffect(() => {

    setResponseData('hello nah nah')
    console.log(responseData)
  }, [setResponseData, responseData])

  // const headers = {

  //   'Accept': 'application/json',
  //   // 'Authorization': token

  // }

  // const get = () =>
  // fetch(`${API}product`, { headers,  })
  //   .then(res => res.json())
  //   .catch(err => console.log(err))


    // .then(data => data.book)


  return (
    <div className="App">
      <header className="App-header">
    
        <p>
          Tesing BACKEND API here using react hook
        </p>

      </header>
    </div>
  );
}


