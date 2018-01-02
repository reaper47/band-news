import React from 'react';


class NavbarButton extends React.Component {
  
  render() {
    return (
      <div id="navbar-btn">
        <button onClick={this.props.handler} title="toggle menu">
          Click Me
        </button>
     </div>
   );
  }
  
};

export default NavbarButton;
