
This Python utility allows you to remotely start a **NICE inContact** script using authenticated API calls. It authenticates using OAuth credentials, retrieves tenant configuration, and executes scripts through the inContact API.

***

## Overview

This method starts a script identified by its **scriptId**.  
Currently, this only supports **channel-related scripts** such as Email, Phone, and Chat. You cannot start **Generic** or **API** scripts using this method.  
Support for those types will be added in a later release.

A **skillId** is required to run the script. The **skill’s media type** must match the **media type of the script** for it to run successfully.

You can also send **up to 20 separate values** into the script using the `Parameters` field, separated by the `|` symbol. These will be automatically assigned as ascending parameters named **P1, P2, P3, …** for access within NICE inContact Studio.

***

## Features

- OAuth-based authentication with NICE inContact API  
- Script initiation through skill binding  
- Support for up to 20 runtime parameters  
- JSON response handling and error reporting  
- User input-driven execution for flexible testing or integration  

***

## Requirements

- **Python:** 3.7 or newer  
- **Libraries:**  
  - `requests`

- **Project structure:**
  ```
  src/
  ├── auth/
  │   ├── auth.py          # Implements get_auth_token() and get_tenant_configuration()
  │   └── config.py        # Stores credentials and tenant configuration
  └── start_script.py      # Main script runner
  ```

***

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install requests
   ```

2. **Configure authentication parameters** in `src/auth/config.py`:
   ```python
   CLIENT_ID = "<your_client_id>"
   CLIENT_SECRET = "<your_client_secret>"
   USERNAME = "<your_username>"
   PASSWORD = "<your_password>"
   TOKEN_URL = "https://api-{region}.incontact.com/InContactAuthorizationServer/Token"
   TENANT_ID = "<your_tenant_id>"
   ```

3. **Ensure `src/auth/auth.py` includes:**
   - `get_auth_token(client_id, client_secret, username, password, token_url)`
   - `get_tenant_configuration(tenant_id)`

***

## Usage

Run the script from your project root:
```bash
python src/start_script.py
```

You will be prompted for:
- Skill ID  
- Script Path  
- Record ID  
- Phone Number  
- Agent  

### Example session
```
Enter Skill ID: 12345
Enter The Script Path: /AgentScripts/Welcome
Enter recordId: abc-789
Enter phoneNumber: 5551234567
Enter agent: JohnDoe
```

Expected output on success:
```
Access Token: eyJhbGciOiJIUzI1...
Script Started: {'status': 'success', 'instanceId': 'c123-456-xyz'}
```

***

## Error Handling

- If authentication or API execution fails, an exception with the status code and error message is printed.  
- The script attempts to parse JSON responses; if none exist, it displays status and text output.

***

## Customization

You can modify the user prompts or extend the `Parameters` payload to send additional context (e.g., customer IDs, campaign data).  
The API currently supports up to **20 parameters**, accessible within NICE inContact Studio as **P1–P20**.

***

Would you like me to add a section showing a sample JSON response structure from the NICE inContact API?