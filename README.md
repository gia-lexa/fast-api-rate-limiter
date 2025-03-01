# 🚀 FastAPI Rate-Limited Public API

## 🔥 Why This Project?
This API is built to **handle high-traffic workloads while preventing abuse**, using **rate limiting, JWT authentication, and Redis caching**. If you're building or maintaining a public API, you need **security, scalability, and performance**—this project delivers just that.

## ✅ What's Already Built
### **Scalability & Performance**
- ⚡ **FastAPI-powered API** – Lightweight and high-performance.
- 🚀 **Redis-based rate limiting** – Efficiently controls API traffic.
- 🧠 **Smart middleware** – Applies rate limits dynamically at request processing.

### **Security & Authentication**
- 🔐 **JWT authentication** – Secure token-based access.
- ⚖️ **Role-based rate limits** – Different quotas for anonymous, authenticated, and premium users.
- 🔄 **OAuth2 password flow** – Industry-standard authentication.

### **Cloud & DevOps Readiness**
- 📦 **Dockerized setup** – Ready for deployment.
- ☁️ **Redis-backed request tracking** – Scalable for distributed environments.
- 🌍 **Deployable on AWS/GCP/Azure** – With **NGINX/Trafik reverse proxying**.

---

## 🚀 What's Coming Next
- **📝 User Registration & Database Integration** – Store users in a database.
- **📊 Admin Dashboard** – Monitor request trends & blocked users.
- **🛡️ Advanced Security** – Blacklist abusive clients, implement IP whitelisting.
- **☁️ Cloud Deployment Examples** – AWS Lambda, Kubernetes, Serverless API.

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

## 🔗 API Endpoints

| **Method** | **Endpoint** | **Description** |
|-----------|------------|----------------|
| **GET** | `/public` | Open access, no authentication required |
| **GET** | `/protected` | Requires JWT authentication |
| **GET** | `/rate-limited` | Enforced rate-limited endpoint |
| **POST** | `/token` | Generate JWT token |

---

## 🔑 Coming Soon: Authentication & Role-Based Rate Limiting

Once JWT authentication is implemented, users will:
1. **Login to receive a JWT token** (`/token`).
2. **Use the token** in API requests (`Authorization: Bearer <token>`).
3. **Be assigned rate limits based on role**:
   - 🔹 **Anonymous users:** **100 requests per 10 minutes**.
   - 🔹 **Authenticated users:** **500 requests per 10 minutes**.
   - 🔹 **Premium users:** **1000 requests per 10 minutes**.

---
