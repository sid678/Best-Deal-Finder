import React, {useState} from "react";
import SearchBar from "material-ui-search-bar";
import { makeStyles } from '@material-ui/core/styles';
import FilterListIcon from '@material-ui/icons/FilterList';
import {Button, Dialog, TextField, Paper} from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    main: {
        height: '65px',
        backgroundColor: '#263238',
        width: '100% !important',
        marginTop: '-20px',
    },
    searchBar: {
        width: '60%',
        margin: 'auto',
    },
    searchDiv: {
        paddingTop: '8px',
    },
    dialog: {
        position: 'absolute',
        right: 10,
        top: 50
    },
    dialogStyling: {
        padding: '20px'
    },
    paper: {
        width: '100% !important',
        backgroundColor: '#1E1E1E',
    }, 
}));

function AppHeader(props) {
    const classes=useStyles();
    const [searchQuery, setSearchQuery] = useState("");
    const [rangeSetDialog, openRangeSetDialog]=useState(false);
    const [price, setPriceFilter] = useState({
        minimum: "",
        maximum: "",
    })

    function onSearch() {
        openRangeSetDialog(false)
        window.location.href=`http://localhost:3000/search/`+searchQuery;
    }

    function handleChange(event) {
        let element=event.target.name;
        let value=event.target.value;
        setPriceFilter(prevValue => {
            return ({
                ...prevValue,
                [element]: value
            })
        })
    }

    function handleClick() {
        openRangeSetDialog(false);
        props.handleSetFilter(price.minimum, price.maximum);
    }

    return(
        <div className={classes.main} style={{position: 'fixed', zIndex: '3',}}>
            <Paper elevation = {3} className={classes.paper}>
            <div className={classes.searchDiv}>
                <div style={{width: '90%', display:'inline-block'}}>
                    <SearchBar
                        value={searchQuery}
                        onChange={(newValue) => setSearchQuery(newValue)}
                        onRequestSearch={() => onSearch()}
                        className={classes.searchBar}
                    />
                </div>
                <Button onClick={()=>{openRangeSetDialog(true)}}>
                    <FilterListIcon color="primary"/>
                </Button>
                <Dialog open={rangeSetDialog} onClose={() => {openRangeSetDialog(false)}} classes={{paper: classes.dialog}} className={classes.dialogStyling}>
                    <TextField id="minimum" name = "minimum" label="Minimum" style={{margin: '10px'}} variant="outlined" color="secondary" defaultValue="" value={price.minimum} onChange={handleChange}/>
                    <TextField id="maximum" name = "maximum" label="Maximum" style={{margin: '10px'}} variant="outlined" color="secondary" defaultValue="" value={price.maximum} onChange={handleChange}/>
                    <Button color="secondary" variant="contained" style={{margin: '10px'}} onClick={()=> {handleClick()}}>Set Filter</Button>
                </Dialog>
            </div>
            </Paper>
        </div>
    )
}

export default AppHeader;