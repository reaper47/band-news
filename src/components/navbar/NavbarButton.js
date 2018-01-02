import React, { Component } from 'react';
import styles from './styles.css';


class NavbarButton extends Component {
  
  render() {
    return (
      <button className={styles.navbar_btn}
              onMouseDown={this.props.handleMouseDown}
              title="open menu">
      </button>
   );
  }
  
};

export default NavbarButton;
