**Cyber Defense Lab Frontend** is a Vite-powered React application that connects securely to the Flask backend to enable Red/Blue team user interactions.

#### Stack:
- **React (Vite)** for a fast SPA UI
- **Fetch API** to communicate with Flask
- **Role-based forms** for login/registration
- (Coming Soon) Secure dashboards, attack simulation UI

#### Components:
- `LoginForm.jsx`: Simple username/password login with JWT token storage
- `RegisterForm.jsx`: Allows user to choose team (red/blue) at registration

#### Running Locally:
```bash
cd frontend
npm install
npm run dev
```

In Docker:
```bash
docker-compose up --build
```

Make sure backend (`localhost:5000`) is up before using the frontend (`localhost:5173`).
