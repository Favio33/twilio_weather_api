# API Weather Report Project

## Table of Contents

- [Introduction](#introduction)
- [How does it work?](#how)
- [Docker](#docker)

## Introduction

Hi there! This code was developed in Python 3.10 using Weather API and Twilio. The main purpose is to get which hours of the day are more probably to be rainy

## How does it work?

- You must run pip install -r requirements.txt
- Create an account on [Weather API](https://www.weatherapi.com/) to get the token API_KEY_WAPI
- Create an account on (Twilio)[https://www.twilio.com/en-us] and get a phone number, you could use the free trial
- The .env file is not in the repo, you must create it and set the following variables:
  - TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, PHONE_DESTINATION, API_KEY_WAPI
- Run main.py and check your whatsapp!
- The logs are storaged in src/logs

*If there is any error about import packages or modules, the current work directory is twilio_weather_api/*

## Docker

- The .dockerignore includes the virtual env create for this project
- The runtime was set up in Python 3.10
- The main directory is /app
- To run the container you can use Docker Desktop or a docker run {tagname} parm1{city} parm2{phone_destination}
