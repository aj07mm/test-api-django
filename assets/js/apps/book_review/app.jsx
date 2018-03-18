const React = require('react');
import Axios from '../../helpers/Axios';


class BookReviewApp extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            app: document.getElementById('react-app-books-review'),
            rate: { title: null, isbn_number: null, book: null, },
            bookOptions: [],
            results: [],
            errors: [],
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        const app = document.getElementById('react-app-rates-review');

        // load books for book select
        Axios.get(this.state.app.getAttribute('data-url-books'))
        .then((response) => {
            this.setState({
                bookOptions: response.data.results.map((book) => (
                   { 'key': book.title, 'value': book.id, }
                ))
            });
        });
    }

    handleChange(event) {
        let rate = Object.assign({}, this.state.rate);
        rate[event.target.name] = event.target.value
        this.setState({rate});
    }

    handleSubmit(event) {
        // disable default form behaviour
        event.preventDefault();
        // make ajax request
        Axios.post(
            this.state.app.getAttribute('data-url-rates'),
            this.state.rate,
        )
        .then((response) => {
            window.location = '/home';
        })
        .catch((error) => {
            this.setState({
                errors: Object.keys(error.response.data).map((key, index) => {
                    return key + ' - ' + error.response.data[key];
                })
            });
        });

    }

    render() {
        return (
            <div className="container docs-example docs-example-forms">
                <form onSubmit={ this.handleSubmit }>
                    <div className="row">
                        <label htmlFor="{{ profile_form.about_you.id_for_label }}">Stars:</label>
                        <input value={1} onChange={this.handleChange} type="checkbox" name="stars" /> 1 &nbsp;
                        <input value={2} onChange={this.handleChange} type="checkbox" name="stars" /> 2 &nbsp;
                        <input value={3} onChange={this.handleChange} type="checkbox" name="stars" /> 3 &nbsp;
                        <input value={4} onChange={this.handleChange} type="checkbox" name="stars" /> 4 &nbsp;
                        <input value={5} onChange={this.handleChange} type="checkbox" name="stars" /> 5 &nbsp;
                    </div>
                    <div className="row">
                        <label htmlFor="{{ profile_form.about_you.id_for_label }}">Review:</label>
                        <textarea className="u-full-width" value={this.state.rate.isbn_number} onChange={this.handleChange} type="text" name="review" />
                    </div>
                    <div className="row">
                        <label htmlFor="{{ profile_form.about_you.id_for_label }}">Book:</label>
                        <select className="u-full-width" value={this.state.rate.book} onChange={this.handleChange} name="book">
                            {
                                this.state.bookOptions.length > 0 &&
                                this.state.bookOptions.map((bookOption, i) => <option value={bookOption.value}>{ bookOption.key }</option>)
                            }
                            <option>Select one</option>
                        </select>
                    </div>
                    <button className="u-full-width button-primary">Create</button>
                </form>
                <ul>
                    { this.state.errors.length > 0 && this.state.errors.map((error, i) => <li>{ error }</li>)}
                </ul>
            </div>
        );
    }
}


module.exports = BookReviewApp
