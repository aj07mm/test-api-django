const React = require('react');
import Axios from '../../helpers/Axios';


class Welcome extends React.Component {

    constructor(props){
        super(props);
        this.state = { results: [] };
    }

    componentDidMount() {
        Axios.get('/api/profiles')
        .then((response) => {
            this.setState({
                results: response.data.results,
            });
        });
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

            const doRequest = () => {
                Axios.post('/api/profiles/', {})
                .then((response) => {
                    this.setState({
                        results: response.data.results,
                    });
                });
            }

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
                    <button onClick={ doRequest }></button>
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


module.exports = Welcome
