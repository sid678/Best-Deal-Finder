import React from "react";
import AppHeader from "./AppHeader"
import logo from "../src/logo3.JPG"
import { makeStyles } from '@material-ui/core/styles';
import { Typography } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({   
    img: {
        marginTop: '100px',
    }
}));

function WelcomePage() {
    const classes=useStyles();
    return (
        <>
        <br/>
        <AppHeader page="WelcomePage"/>
        <center>
            <img src={logo} width="400" height="400" className={classes.img}/>
        </center>

        </>
    )
}

export default WelcomePage;