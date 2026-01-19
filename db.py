"""
Database utility module for the AI Government Service Agent.

This module provides helper functions to load government service data
from a local JSON database file. The data is consumed by MCP tools
(Aadhaar, PAN, Passport, Grievances) to simulate backend lookups.

Database File:
- database/gov_database.json

Intended Usage:
- Internal use by MCP tool functions
- Read-only access to mock government records

Author: Pushap Tyagi
"""

import json

# ---------------------------------------------------------------------
# Database Configuration
# ---------------------------------------------------------------------

DB_PATH = "gov_database.json"


def load_db() -> dict:
    """
    Summary:
        Loads and returns the government services database from a local
        JSON file. This function is intended to be used internally by
        MCP tool implementations for read-only data access.

    Args:
        None

    Returns:
        dict:
            A parsed dictionary containing mock government records,
            including Aadhaar, PAN, Passport, and grievance data.

    Raises:
        FileNotFoundError:
            If the database file does not exist at the specified path.
        json.JSONDecodeError:
            If the database file contains invalid or malformed JSON.
    """
    with open(DB_PATH, "r", encoding="utf-8") as file:
        return json.load(file)