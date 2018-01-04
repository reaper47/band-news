import React from 'react';
import ReactDOM from 'react-dom';
import HomePage from './HomePage';


document.addEventListener('DOMContentLoaded', function() {
  ReactDOM.render(
    React.createElement(HomePage),
    document.getElementById('mount')
  );
});
