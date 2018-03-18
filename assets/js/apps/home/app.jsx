const React = require('react');
import Axios from '../../helpers/Axios';


class HomeApp extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            isLoading: false,
            results_books: [],
            results_rates: [],
            errors: [],
        };
    }

    componentDidMount() {
        // get url
        const app = document.getElementById('react-app-books');
        // is loading
        this.setState({ isLoading: true })
        // do request
        Axios.all([
            Axios.get(app.getAttribute('data-url-books')),
            Axios.get(app.getAttribute('data-url-rates')),
        ])
        .then((responses) => {
            this.setState({
                results_books: responses[0].data.results,
                results_rates: responses[1].data.results,
                isLoading: false,
            });
        });
    }

    render() {
        let tableContentBooks = null
        let tableContentRates = null
        if(this.state.results_books.length > 0){
            let rows = [];
            this.state.results_books.forEach((book) => {
                rows.push(
                    (<tr>
                        <td>{ book.id }</td>
                        <td>{ book.isbn_number }</td>
                        <td>{ book.title }</td>
                        <td>{ book.created_by.username }</td>
                        <td><a href={ book.review_book_url } className="button">Review book</a></td>
                    </tr>)
                );
            });
            tableContentBooks = rows;
        } else {
            tableContentBooks = <tr><td colSpan="5" style={{textAlign: "center"}}>Empty!</td></tr>;
        }
        if(this.state.results_rates.length > 0){
            let rows = [];
            this.state.results_rates.forEach((rate) => {
                rows.push(
                    (<tr>
                        <td>{ rate.id }</td>
                        <td>{ rate.stars }</td>
                        <td>{ rate.review }</td>
                        <td>{ rate.created_by.username }</td>
                        <td>{ rate.book }</td>
                    </tr>)
                );
            });
            tableContentRates = rows;
        } else {
            tableContentRates = <tr><td colSpan="5" style={{textAlign: "center"}}>Empty!</td></tr>;
        }

        const loadingSpinner = (
            <img style={{width: "50%"}} className="two-third column" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif" />
        )

        return (
            <div>
                <h5>My Books</h5>
                <table className="u-full-width">
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>isbn_number</th>
                            <th>title</th>
                            <th>created by</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.isLoading ?
                            loadingSpinner :
                            tableContentBooks
                        }
                    </tbody>
                </table>
                <br/>
                <h5>My Reviews and reviews others wrote for my books</h5>
                <table className="u-full-width">
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>stars</th>
                            <th>review</th>
                            <th>created by</th>
                            <th>book</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.isLoading ?
                            loadingSpinner :
                            tableContentRates
                        }
                    </tbody>
                </table>
            </div>
        );
    }
}


module.exports = HomeApp
