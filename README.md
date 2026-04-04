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
