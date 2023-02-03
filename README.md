## Introduction
This repo is to store scripts, pipelines and  services related to house-of-home-grown
Microservice architecture is followed here for scalability and reliability 

There are 14 main components of house-of-home-grown e-commerce:
* [User Service] - user login, authentication and authorization, add user, delete user
* [Product Service] - all product related activities (add delete update view)
* [Cart Service] - all cart related endpoints
* [Order Service] - all order related endpoints (old orders, place order, approve order, track, return, status)
* [Customer Service] - all customer private details like billing address, postal address, payment methods, customer rating etc
* [Vendor Service] - all vendor private details like warehouse address, gst etc
* [Payment Service] - processing payment and checking fraud
* [Content Service] - managing and serving static content (headers, footers, category, theme etc)
* [Inventory Service] - managing inventory for pre and post order
* [Analytics Service] - providing analytics to both admin and vendor
* [Recommendation Service] - targeted recommendations for user and general recommendations, similar products, also bought etc
* [Autosuggest Service] - for search and autocomplete
* [Notification Service] - for providing notification to users
* [User Interface] - UI for the web

# Deployment
* Deployment for this project is through docker.
* There are three types of deployment:
 - Dev - for development
 - Staging - for staging environment
 - Production - for production environment
* Deployment can be done using run.sh script with the required deployment 
 - example - sh run.sh dev (This command is for mac and linux)