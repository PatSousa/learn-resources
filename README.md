[![Build Status](https://travis-ci.org/PatSousa/learn-resources.svg?branch=master)](https://travis-ci.org/PatSousa/learn-resources)

# REST API to hold learn resources

## Installation
    1. create virtual environment
    2. pip install -r requirements.txt
    3. ./manage.py migrate

## Purpose

The purpose of this project was to create a REST API using DRF to handle the learning resources a user finds online.
Should be part of a project to have a learning resources DB where one can store and consult the resources found online.

## API specifications

The endpoints for the API are:

| Endpoints        | HTTP Method   | CRUD Method | Result                         |
| ---------------- | ------------- | ----------- | ------------------------------ |
| resources        | GET           |  READ       | Get all resources for the user |
| resources/:id    | GET           |  READ       | Get the resouce with id        |
| resources        | POST          |  CREATE     | Add a resource                 |
| resources/:id    | PUT           |  UPDATE     | Update a resource              |
| resources/:id    | DELETE        |  DELETE     | Delete a single resource       | 
