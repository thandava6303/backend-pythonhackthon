source venv/bin/activate
pip install "pydantic[email]"
uvicorn app.main:app --host 0.0.0.0 --port 8000
