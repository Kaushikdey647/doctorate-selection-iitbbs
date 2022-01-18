# 1. doctorate-selection-iitbbs

## 1.1. Table of Contents

- [1. doctorate-selection-iitbbs](#1-doctorate-selection-iitbbs)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. Introduction](#12-introduction)
  - [1.3. How to use](#13-how-to-use)
  - [1.4. Structure of The App](#14-structure-of-the-app)
  - [1.5. Database](#15-database)
    - [Description](#description)
    - [Proposed Schema](#proposed-schema)
  - [1.6. Todo List](#16-todo-list)

## 1.2. Introduction

## 1.3. How to use

## 1.4. Structure of The App

The app will be divided into two parts

- API: A server api built on express
- Client: A user interface based on react

## 1.5. Database

### Description

The database will be served by mongo atlas. It is expected to be a free cluster with about 512mb of space and a capacity of max 500 requests hadndled at a time

### Proposed Schema

- Creds
  - Email
  - Password(Hash)
- <Fill The Schema>
  
## 1.6. Todo List

- [ ] Create the base api
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
