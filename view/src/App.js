import React from "react";
import { Route, Switch, BrowserRouter as Router } from 'react-router-dom';
import {ThemeProvider } from '@material-ui/core/styles';
import axios from "axios";
import ResultsPage from './ResultsPage';
import WelcomePage from './WelcomePage';
import Test from './Test';
import theme from './theme';

axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <ThemeProvider theme = {theme}>
                        <Route exact path="/" component={WelcomePage}/>
                        <Route exact path="/search/:productName" component={ResultsPage}/>
                        <Route exact path="/test" component={Test} />
                    </ThemeProvider>
                </Switch>
            </div>
        </Router>
    )
}

export default App;