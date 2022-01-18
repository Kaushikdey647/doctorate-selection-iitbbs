# 1. doctorate-selection-iitbbs

## 1.1. Table of Contents

- [1. doctorate-selection-iitbbs](#1-doctorate-selection-iitbbs)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. Introduction](#12-introduction)
  - [1.3. How to use](#13-how-to-use)
  - [1.4. Structure of The App](#14-structure-of-the-app)
  - [1.5. Database](#15-database)
    - [1.5.1. Description](#151-description)
    - [1.5.2. Proposed Schema](#152-proposed-schema)
  - [1.6. Todo List](#16-todo-list)

## 1.2. Introduction

## 1.3. How to use

1. Either download this repository via this [link](https://github.com/Kaushikdey647/doctorate-selection-iitbbs/archive/refs/heads/main.zip) or clone this repository using
   `git clone https://github.com/Kaushikdey647/doctorate-selection-iitbbs`
2. Make sure you have [node](https://nodejs.org/) installed on your system.
3. Open up your command line/terminal
4. Run `npm start`
5. Open postman and redirect all requests to [http://localhost:9000](http://localhost:9000)

## 1.4. Structure of The App

The app will be divided into two parts

- API: A server api built on express
- Client: A user interface based on react

## 1.5. Database

### 1.5.1. Description

The database will be served by mongo atlas. It is expected to be a free cluster with about **512 MB** of space and a capacity of max **500 requests** hadndled at a time

### 1.5.2. Proposed Schema

- **creds**:
  - email,
  - password,
- **tenth**:
  - Institute,
  - Year,
  - Division,
  - Percentage,
  - CGPA,
  - CGPAMax
- **twelfth**:
  - Specialization,
  - Institute,
  - Year,
  - Division,
  - Percentage,
  - CGPA,
  - CGPAMax
- **bio**:
  - Name,
  - Type,
  - sponsoredAgency,
  - School,
  - Discipline,
  - ResearchArea1,
  - Gender,
  - Category,
  - PWD,
  - MTechThroughGate
- **gate**:
  - Discipline,
  - Score,
  - Percentile,
  - Rank,
  - Year,
  - Validity
  
- **masters**:
  - Programme,
  - Specialization,
  - Institute,
  - Year,
  - Division,
  - Percentage,
  - CGPA,
  - CGPAMax
  
- **bachelors**:
  - Programme,
  - Specialization,
  - Institute,
  - Year,
  - Division,
  - Percentage,
  - CGPA,
  - CGPAMax
  
- **net**:
  - Discipline,
  - Year
  
- **experience**:
  - Employer,
  - Designation,
  - PeriodBegin,
  - PeriodMonths,
  - Nature
  
- **others**:
  - Programme,
  - Institute,
  - Specialization,
  - Year,
  - Division,
  - Percentage,
  - CGPA,
  - CGPAMax

## 1.6. Todo List

- [x] Create the base api
  - [x] Create the base express app
  - [x] Connect to atlas server using mongoose
  - [ ] Create the database schema
  - [ ] Upload the data and give generic emails/passwords
  - [ ] Configure Routes for login and register
    - [ ] Configure the Login Route
      - [ ] Create login routers
      - [ ] Create login controllers
      - [ ] Configure JWT Tokens
    - [ ] Configure the Sign Up Route
      - [ ] Create signup routers
      - [ ] Create signup controllers
      - [ ] Configure JWT Tokens
  - [ ] Test the api
- [ ] Create react client
  - [ ] Decide on the React library versions
.
.
.
