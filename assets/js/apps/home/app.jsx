import React, {  Component } from 'react';
import { connect } from 'react-redux';
import { ConnectedRouter, BrowserRouter, routerReducer, routerMiddleware, push } from 'react-router-redux'

import { activateGeod, closeGeod } from './reducers';

import { Route } from 'react-router'

class App extends Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
            <div>xas asd dasd</div>
        </div>
    )
  }

}

// AppContainer.js
const mapStateToProps = (state, ownProps) => ({  
  geod: state.geod,
});

const mapDispatchToProps = {  
  activateGeod,
  closeGeod,
};


module.exports = connect(mapStateToProps, mapDispatchToProps)(App)
