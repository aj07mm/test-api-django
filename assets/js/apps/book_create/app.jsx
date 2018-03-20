import Axios from '../../helpers/Axios';

const React = require('react');


class BookCreateApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      app: document.getElementById('react-app-books-create'),
      book: { title: null, isbn_number: null },
      errors: [],
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const book = Object.assign({}, this.state.book);
    book[event.target.name] = event.target.value;
    this.setState({ book });
  }

  handleSubmit(event) {
    // disable default form behaviour
    event.preventDefault();
    // make ajax request
    Axios.post(
      this.state.app.getAttribute('data-url-books'),
      this.state.book,
    )
      .then(() => {
        window.location = '/home';
      })
      .catch((error) => {
        this.setState({
          errors: Object.keys(error.response.data).map(key => `${key} - ${error.response.data[key]}`),
        });
      });
  }

  render() {
    return (
      <div className="container docs-example docs-example-forms">
        <form onSubmit={this.handleSubmit}>
          <div className="row">
            <label htmlFor="title">Title:</label>
            <input className="u-full-width" id="title" value={this.state.book.title} onChange={this.handleChange} type="text" name="title" />
          </div>
          <div className="row">
            <label htmlFor="{{ profile_form.about_you.id_for_label }}">ISBN number:</label>
            <input className="u-full-width" value={this.state.book.isbn_number} onChange={this.handleChange} type="text" name="isbn_number" />
          </div>
          <button className="u-full-width button-primary">Create</button>
        </form>
        <ul>
          { this.state.errors.length > 0 && this.state.errors.map(error => <li>{ error }</li>)}
        </ul>
      </div>
    );
  }
}


module.exports = BookCreateApp;
