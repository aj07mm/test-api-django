const React = require('react');
//const App = require('./app');
import App from './app';


const domElement = document.getElementById('react-app');

if (domElement) {
  React.render(<App />, domElement);
}
