# NICE CXone API Integration Project

## Overview
This repository contains a modular Python project for integrating with the **NICE CXone APIs**, including features for authentication, tenant configuration discovery, and sending conversation transcripts.

More APIs would be added and presently its just a starter pack where you can spin up your authentication framework and call basic APIs

The project is structured for clarity and maintainability, separating authentication, API communication, and execution logic across distinct packages.

***

## Project Structure

```
src/
│
├── auth/
│   ├── __init__.py
│   ├── auth.py            # Handles authentication, token refresh, and tenant discovery
│   └── config.py          # (Excluded from repo) Contains secure credentials
│
├── digital_engagement/
│   ├── __init__.py
│   └── send_transcript.py # Implements the transcript API for sending conversation details
│
├── miscellaneous/
│   ├── __init__.py
│   └── main.py            # Entry point that fetches the value of the environment
├── admin/
│   ├── init/
│   │   └── start_script.py  # Script to start interaction by prompting user input details
├── realtime_data/
│   ├── init/
│   │   └── skill_activity.py  # Script for health check of a skill

```

Each subfolder has an `__init__.py` to ensure it’s recognized as a valid Python package.

***

## Prerequisites

- Python 3.8+  
- Git  
- A NICE CXone developer account and tenant credentials  
- Dependencies:
  ```bash
  pip install requests
  ```

***

## Getting Access to the CXone API

Before running this project, you must register your application with NICE CXone to obtain your client credentials (`client_id`, `client_secret`, etc.).

Follow the official guide on the NICE CXone Developer Portal:  
[Getting Started with CXone Mpower APIs](https://developer.niceincontact.com/Documentation/GettingStarted)

This page walks you through:
- Understanding **single-tenant** vs. **multi-tenant** app setups  
- Registering your application with NICE  
- Receiving your **client ID** and **client secret**  
- Setting up standard **OAuth2.0** authentication for back-end apps  
- Obtaining access and refresh tokens for API calls  

**Pro tip:** NICE typically takes around **2–3 business days** to approve your app registration and send credentials.

***

## Setting Up `config.py`

The `config.py` file is used to store sensitive credentials (client ID, secret, and tenant) **locally** and is intentionally **excluded** from version control using `.gitignore`.

### 1. File Location

Create the file inside:
```
src/auth/config.py
```

### 2. File Contents Example

```python
CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
USERNAME = "your_username_here"
PASSWORD = "your_password_here"
TENANT_ID = "your_tenant_id_here"
TOKEN_URL = "your_auth_token_url"
```

Alternatively, if you prefer environment variables (recommended for deployment):

```python
import os

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TENANT_ID = os.getenv("TENANT_ID")
TOKEN_URL = os.getenv("TOKEN_URL")
```

***

## Running the Script

This is an Example
From your project’s **root directory**, execute:

```bash
python -m src.digital_engagenment.send_transcript
```

This will:
1. Authenticate with CXone and retrieve an access token  
2. Discover tenant configuration details  
3. Prompt for `contact_id` and `email` input  
4. Request the transcript via the CXone DFO API  

***

## Example Output

```
Access Token: eyJhbGc...
Tenant Configuration Details:
API Endpoint: https://api-au1.niceincontact.com
Auth Endpoint: https://au1.nice-incontact.com
Domain: niceincontact.com
Area: au1
Cluster: A32

Enter contact ID: 682956606682323
Enter recipient email: samrat.som@nice.com
Transcript API response: {'status_code': 202, 'message': 'Accepted'}
```

***

## Sample `.gitignore`

```
# Exclude sensitive configs
src/auth/config.py

# Python cache and virtual env files
__pycache__/
*.pyc
*.pyo
venv/
.env/
.venv/
```

This prevents local credentials from ever being committed or pushed to GitHub.

***

## Key Features

- **Secure Authentication** using OAuth2.0 tokens  
- **Tenant Configuration Retrieval** for endpoint discovery  
- **Transcript API Integration** for sending contact details via CXone  
- Modular, extensible design for expanding CXone API functionality  

***

## Security Recommendations

- Never store production credentials in plain text.  
- Use `.gitignore` to exclude sensitive files.  
- For CI/CD pipelines, use environment variables or GitHub Secrets.  
- Validate `id_tokens` if using OIDC login flows.  
- Allow time drift tolerance when validating tokens (recommended ±5 minutes).  

***

## References

- Developer documentation: [Getting Started with CXone Mpower](https://developer.niceincontact.com/Documentation/GettingStarted)  
- OAuth2.0 and OpenID Connect specifications  
- CXone API Discovery endpoint:  
  ```
  https://cxone.niceincontact.com/.well-known/cxone-configuration?tenantId={tenantId}
  ```

***

This README follows best practices for Python API integration projects. It ensures clear onboarding steps, secure configuration handling, and proper documentation for NICE CXone tenant developers.