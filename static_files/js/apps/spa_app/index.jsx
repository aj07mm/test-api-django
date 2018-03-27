import React from 'react'
import ReactDOM from 'react-dom'

import { createStore, combineReducers, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'

import createHistory from 'history/createBrowserHistory'

import { ConnectedRouter, BrowserRouter, routerReducer, routerMiddleware, push } from 'react-router-redux'

import { Router, Route, IndexRoute, browserHistory } from 'react-router'
import { reducers } from './reducers' // Or wherever you keep your reducers
// Create a history of your choosing (we're using a browser history in this case)
const history = createHistory()

// Build the middleware for intercepting and dispatching navigation actions
const middleware = routerMiddleware(history)

import App from './components/App';
import Foo from './components/Foo';

// Add the reducer to your store on the `router` key
// Also apply our middleware for navigating
const store = createStore(
  combineReducers({
    ...reducers,
    router: routerReducer
  }),
  applyMiddleware(middleware)
)

// Now you can dispatch navigation actions from anywhere!
// store.dispatch(push('/foo'))

ReactDOM.render(
  <Provider store={store}>
    <div>
        <Router history={browserHistory}>
            <Route path="/" component={App}>
                <Route path="foo" component={Foo}/>
                <Route path="bar" component={App}/>
            </Route>
        </Router>
    </div>
  </Provider>,
  document.getElementById('react-app')
)
