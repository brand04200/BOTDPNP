import os
from pathlib import Path

from dotenv import load_dotenv

# Load a local .env file for development while still allowing Railway
# environment variables to take precedence in production.
load_dotenv(Path(__file__).with_name(".env"))

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError(
        "Environment variable TOKEN belum diatur. "
        "Tambahkan TOKEN di Railway Variables atau file .env lokal."
    )

