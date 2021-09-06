import { createMuiTheme } from '@material-ui/core/styles';

const theme=createMuiTheme({
    typography: {
        fontFamily: `'Roboto', sans-serif`,
        h3 : {
            fontSize: '2.7rem',
            '@media (max-width:600px)': {
                fontSize: '1.8rem',
            }, 
            fontWeight: "650",
        },
    },
    palette: {
        primary: {
            main: '#fafafa'
        },
        secondary: {
            main: '#212121',
        },
        inherit: {
            main: '#29b6f6'
        },
        info: {
            main: '#00e676'
        },
        error: {
            main: '#e53935'
        }
    },
});

export default theme;