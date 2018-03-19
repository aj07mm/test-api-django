const React = require('react');
const App = require('./app');


const domElement = document.getElementById('react-app-books-review');

if (domElement) {
  React.render(<App />, domElement);
}
