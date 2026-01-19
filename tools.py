"""
MCP Tool Server for AI Government Service Agent.

This module defines MCP tools exposed via FastMCP for checking the
status of various Indian government services, including:

- Aadhaar
- PAN
- Passport
- Grievances

The tools fetch data from a mock/local database and are intended to be
invoked by an AI agent through the Model Context Protocol (MCP).

Dependencies:
- fastmcp
- db.load_db()

Author: Pushap Tyagi
"""

from fastmcp import FastMCP
from db import load_db

# ---------------------------------------------------------------------
# MCP Server Initialization
# ---------------------------------------------------------------------

mcp = FastMCP("AI-Government-Service-Agent")

# ---------------------------------------------------------------------
# AADHAAR TOOLS
# ---------------------------------------------------------------------


@mcp.tool()
def aadhaar_status_check(aadhaar_number: str) -> dict:
    """
    Summary:
        Fetches the status details associated with a given Aadhaar number
        from the local/mock database.

    Args:
        aadhaar_number (str): The 12-digit Aadhaar number provided
            by the citizen.

    Returns:
        dict:
            Aadhaar status details if the record exists,
            otherwise an error message indicating the Aadhaar
            record was not found.
    """
    db = load_db()
    return db["aadhaar"].get(
        aadhaar_number,
        {"error": "Aadhaar not found"},
    )


# ---------------------------------------------------------------------
# PAN TOOLS
# ---------------------------------------------------------------------


@mcp.tool()
def pan_status_check(pan_number: str) -> dict:
    """
    Summary:
        Retrieves the status information of a Permanent Account Number (PAN)
        from the local/mock database.

    Args:
        pan_number (str): The PAN number provided by the citizen.

    Returns:
        dict:
            PAN status details if the record exists,
            otherwise an error message indicating the PAN
            record was not found.
    """
    db = load_db()
    return db["pan"].get(
        pan_number,
        {"error": "PAN not found"},
    )


# ---------------------------------------------------------------------
# PASSPORT TOOLS
# ---------------------------------------------------------------------


@mcp.tool()
def passport_status_check(application_id: str) -> dict:
    """
    Summary:
        Retrieves the status of a passport application using
        the provided application ID.

    Args:
        application_id (str): The passport application reference ID.

    Returns:
        dict:
            Passport application status if the record exists,
            otherwise an error message indicating the application
            was not found.
    """
    db = load_db()
    return db["passport"].get(
        application_id,
        {"error": "Passport not found"},
    )


# ---------------------------------------------------------------------
# GRIEVANCE TOOLS
# ---------------------------------------------------------------------


@mcp.tool()
def grievance_status_check(grievance_id: str) -> dict:
    """
    Summary:
        Retrieves the current status of a registered grievance
        using its grievance reference ID.

    Args:
        grievance_id (str): The grievance reference identifier.

    Returns:
        dict:
            Grievance status details if the record exists,
            otherwise an error message indicating the grievance
            record was not found.
    """
    db = load_db()
    return db["grievances"].get(
        grievance_id,
        {"error": "Grievance not found"},
    )


# ---------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------

if __name__ == "__main__":
    """
    Start the MCP tool server using standard input/output (stdio)
    transport, allowing it to be invoked by external AI agents.
    """
    mcp.run(transport="stdio")
