# fast-api-rate-limiter
I Rate-Limited My Own API. Because Even Good Ideas Need Boundaries.


FastAPI Rate-Limited Public API

### Overview

This project is a FastAPI-based public API that implements rate limiting using Redis. The goal is to prevent excessive API usage by enforcing request limits per user/IP within a specified time window. This ensures fair usage and prevents abuse.

Why This Project?

This API is being built to provide public access to a set of endpoints while maintaining stability and security. Public APIs are often targeted by scrapers, bots, or excessive requests from users, which can degrade performance. Implementing rate limiting and authentication ensures that resources are fairly distributed, protects against DDoS attacks, and encourages responsible API consumption.

Current Features

FastAPI-based API: A lightweight, high-performance backend.

Redis-based Rate Limiting: Limits requests per IP using a fixed window approach.

Configurable Rate Limits: Set a maximum number of requests per time window (e.g., 100 requests per 10 minutes).

Middleware Implementation: Rate limiting is enforced through FastAPI’s middleware.

HTTP 429 Too Many Requests: Users exceeding the limit receive an appropriate error response.

Upcoming Features

To make this API more robust and production-ready, the following enhancements are planned:

JWT-Based Authentication

Implement authentication via JSON Web Tokens (JWTs).

Allow authenticated users to have different rate limits compared to anonymous users.

Secure endpoints using OAuth2 password flow with JWT.

Custom Rate Limits per User Type

Implement different rate limits for:

Anonymous users: 100 requests per 10 minutes.

Authenticated users: 500 requests per 10 minutes.

Premium users: Higher or unlimited requests.

Modify the rate limiter middleware to check user roles and apply appropriate limits.

Enhanced Security Measures

Implement IP whitelisting for internal use cases.

Introduce blacklisting for abusive clients exceeding limits repeatedly.

Deployment and Scalability

Dockerize the application for easy deployment.

Deploy using AWS, GCP, or Azure.

Integrate a reverse proxy (NGINX, Traefik) for additional rate limiting at the network level.

Installation and Setup

Prerequisites

Python 3.8+

Redis Server

FastAPI & Uvicorn

Installation

Clone the repository:

git clone https://github.com/yourusername/fastapi-rate-limit-api.git
cd fastapi-rate-limit-api

Install dependencies:

pip install -r requirements.txt

Run Redis server (if not already running):

redis-server

Start the FastAPI server:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Test the API:

Open your browser and visit: http://127.0.0.1:8000/docs

Use tools like Postman or curl to send requests.

API Endpoints

Method

Endpoint

Description

GET

/public

Publicly accessible endpoint

GET

/protected

Requires JWT authentication

GET

/rate-limited

Example endpoint with enforced rate limits

POST

/token

Generate JWT token for authentication

Authentication (Upcoming)

Once JWT authentication is implemented, users will need to:

Register/Login to receive a JWT token.

Include the JWT token in the Authorization header (Bearer <token>).

Receive different rate limits based on their authentication level.

Stay Tuned!

More enhancements are on the way. Contributions and feedback are welcom
