import redis # Import redis client to interact with redis server
import time # To manage time-based rate limiting
from fastapi import FastAPI, Request, HTTPException # FastAPI components help with API handling
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
async def sliding_window_rate_limiter(request: Request, call_next):
    client_ip = request.client.host  # Identify user by IP (or API key later)
    current_time = time.time()  # Get current timestamp
    redis_key = f"rate_limit:{client_ip}"  # Unique key for each user

    # Remove outdated requests (older than WINDOW_SIZE)
    redis_client.zremrangebyscore(redis_key, 0, current_time - WINDOW_SIZE)

    # Count valid requests within the window
    request_count = redis_client.zcard(redis_key)

    if request_count >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # Add the current request timestamp to Redis
    redis_client.zadd(redis_key, {current_time: current_time})

    # Set expiry slightly longer than WINDOW_SIZE to optimize memory usage
    redis_client.expire(redis_key, WINDOW_SIZE + 1)

    response = await call_next(request)
    return response
