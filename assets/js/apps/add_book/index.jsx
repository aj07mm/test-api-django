var React = require('react')
var App = require('./app');


const domElement = document.getElementById('react-app-books-create');

if (domElement) {
    React.render(<App/>, domElement);
}
