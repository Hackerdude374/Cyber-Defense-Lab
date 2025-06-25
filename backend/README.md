**Cyber Defense Lab Backend** is a Flask API server responsible for handling authentication, role management, and logging Red/Blue team actions. It communicates with a PostgreSQL database and returns secure JSON responses to the frontend.

#### Technologies:

- **Flask** for the web framework
- **SQLAlchemy** as ORM for PostgreSQL
- **JWT Extended** for secure token auth
- **Docker** for containerization

#### Endpoints:
- `POST /register` – Registers a user with `username`, `password`, and `role` ("red" or "blue")
- `POST /login` – Authenticates a user and returns a JWT
- (Coming Soon) `POST /attack`, `POST /log-defense`, `GET /threats`

#### Running Locally:
```bash
cd backend
pip install -r requirements.txt
flask run
```

In Docker:
```bash
docker-compose up --build
```

Ensure PostgreSQL is reachable using the `DATABASE_URL` environment variable.

---
