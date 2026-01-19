"""
Environment Configuration Module

This module loads environment variables from a .env file and
exposes critical configuration values for the application.

Specifically:
    - GEMINI_API_KEY: API key for Google Gemini LLM.

Usage:
    from cred import GEMINI_API_KEY
"""

import os
from dotenv import load_dotenv

# -------------------------------
# Load environment variables from .env file
# -------------------------------
load_dotenv()

# -------------------------------
# Read Gemini API key from environment
# -------------------------------
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

# -------------------------------
# Validate API key existence
# -------------------------------
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY not found in .env file")
