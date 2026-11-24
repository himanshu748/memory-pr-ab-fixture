# payments-api demo service

Toy service used to demonstrate agent memory drift.

- Runtime: Python 3.12
- Data store: MongoDB 8 (`src/db.py` uses `pymongo`)

Run locally:

```bash
docker compose up --build
curl localhost:8080/db   # 503 until DATABASE_URL is set in .env
```
