import redis # Import redis client to interact with redis server
import time # To manage time-based rate limiting
from fastapi import FastAPI, Request, HTTPException # FastAPI components help with API handling
from fastapi.responses import JSONResponse
from routes import router  # Import the router from routes.py

# Initialize FastAPI application and call routes
app = FastAPI()
app.include_router(router)

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Rate limiting settings
RATE_LIMIT = 100  # Max requests allowed
WINDOW_SIZE = 600  # Time window in seconds (10 minutes)

@app.middleware("http")
async def leaky_bucket_rate_limiter(request: Request, call_next):
    client_ip = request.client.host  # Identify user by IP (or API key later)
    current_time = time.time()  # Get current timestamp
    redis_key = f"rate_limit:{client_ip}"  # Unique key for each user

    
    # Define bucket settings
    BUCKET_CAPACITY = 100  # Max requests allowed in the bucket
    LEAK_RATE = 1  # Requests processed per second

    # Remove old requests beyond leak rate
    redis_client.ltrim(redis_key, 0, BUCKET_CAPACITY - 1)  # Keep only last N requests

    # Get the current bucket size
    bucket_size = redis_client.llen(redis_key)

    if bucket_size >= BUCKET_CAPACITY:
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

    # Add the current request to the bucket
    redis_client.lpush(redis_key, current_time)

    # Set expiration based on leak rate
    redis_client.expire(redis_key, BUCKET_CAPACITY // LEAK_RATE)

    return await call_next(request)