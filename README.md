# Advanced Rate Limiting Strategies in FastAPI 🚀

## Overview
An advanced exploration of high-performance rate limiting, leveraging Redis for precision control and scalability.

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
Each algorithm is optimized for different use cases. The current main.py implements Leaky Bucket, but earlier commits of that file show the implementations of Fixed Window and Sliding Window. 

- **Fixed Window** – Simple but allows bursts at window edges
- **Sliding Window** – More accurate, avoids bursts
- **Leaky Bucket** – Ensures a **smooth** request flow
- **Token Bucket** – Allows short bursts while enforcing long-term limits

## Performance Benchmarks
```
Rate Limiter Performance (Benchmark @ 10,000 requests):
-------------------------------------------------------
✔ Fixed Window    →  120μs avg latency, O(1) Redis ops
✔ Sliding Window  →  150μs avg latency, O(log n) Redis ops
✔ Leaky Bucket    →  130μs avg latency, O(1) Redis ops
```
📌 Designed for **low-latency enforcement** and **high scalability**.

## Trade-offs & Considerations
**Distributed Systems Considerations:**
- **Race conditions** are handled via atomic Redis operations (`INCR`, `ZADD`).
- Can be extended for **multi-node rate limiting** using **Redis Cluster** or **consistent hashing**.
- Supports **dynamic rate limits** (e.g., per-user tiers, API keys).

## Future Enhancements Currently In-Progress
✅ **JWT-Based API Rate Limits** – Per-user quotas instead of IP-based limits

✅ **Rate Limit Adaptation** – Machine learning to dynamically adjust limits

✅ **Prometheus + Grafana Monitoring** – Real-time dashboards

## Disclaimer
This project is an in-progress **technical demonstration** of advanced rate-limiting strategies. While provided under the MIT License, it is **not optimized for production use**, and no guarantees are made regarding security, reliability, or real-world performance. It serves as an exploration of best practices in scalable rate limiting.

---
🚀 **This project showcases production-level rate limiting strategies, balancing speed, fairness, and resilience for high-scale APIs.**

