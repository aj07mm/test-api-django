const React = require('react');
//const App = require('./app');
import App from './app';
import Foo from './foo';
import { Router, Route, hashHistory, browserHistory } from 'react-router'
import { createHistory } from 'history';

const domElement = document.getElementById('react-app');

if (domElement) {
    React.render(
        <div>
            <Router history={hashHistory}>
                <Route path="/" component={App}/>
                <Route path="/foo" component={Foo}/>
            </Router>
        </div>, 
        domElement
    );
}
