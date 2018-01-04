import React, { Component } from 'react';
import NavbarButton from './NavbarButton';
import NavbarMenu from './NavbarMenu';
import styles from './styles.css';


class NavbarContainer extends Component {

  constructor(props) {
    super(props);

    this.state = {
      show: false 
    };

    this.links = [
      { name: 'facebook news', to: '#' },
      { name: 'web news', to: '#' }, 
      { name: 'tour calendar', to: '#' }
    ];

    this.handleMouseDown = this.handleMouseDown.bind(this);
    this.toggleMenu = this.toggleMenu.bind(this);
  }

  handleMouseDown(e) {
    this.toggleMenu();
    e.stopPropagation();
  }

  toggleMenu() {
    this.setState({ 
      show: !this.state.show 
    });
  }

  render() {
    return (
      [
        <NavbarButton key="NavbarButton" 
                      handleMouseDown={this.handleMouseDown} />,
        <NavbarMenu key="NavbarMenu"
                    handleMouseDown={this.handleMouseDown}
                    menuShow={this.state.show} 
                    links={this.links} />
      ]
      
    );
  }
}

export default NavbarContainer;
