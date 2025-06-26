from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).resolve().parents[2] / "config" / ".env"
load_dotenv(dotenv_path=env_path)