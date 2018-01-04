import React, { Component } from 'react';
import FbSearchContainer from './search/FbSearchContainer';


class FbContainer extends Component {
  
  constructor() {
    super();
  }

  render() {
    return (
      <div id="fb_root">
        <FbSearchContainer />
      </div>
    )
  }

}

export default FbContainer;

