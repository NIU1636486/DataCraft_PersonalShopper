import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';


function NavBar() {
  return(
  <Navbar expand="lg" className='bg-body-tertiary'>
   <Container>
    <Navbar.Brand href="">myPersonalShopper DEMO</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav">
     <Nav className="me-auto">
      <NavDropdown title="User" id="basic-nav-dropdown">
      <Nav.Link href="/user_purchases">My purchases</Nav.Link>
      </NavDropdown>
      <NavDropdown title="Shopper" id="basic-nav-dropdown">
      <Nav.Link href="/my_selections">My selections</Nav.Link>
      <Nav.Link href="/new_selection">New selection</Nav.Link>
      </NavDropdown>
     </Nav>
    </Navbar.Collapse>
   </Container>
  </Navbar>)
  
}

export default NavBar