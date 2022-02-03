# Lab 16 Serverless

## [Star Wars API](api/star_wars.py)

This app gets a random Star Wars Character from the database using a call to the Star Wars API (SWAPI). Upon refreshing the page, a new Star Wars Character will be generated.

Vercel Link: <https://vercel.com/jhuston5/serverless-app/EtRsurkwiQc3qAwQgYnP483ucN47/api/star_wars>

### Author: Joshua Huston

### Links/Resources

[https://swapi.dev/documentation]
[https://realpython.com/python-api/]

### Comments

Overall, this lab went fairly well. The big issue I had was keeping the functionality of the app very simple. At first I worked to hook up authentication with the Twitter API, and was successful up until pushing to Vercel. My SSL certificates are still causing issues. Instead, I connected to the Star Wars API and used a random number generator to select a random character from the API whenever the page is refreshed.
