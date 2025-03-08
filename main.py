import redis # Import redis client to interact with redis server
import time # To manage time-based rate limiting
import jwt
from fastapi import FastAPI, Request, HTTPException # FastAPI components help with API handling
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from routes import router  # Import the router from routes.py

# Initialize FastAPI application and call routes
app = FastAPI()
app.include_router(router)

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

SECRET_KEY = "use your own secret"
security = HTTPBearer()

# Rate limiting settings by user role
RATE_LIMITS = {
    "free": (100, 600),  # 100 requests per 10 min
    "premium": (500, 600),  # 500 requests per 10 min
}

def decode_jwt(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms="HS256")
    except  jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    

@app.middleware("http")
async def jwt_based_rate_limiter(request: Request, call_next):
    auth= request.headers.get("Auhorization")
    
    if not auth:
        return JSONResponse(status_code=401, content={"detail": "Missing token"})
    

    token = auth.split("Bearer ")[-1]
    user_data = decode_jwt(token)  # Extract user info
    user_id = user_data["user_id"]
    user_role = user_data.get("role", "free")  # Default to free

    max_requests, window_size = RATE_LIMITS.get(user_role, RATE_LIMITS["free"])
    redis_key = f"rate_limit:{user_id}"

    # Sliding window logic
    current_time = time.time()
    redis_client.zremrangebyscore(redis_key, 0, current_time - window_size)
    request_count = redis_client.zcard(redis_key)

    if request_count >= max_requests:
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

    redis_client.zadd(redis_key, {current_time: current_time})
    redis_client.expire(redis_key, window_size + 1)

    return await call_next(request)