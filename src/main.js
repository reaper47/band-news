import React from 'react';
import ReactDOM from 'react-dom';
import NavbarContainer from './components/navbar/NavbarContainer';


document.addEventListener('DOMContentLoaded', function() {
  ReactDOM.render(
    React.createElement(NavbarContainer),
    document.getElementById('mount')
  );
});
