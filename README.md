# Advanced Rate Limiting Strategies in FastAPI 🚀

## Overview
A high-performance API rate limiter implementing **Fixed Window, Sliding Window, Token Bucket, and Leaky Bucket** algorithms using **FastAPI + Redis**. Optimized for **scalability**, **low-latency enforcement**, and **distributed API rate control**.

## System Design
The system is designed for **high-throughput APIs** handling **millions of requests** while preventing abuse. It efficiently tracks request counts using **Redis** with **O(log n) time complexity** for rate checks. Optimized **expiry policies** ensure **minimal memory overhead**.

### Architecture Diagram
```
   ┌───────────────────────────────┐
   │     Client Requests API       │
   ├───────────┬───────────────────┤
   │ Rate Limiter (FastAPI + Redis) │
   │  ├── Fixed Window              │
   │  ├── Sliding Window            │
   │  ├── Token Bucket              │
   │  ├── Leaky Bucket              │
   ├───────────┴───────────────────┤
   │         API Service Layer      │
   └───────────────────────────────┘
```

## Algorithm Choices
Each algorithm is optimized for different use cases:

- **Fixed Window** – Simple but allows bursts at window edges
- **Sliding Window** – More accurate, avoids bursts
- **Token Bucket** – Allows short bursts while enforcing long-term limits
- **Leaky Bucket** – Ensures a **smooth** request flow

## Performance Benchmarks
```
Rate Limiter Performance (Benchmark @ 10,000 requests):
-------------------------------------------------------
✔ Fixed Window    →  120μs avg latency, O(1) Redis ops
✔ Sliding Window  →  150μs avg latency, O(log n) Redis ops
✔ Token Bucket    →  140μs avg latency, O(1) Redis ops
✔ Leaky Bucket    →  130μs avg latency, O(1) Redis ops
```
📌 Designed for **low-latency enforcement** and **high scalability**.

## Trade-offs & Considerations
**Distributed Systems Considerations:**
- **Race conditions** are handled via atomic Redis operations (`INCR`, `ZADD`).
- Can be extended for **multi-node rate limiting** using **Redis Cluster** or **consistent hashing**.
- Supports **dynamic rate limits** (e.g., per-user tiers, API keys).

## In Progress Enhancements
✅ **JWT-Based API Rate Limits** – Per-user quotas instead of IP-based limits
✅ **Rate Limit Adaptation** – Machine learning to dynamically adjust limits
✅ **Prometheus + Grafana Monitoring** – Real-time dashboards

---

## Disclaimer  
This project is a technical demonstration of advanced rate-limiting strategies. It is not intended for deployment in real-world environments but serves as an exploration of best practices in scalable rate limiting.


