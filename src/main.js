import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from './components/navbar/Navbar';

document.addEventListener('DOMContentLoaded', function() {
  ReactDOM.render(
    React.createElement(Navbar),
    document.getElementById('mount')
  );
});
