const React = require('react');
import Axios from '../../helpers/Axios';


class Rates extends React.Component {

    constructor(props){
        super(props);
        this.state = { results: [], errors: [], };
    }

    componentDidMount() {
        // get url
        const app = document.getElementById('react-app-books-review');
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
        if(this.state.results.length > 0){
            let rows = [];
            this.state.results.forEach((profile) => {
                rows.push(
                    (<tr>
                        <td>{ profile.uuid }</td>
                        <td>{ profile.full_name }</td>
                        <td>{ profile.current_position }</td>
                        <td><a href={ profile.profile_url } className="button">View profile</a></td>
                    </tr>)
                )

            });

            return (
                <div>
                    <table className="u-full-width">
                        <thead>
                            <tr>
                                <th>uuid</th>
                                <th>full name</th>
                                <th>current_position</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            { rows }
                        </tbody>
                    </table>
                </div>
            );
        }
        return (
            <div className="container">
                <div className="row">
                    <img style={{width: "50%"}} className="two-third column" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif" />
                </div>
            </div>
        );
    }
}


module.exports = Rates
