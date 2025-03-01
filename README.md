# 🚀 FastAPI Rate-Limited Public API

## 🔥 Why This Project?
This API is built to **handle high-traffic workloads while preventing abuse**, using **rate limiting and Redis caching**. 

Security is a major focus for me, and I’m especially interested in companies like **1Password, Okta, and Cloudflare**—leaders in authentication, secure access control, and API protection. This project is a **practical demonstration of my ability to design and implement security-first APIs**, enforcing **strict rate limits, blocking abuse, and ensuring scalable request management**—essential in modern cloud-based authentication and API security systems.

## ✅ What's Already Built
### **Scalability & Performance**
- ⚡ **FastAPI-powered API** – High-performance, lightweight framework.
- 🚀 **Redis-based fixed window rate limiting** – Efficiently tracks API usage.
- 🛠 **Middleware-based enforcement** – Rate limits are applied dynamically at request processing.

### **Security & Access Control**
- 🔄 **IP-based rate limits** – Prevents excessive requests from a single client.
- ⚠️ **HTTP 429 enforcement** – Users exceeding limits receive proper error responses.
- 🛡️ **Prevention against API abuse** – First layer of defense against spammy requests.

---

## 🚀 What's Coming Next
- 🔐 **JWT Authentication** – Secure endpoints and track users.
- ⚖️ **Role-Based Rate Limits** – Different quotas for anonymous, authenticated, and premium users.
- 📝 **User Registration & Database Integration** – Store users in a database.
- 📊 **Admin Dashboard** – Monitor request trends & blocked users.
- 🛡️ **Advanced Security** – Blacklist abusive clients, implement IP whitelisting.
- 📦 **Dockerized Deployment** – Containerized version for easy cloud deployment.
- ☁️ **Cloud Scaling Examples** – AWS Lambda, Kubernetes, Serverless API.
- ✅ **Cloud deployable** – Can be deployed to AWS/GCP/Azure with additional setup.
- ✅ **Easily extendable** – Structured for adding authentication, advanced rate limiting, and more.

---

## 🛠 Installation & Setup

### **Prerequisites**
- **Python 3.8+**
- **Redis Server**
- **FastAPI & Uvicorn**

### **Installation Steps**

#### **1️⃣ Clone the repository**
```sh
git clone https://github.com/yourusername/fastapi-rate-limit-api.git
cd fastapi-rate-limit-api
```

#### **2️⃣ Install dependencies**
```sh
pip install -r requirements.txt
```

#### **3️⃣ Run Redis server** (if not already running)
```sh
redis-server
```

#### **4️⃣ Start the FastAPI server**
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### **5️⃣ Test the API**
- Open: `http://127.0.0.1:8000/docs`
- Use tools like **Postman** or `curl` to send requests.

---

## 🔗 API Endpoints So Far

| **Method** | **Endpoint** | **Description** |
|-----------|------------|----------------|
| **GET** | `/public` | Open access, no authentication required |
| **GET** | `/rate-limited` | Enforced rate-limited endpoint |

---

## 🎯 Why I Love This Work
Security-first API design is a must-have in our current landscape, where secure authentication, rate limiting, and access control are critical. Whatever services I build, I want people to feel safe using them.

This project allows me to design, build, and optimize backend security systems by demonstrating:
- ✅ **Rate limiting & API security best practices** – Protecting against abuse and DDoS.
- ✅ **Scalable security architecture** – Foundation for authentication and access control.
- ✅ **Middleware processing expertise** – High-performance request handling.
- ✅ **Cloud-native API development** – Built for easy expansion and security integrations.

---

