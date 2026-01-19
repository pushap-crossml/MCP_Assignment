# MCP_Assignment

A Model Context Protocol (MCP) server implementation that provides access to government ID information (Aadhaar, PAN Card, Passport) and grievance status checking through a JSON database, integrated with Google's Gemini LLM API.

## 📋 Overview

This project implements an MCP server that stores and retrieves government identification data and grievance information. Users can interact with the system using natural language prompts through the Gemini LLM, which fetches information from the MCP server.

## 🚀 Features

- **Government ID Storage**: Store and retrieve Aadhaar, PAN Card, and Passport information
- **Grievance Tracking**: Check status of grievances/complaints
- **MCP Server**: Standards-compliant Model Context Protocol server
- **Gemini LLM Integration**: Natural language queries using Google's Gemini API
- **JSON Database**: Lightweight JSON-based data storage

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pushap-crossml/MCP_Assignment.git
   cd MCP_ASSIGNMENT
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```


## 🎯 Usage

### Starting the MCP Server

```bash
python agent.py
```

### Running the Client

```bash
python client.py
```

### Example Queries

The system supports natural language queries like:

- "Show me Aadhaar details for number 1234-5678-9012"
- "Get PAN card information for ABCDE1234F"
- "Check status of grievance GR001"
- "Find passport details for A12345678"

## 🔧 Component Details

### `agent.py`
MCP server implementation that handles tool registration and request processing.

### `client.py`
Client interface that connects to the MCP server and sends queries via Gemini LLM.

### `db.py`
Database operations handler for reading/writing to `gov_database.json`.

### `tools.py`
Defines MCP tools/functions for different operations:
- `get_aadhaar_details`
- `get_pancard_details`
- `get_passport_details`
- `check_grievance_status`

### `cred.py`
Manages API credentials and authentication.

## 🔐 Security Considerations

- Store sensitive API keys in `.env` file
- Add `.env` to `.gitignore` (already included)
- Never commit real government ID data
- Use sample/mock data for testing

## 📦 Dependencies

Key dependencies include:
- `google-generativeai` - Gemini LLM API
- `python-dotenv` - Environment variable management
- MCP-related libraries for server implementation

See `requirements.txt` for complete list.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

