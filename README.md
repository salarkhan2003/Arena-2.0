# Arena 2.0

Premium mobile-ready 3D browser arena game built with FastAPI and Three.js.

## Local Run

```bash
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/`.

## Deploy

This project includes `vercel.json` for Vercel Python serverless deployment. Explicit builds and routes are configured to bypass Vercel's zero-config assumptions.

