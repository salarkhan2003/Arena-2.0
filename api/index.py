import os
import sys
from pathlib import Path

# Add project root to sys.path to allow importing main.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from main import app
