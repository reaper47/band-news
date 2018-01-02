import React from 'react';
import NavbarButton from './NavbarButton';
import NavbarMenu from './NavbarMenu';


class Navbar extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      show: false
    }

    this.toggleMenu = this.toggleMenu.bind(this);
  }

  toggleMenu() {
    this.setState({ 
      show: !this.state.show 
    });
  }

  render() {
    return (
      <div id="navbar-root">
        <NavbarButton handler={this.toggleMenu} />
        {this.state.show ? <NavbarMenu /> : ''}
      </div>
    );
  }
}

export default Navbar
