import Axios from '../../helpers/Axios';

const React = require('react');


class BookReviewApp extends React.Component {
  constructor(props) {
    super(props);
    const app = document.getElementById('react-app-books-review');
    this.state = {
      app,
      rate: {
        title: null,
        isbn_number: null,
        book: app.getAttribute('data-attr-book-id'),
      },
      errors: [],
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const rate = Object.assign({}, this.state.rate);
    rate[event.target.name] = event.target.value;
    this.setState({ rate });
  }

  handleSubmit(event) {
    // disable default form behaviour
    event.preventDefault();
    // make ajax request
    Axios.post(
      this.state.app.getAttribute('data-url-rates'),
      this.state.rate,
    )
      .then(() => {
        window.location = '/home';
      })
      .catch(error => 
        this.setState({
          errors: Object.keys(error.response.data).map((key) => (
            `${key} - ${error.response.data[key]}`
          )),
        }),
      );
  }

  render() {
    return (
      <div className="container docs-example docs-example-forms">
        <form onSubmit={this.handleSubmit}>
          <div className="row">
            <label htmlFor="stars">Stars:</label>
            <input value={1} onChange={this.handleChange} type="checkbox" name="stars" /> 1 &nbsp;
            <input value={2} onChange={this.handleChange} type="checkbox" name="stars" /> 2 &nbsp;
            <input value={3} onChange={this.handleChange} type="checkbox" name="stars" /> 3 &nbsp;
            <input value={4} onChange={this.handleChange} type="checkbox" name="stars" /> 4 &nbsp;
            <input value={5} onChange={this.handleChange} type="checkbox" name="stars" /> 5 &nbsp;
          </div>
          <div className="row">
            <label htmlFor="review">Review:</label>
            <textarea className="u-full-width" id="review" value={this.state.rate.isbn_number} onChange={this.handleChange} type="text" name="review" />
          </div>
          <button className="u-full-width button-primary">Create</button>
        </form>
        <ul>
          { this.state.errors.length > 0 && this.state.errors.map((error) => <li>{ error }</li>)}
        </ul>
      </div>
    );
  }
}


module.exports = BookReviewApp;
