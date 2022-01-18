const mongoose = require('mongoose');

/*
YOU HAVE TO GO FROM HERE

{
  name:
  rating:
  price:
}

TO HERE

{
  creds:{
    email: '',
    password: '',
  }
  tenth:{
    Institute,
    Year,
    Division,
    Percentage,
    CGPA,
    CGPAMax
  },
  twelfth:{
    Specialization,
    Institute,
    Year,
    Division,
    Percentage,
    CGPA,
    CGPAMax
  },
  bio:{
    Name,
    Type,
    sponsoredAgency,
    School,
    Discipline,
    ResearchArea1,
    Gender,
    Category,
    PWD,
    MTechThroughGate
  }
  gate:{
    Discipline,
    Score,
    Percentile,
    Rank,
    Year,
    Validity
  }
  masters:{
    Programme,
    Specialization,
    Institute,
    Year,
    Division,
    Percentage,
    CGPA,
    CGPAMax
  }
  bachelors:{
    Programme,
    Specialization,
    Institute,
    Year,
    Division,
    Percentage,
    CGPA,
    CGPAMax
  }
  net:{
    Discipline,
    Year
  }
  experience:{
    Employer,
    Designation,
    PeriodBegin,
    PeriodMonths,
    Nature
  }
  others:{
    Programme,
    Institute,
    Specialization,
    Year,
    Division,
    Percentage,
    CGPA,
    CGPAMax
  }
}


*/

//schema for institute details
const insti = new mongoose.Schema({
  programme: {
    type: String,
  },
  institute: {
    type: String,
  },
  specialization: {
    type: String,
  },
  year: {
    type: Number,
  },
  division: {
    type: Number,
  },
  percentage: {
    type: Number,
  },
  cgpa: {
    type: Number,
  },
});

const net = new mongoose.Schema({
  discipline: {
    type: String,
  },
  year: {
    type: Number,
  },
  cleared: {
    type: Boolean,
    required: true
  }
})

const creds = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
})

const gate = new mongoose.Schema({
  discipline: {
    type: String,
  },
  score: {
    type: String,
  },
  percentile: {
    type: Number,
  },
  rank: {
    type: Number,
  },
  year: {
    type: Number,
  },
  validity: {
    type: Number,
  },
  cleared: {
    type: Boolean,
    required: true,
  }
})

const bio = new mongoose.Schema({
  name: {
    type: String,
    required: [true, "A Name Is Required"],
  },
  type: {
    type: String,
    required: [true, "A Name Is Required"],
  },
  sponsoredAgency: {
    type: String,
  },
  school: {
    type: String,
    required: [true, "Please Specify School"],
  },
  discipline: {
    type: String,
    required: [true, "Please Specify Discipline"],
  },
  researchArea1: {
    type: String,
    required: [true, "A Name Is Required"],
  },
  gender: {
    type: String,
    required: [true, "A Name Is Required"],
  },
  category: {
    type: String,
    required: [true, "A Name Is Required"],
  },
  pwd: {
    type: Boolean,
    required: [true, "A Name Is Required"],
  },
  mtechthroughgate: {
    type: Boolean,
    required: [true, "A Name Is Required"],
  },
})

const experience = new mongoose.Schema({
  employer: {
    type: String,
  },
  designation: {
    type: String,
  },
  periodbegin: {
    type: Date
  },
  periodmonths: {
    type: Number,
  },
  nature: {
    type: String,
  },
})

const studentSchema = new mongoose.Schema({
  credentials: {
    type: creds,
    required: true,
  },
  bio: {
    type: bio,
    required: true,
    
  },
  tenth: {
    type: insti,
    required: true,
    
  },
  twelfth: {
    type: insti,
    required: true,
    
  },
  bachelors: {
    type: insti,
    required: true,
    
  },
  masters: {
    type: insti,
    
  },
  gate: {
    type: gate,
  },
  net: {
    type: net,
  },
  others: {
    type: [insti],
    
  },
  experience: {
    type: [experience],
    
  },
});

const Student = mongoose.model('Student', studentSchema); //'Student' is the collection the model is for, and StudentSchema is well, the schema
//now Student is the object that can be used to fill in new objects
module.exports = Student;