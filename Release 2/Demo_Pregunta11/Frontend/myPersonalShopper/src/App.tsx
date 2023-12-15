import {Navbar, Footer} from './components'
import './App.css'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Login from "./pages/Login.tsx"
import UserPurchases from "./pages/UserPurchases.tsx"
import ShopperSelections from "./pages/ShopperSelections.tsx"
import ShopperNewSelection from "./pages/ShopperNewSelection.tsx"
import {useState} from "react"

function App() {

  const [loggedIn, setLoggedIn] = useState(false)

  return (
    <Router>
      <Navbar/>
      <div className='content'>
        <Routes>
          <Route path='/' element={<div></div>}/>
          <Route path='/login' element={<Login/>}></Route>
          <Route path="/user_purchases" element = {<UserPurchases/>}></Route>
          <Route path="/my_selections" element = {<ShopperSelections/>}></Route>
          <Route path="/new_selection" element = {<ShopperNewSelection/>}></Route>
          <Route path="*" element={<p className='fs-1 bs-danger'>404 NOT FOUND</p>}/>
        </Routes>
      </div>
    </Router>
  )
}

export default App
