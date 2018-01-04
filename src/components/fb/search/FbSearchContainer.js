import React, { Component } from 'react';
import styles from './styles.css';


class FbSearchContainer extends Component {

  constructor() {
    super();

    this.state = {
      band: ''
    }

    this.icon = "http://www.endlessicons.com/wp-content/uploads/2012/12/search-icon.png";

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleSearchChange = this.handleSearchChange.bind(this);
  } 

  handleSearchChange(e) {
    this.setState({ 
      band: e.target.value 
    });
  }

  handleSubmit(e) { 
    e.preventDefault();
    console.log(this.state.band);
    
  }

  render() {
    return (
      <form id="fb_search_form" 
            className={styles.fb_search_container} 
            onSubmit={this.handleSubmit}>
        
        <input type="text"
               id="fb_search_input"
               className={styles.fb_search} 
               placeholder="Which band may I help you with?" 
               value={this.state.band}
               onChange={this.handleSearchChange} />

        <a href="#" onClick={this.handleSubmit}>
          <img className={styles.fb_search_icon} 
               src={this.icon} />
        </a>
      </form>
    )
  }

}

export default FbSearchContainer;

