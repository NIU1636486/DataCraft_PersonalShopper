import {Navbar, Footer, ChatButton} from './components'
import './App.css'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Login from "./pages/Login.tsx"
import UserPurchases from "./pages/UserPurchases.tsx"
import {useState} from "react"

function App() {

  const [loggedIn, setLoggedIn] = useState(false)

  return (
    <Router>
      <Navbar/>
      <div className='content'>
        <Routes>
          <Route path='/' element={<p>Home</p>}/>
          <Route path='/login' element={<Login/>}></Route>
          <Route path="/user_purchases" element = {<UserPurchases/>}></Route>
          <Route path="*" element={<p className='fs-1 bs-danger'>NOOOOOOO</p>}/>
        </Routes>
      </div>
      <Footer/>
    </Router>
  )
}

export default App
