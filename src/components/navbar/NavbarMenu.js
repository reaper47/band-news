import React, { Component } from 'react';
import styles from './styles.css';


class NavbarMenu extends Component {

  render() { 
    return (
      <div id="slide_menu"
           onMouseDown={this.props.handleMouseDown}
           className={this.props.menuShow ? styles.menu_show : styles.menu_hide}>

        {
          this.props.links.map(el => {
            return (
              <h2 className={styles.h2} key={el.name}>
                <a href={el.to} className={styles.a}>{el.name}</a>
              </h2>
            )
          })
        }
        
      </div>
    );
  }

};

export default NavbarMenu;
