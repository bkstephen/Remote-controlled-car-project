
//Load HTTP module
const http = require("http");
const hostname = '192.168.1.100';
const port = 3000;
const express = require('express');
const app = express();
const expresslayouts = require('express-ejs-layouts');
const PORT = process.env.PORT || 3000;
app.listen(PORT, console.log('Server started on port ' + PORT));
const direction = require('./handler.js');

//expressjs
app.use(expresslayouts);
app.set('view engine', 'ejs');
app.set('view options', { layout: false });

//Bodyparser
app.use(express.urlencoded({ extended: false }))
var d = null;


app.get('/index', (req, res)=>{
    res.render('index',{direction:null});    
} );

app.post('/index',(req, res)=>{
    d = req.body.button;
    req.body.direction = d;
    res.render('index',{direction:d});
} );

app.get('/', (req, res)=>{
    res.send({d}); 
});
