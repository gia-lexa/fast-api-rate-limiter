import redis # Import redis client to interact with redis server
import time # To manage time-based rate limiting
from fastapi import FastAPI, Request, HTTPException # FastAPI components help with API handling

# Initialize FastAPI application
app = FastAPI()

# Connect to redis server
redis_client = redis.Redis(host="localhost", port=6379, db=0)

RATE_LIMIT = 100 # Max allowed requests per time window
Window = 600 # Time window in seconds (10 minutes)

# instantiate FastAPI decordator that intercepts all requests before they 
# reach route handlers, allowing modification of the request, eg
# auth, rate limitng,logging, etc
@app.middleware("http")
async def rate_limiter(request: Request, call_next):
  client_ip = request.client.host
  current_time = int(time.time() // WINDOW)
  key = f"rate_limit:{client_ip}:{current_time}"  # Generate a unique key for the IP and time window
  
  request_count = redis_client.incr(key)  # Increment request count in Redis for this key

  if request_count == 1:
        redis_client.expire(key, WINDOW)  # Set expiration time for the key to match the window duration

  if request_count > RATE_LIMIT:
        # If request count exceeds the limit, return a 429 Too Many Requests error
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
  
  # If within limit, process the request normally
  response = await call_next(request)
  return response