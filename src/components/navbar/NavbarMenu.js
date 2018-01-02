import React from 'react';


class NavbarMenu extends React.Component {
  
  render() {
    const menuItems = [
      'facebook news',
      'web news',
      'tour calendar',
    ]

    return (
      <div id="navbar-menu">
        <ul>
          {menuItems.map(item => <li>{item}</li>)}          
        </ul>
      </div>
    );
  }

};

export default NavbarMenu;
