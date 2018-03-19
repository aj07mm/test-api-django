const React = require('react');
const App = require('./app');


const domElement = document.getElementById('react-app-books-list');

if (domElement) {
  React.render(<App />, domElement);
}
