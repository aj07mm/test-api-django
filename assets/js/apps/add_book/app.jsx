const React = require('react');
import Axios from '../../helpers/Axios';


class BookApp extends React.Component {

    constructor(props){
        super(props);
        this.state = { results: [], errors: [], };
    }

    componentDidMount() {
        // get url
        const app = document.getElementById('react-app-books-create');
        // do request
        Axios.get(app.getAttribute('data-url'))
        .then((response) => {
            this.setState({
                results: response.data.results,
            });
        })
        .catch((errors) => {
            this.setState({
                errors: errors
            }) 
        })
    }

    render() {

        const submitForm = () => {
        }

        return (
            <div className="container docs-example docs-example-forms">
                <form method="post">
                    <div className="row">
                        <label htmlFor="{{ profile_form.about_you.id_for_label }}">Title:</label>
                        <input className="u-full-width" name="asd" />
                    </div>
                    <div className="row">
                        <label htmlFor="{{ profile_form.about_you.id_for_label }}">ISBN number:</label>
                        <input className="u-full-width" name="asd" />
                    </div>
                    <button className="u-full-width" onclick={ submitForm }>Create</button>
                </form>
            </div>
        );
    }
}


module.exports = BookApp
