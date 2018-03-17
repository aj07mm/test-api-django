const React = require('react');
import Axios from '../../helpers/Axios';


class BooksApp extends React.Component {

    constructor(props){
        super(props);
        this.state = { isLoading: false, results: [], errors: [], };
    }

    componentDidMount() {
        // get url
        const app = document.getElementById('react-app-books');
        // is loading
        this.setState({ isLoading: true })
        // do request
        Axios.get(app.getAttribute('data-url'))
        .then((response) => {
            this.setState({
                results: response.data.results,
                isLoading: false,
            });
        });
    }

    render() {
        let tableContent = null
        if(this.state.results.length > 0){
            let rows = [];
            this.state.results.forEach((book) => {
                rows.push(
                    (<tr>
                        <td>{ book.id }</td>
                        <td>{ book.isbn_number }</td>
                        <td>{ book.title }</td>
                        <td><a href={ book.book_url } className="button">Review book</a></td>
                    </tr>)
                );
            });
            tableContent = rows;
        }

        return (
            <div>
                <table className="u-full-width">
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>isbn_number</th>
                            <th>title</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        { 
                            this.state.isLoading ?
                            <img style={{width: "50%"}} className="two-third column" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif" /> :
                            tableContent
                        }
                    </tbody>
                </table>
            </div>
        );
    }
}


module.exports = BooksApp
