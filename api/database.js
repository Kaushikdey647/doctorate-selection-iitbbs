const mongoose = require('mongoose');
const dotenv = require('dotenv');

//Environment Configuration
dotenv.config({
  path: `./api/config.env`,
});

//Generate Connection String
const db_url = process.env.DATABASE_CONN
  .replace('<username>',process.env.DATABASE_USER)
  .replace('<password>',process.env.DATABASE_PASSWORD)
  .replace('<database>',process.env.DATABASE_NAME);

//use the connection string
const connectDb = async () => {
  try {
    mongoose.connect(db_url, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to DB Successfully");
  } catch (err) {
    console.log("Error: ",err.message);
  }
}

//export connection object for use
module.exports = connectDb;