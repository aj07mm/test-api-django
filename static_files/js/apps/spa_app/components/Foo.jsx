import React, {  Component } from 'react';
import { connect } from 'react-redux';
import { ConnectedRouter, BrowserRouter, routerReducer, routerMiddleware, push } from 'react-router-redux'

import { activateGeod, closeGeod } from '../reducers';

import { Route } from 'react-router'

class Foo extends Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
            <div>Foo</div>
        </div>
    )
  }

}

// FooContainer.js
const mapStateToProps = (state, ownProps) => ({  
  geod: state.geod,
});

const mapDispatchToProps = {  
  activateGeod,
  closeGeod,
};


module.exports = connect(mapStateToProps, mapDispatchToProps)(Foo)
