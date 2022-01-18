const express = require('express');
const morgan = require('morgan');
//routers

/**
 * The app executes all the middlewares in the middleware chain
 * They are executed in specified order so watch it
 * Put anything you want in the format app.use()
*/
const app = express();

//GENERAL MIDDLEWARES///////////////////////

//Morgan logs down all the requests into dev console
if (process.env.NODE_ENV === 'development') {
  //enable developer features
  app.use(morgan('dev')); //ooh!! morgan!!
}

//This will parse the json files for us
app.use(express.json());

//This will serve static files to client if needed
// app.use(express.static(`${__dirname}/public`));

//This will save the current date-time to request object
app.use((req, res, next) => {
  req.requestTime = new Date().toISOString(); //when the request time is
  //this is now saved as a property of req the object
  next(); //call the next middleware in the stack
});

//CUSTOM MIDDLEWARES///////////////////////

// app.use('your/route/here',yourRouterHere);

//And finally export the app for use

module.exports = app;