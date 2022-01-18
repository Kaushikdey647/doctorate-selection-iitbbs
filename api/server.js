const dotenv = require('dotenv'); //for env variables
const morgan = require('morgan'); //
const database = require('./database'); //Database object
const app = require('./app'); //The express app as in app.js

//Environment Variables for use
dotenv.config({
  path: './api/config.env',
});

//initialize the database
database();


const port = process.env.PORT || 9000;

console.log(`Mode : ${process.env.NODE_ENV}`);

app.listen(port, (req, res) => {
  console.log(`App Running on port ${port}`);
});