# Github-Cloud-Connector

A simple backend connector service built using **Python + FastAPI** that integrates with the **GitHub REST API**.  
It supports authentication using:

- **Personal Access Token (PAT)** (mandatory)
- **OAuth 2.0 Device Flow** (bonus)

This connector exposes REST endpoints to perform GitHub actions such as fetching repositories, listing issues, and creating issues.

---

## Features

### Authentication
- PAT Authentication (via `.env`)
- OAuth 2.0 Device Flow (optional/bonus)

### GitHub API Actions
- Fetch repositories for a user
- Fetch repositories for authenticated user (including private repos)
- List issues from a repository
- Create an issue in a repository

### Interface
- REST API using FastAPI
- Swagger UI available at `/docs`

---

## Tech Stack
- Python 3
- FastAPI
- Uvicorn
- Requests
- GitHub REST API

---

## Project Structure

# Github-Cloud-Connector

A simple backend connector service built using **Python + FastAPI** that integrates with the **GitHub REST API**.  
It supports authentication using:

- **Personal Access Token (PAT)** (mandatory)
- **OAuth 2.0 Device Flow** (bonus)

This connector exposes REST endpoints to perform GitHub actions such as fetching repositories, listing issues, and creating issues.

---

## Features

### Authentication
- PAT Authentication (via `.env`)
- OAuth 2.0 Device Flow (optional/bonus)

### GitHub API Actions
- Fetch repositories for a user
- Fetch repositories for authenticated user (including private repos)
- List issues from a repository
- Create an issue in a repository

### Interface
- REST API using FastAPI
- Swagger UI available at `/docs`

---

## Tech Stack
- Python 3
- FastAPI
- Uvicorn
- Requests
- GitHub REST API

---

## Project Structure
github-connector/
│── app/
│ │── main.py
│ │── config.py
│ │
│ ├── routes/
│ │ ├── github_routes.py
│ │ ├── auth_routes.py
│ │ 
│ │
│ ├── services/
│ │ ├── github_service.py
│ │ ├── oauth_service.py
│ │ 
│ │
│ ├── schemas/
│ │ ├── issue_schema.py
│ │ └── pr_schema.py
│ │
│ └── utils/
│ ├── github_exceptions.py
│ └── github_response_handler.py
│
│
│
│── .env
│── .gitignore
│── requirements.txt
│
│── README.md


github-connector/
│── app/
│ │── main.py
│ │── config.py
│ │
│ ├── routes/
│ │ ├── github_routes.py
│ │ ├── auth_routes.py
│ │ └── device_auth_routes.py
│ │
│ ├── services/
│ │ ├── github_service.py
│ │ ├── oauth_service.py
│ │ └── device_flow_service.py
│ │
│ ├── schemas/
│ │ ├── issue_schema.py
│ │ └── pr_schema.py
│ │
│ └── utils/
│ ├── github_exceptions.py
│ └── github_response_handler.py
│
│── tests/
│ └── test_health.py
│
│── .env
│── .gitignore
│── requirements.txt
│── requirements-dev.txt
│── README.md



## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/Project-Manager1-Tech/Github-Cloud-Connector.git
cd Github-Cloud-Connector

2. Create Virtual Environment (Recommended)
python -m venv venv

3. Activate:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Create a .env file in the root directory.
GITHUB_TOKEN=ghp_your_personal_access_token

6. Run :
 python -m uvicorn app.main:app --reload


