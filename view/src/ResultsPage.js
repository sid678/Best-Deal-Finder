import React, {useState, useEffect} from "react";
import AppHeader from "./AppHeader";
import {Avatar, Grid, Typography, Card, CardContent, CardActions, CardActionArea, CardMedia, Button, CircularProgress} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import StarRatings from 'react-star-ratings';
import axios from "axios"

const useStyles = makeStyles((theme) => ({   
    square: {
        display: 'block',
        maxWidth:'360px',
        maxHeight:'360px',
        width: 'auto',
        height: 'auto',
        marginLeft: 'auto',
        marginRight: 'auto',
        objectFit: 'cover'
    },
    imgdiv: {
        display: 'flex',
        height: '400px',
        alignItems: 'center',
        justigyContent: 'center'
    },
    container: {
        marginTop: '20px',
        backgroundColor: '#eeeeee'
    },
    pname: {
        width: '80%',
        textAlign: 'center',
        margin: 'auto'
    },
    pprice: {
        marginTop: '15px',
        marginBottom: '15px',
        color: '#d50000',
        width: '80%',
        textAlign: 'center',
        margin: 'auto'
    },
    ratingsDiv: {
        display: 'inline-block',
    },
    numratingsDiv: {
        display: 'inline-block',
    },
    pnumratings: {
        display: 'inline-block',
        marginLeft: '8px',
        color: '#0097a7'
    },
    pitem: {
        marginTop: '20px', 
        marginBottom: '20px',
    },
    progess: {
		position: 'relative',
        margin: 'auto',
        marginTop: '200px',
	},
}));

function ResultsPage(props) {
    const classes=useStyles();
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get(`/show_deal/` + props.match.params.productName)
        .then((response) => {
            setProducts(response.data.deals)
            setLoading(false)
        })
        .catch((error) => {
            console.log(error);
        })
    }, []);

    function handleSetFilter(minimum, maximum) {
        setProducts([]);
        setLoading(true);
        axios.get(`/show_deal/` + props.match.params.productName + '/' + minimum + '/' + maximum)
        .then((response) => {
            setProducts(response.data)
            setLoading(false)
        })
        .catch((error) => {
            console.log(error);
        })
    }

    return (
        <>
        <AppHeader page="ResultsPage" products={products} setProducts={setProducts} handleSetFilter={handleSetFilter}/>
        <Grid container className={classes.container} spacing={5}>
            {((loading===false) && products)? products.map((product) => {
                return(
                    <>
                        <Grid item xs={12} sm={6} md={4} lg={3} className={classes.pitem}>
                            <Card>
                                <CardActionArea>
                                    <CardMedia>
                                        <div className={classes.imgdiv}>
                                            <Avatar width='400px' height='400px' variant="square" src={product.img_url} className={classes.square} />
                                        </div>
                                    </CardMedia>
                                    <CardContent>
                                        <Typography variant="h5" className={classes.pname}><b>{product.name.slice(0, Math.min(product.name.length, 50))}</b></Typography>
                                        <Typography variant="h4" className={classes.pprice}>&#8377;{product.price_inr}</Typography>
                                        <center>
                                        <div className={classes.ratingsDiv}>
                                            <StarRatings rating={parseFloat(product.avg_rating.slice(0, 3))} starDimension = "25px" starSpacing = "2px" starRatedColor='#ffb300' name='rating' />
                                        </div>
                                        <div className={classes.numratingsDiv}>
                                            <Typography variant="body2" className={classes.pnumratings}>^{product.num_ratings}</Typography>
                                        </div>
                                        </center>
                                    </CardContent>
                                </CardActionArea>
                                {/* <CardActions> */}
                                    <center>
                                        <Button href={product.url} variant="contained" color="secondary" style={{marginTop: '15px', marginBottom: '15px'}}>Go to Product</Button>
                                    </center>    
                                {/* </CardActions> */}
                                
                            </Card>
                        </Grid>
                    </>
                )
            }):null
            }
            {
                loading && <>
                <CircularProgress size={100} color="secondary" className={classes.progess} />
                </>
            }
        </Grid>
        </>
    )
}

export default ResultsPage;