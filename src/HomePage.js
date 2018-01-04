import React, { Component } from 'react';
import NavbarContainer from './components/navbar/NavbarContainer';
import FbContainer from './components/fb/FbContainer';


class HomePage extends Component {
  
  render() {
    return (
      [
        <NavbarContainer key="NavbarContainer" />,
        <FbContainer key="FbContainer" />
      ]
    )
  }

}

export default HomePage;

