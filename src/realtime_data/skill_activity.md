# Skill Activity API Script

This script retrieves real-time agent activity data for a given **Skill ID** from the NICE CXone (inContact) platform using the **Skill Activity API**. It authenticates using a bearer token and displays a summary of agent state counts including idle, ACW, available, and working statuses.

***

## Prerequisites

Before using this script, ensure you have:

- Python 3.8 or later installed  
- Access to the NICE CXone (inContact) API  
- API credentials defined in `src/auth/config.py`, including:
  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `USERNAME`
  - `PASSWORD`
  - `TOKEN_URL`
  - `TENANT_ID`

***

## File Structure

```
project-root/
│
├── src/
│   ├── auth/
│   │   ├── auth.py
│   │   └── config.py
│
├── skill_activity.py
└── skill_activity.md
```

***

## How It Works

1. **Authentication:**  
   The script calls `get_auth_token()` from `src.auth.auth` to obtain an OAuth Bearer token.

2. **Tenant Configuration:**  
   It retrieves the tenant’s API endpoint using `get_tenant_configuration()`.

3. **Skill Activity Request:**  
   The script sends a GET request to the following endpoint:  
   ```
   /incontactapi/services/v33.0/skills/{skillID}/activity
   ```
   It fetches fields such as:
   - `agentsACW`
   - `agentsIdle`
   - `agentsLoggedIn`
   - `agentsAvailable`
   - `agentsUnavailable`
   - `contactsActive`
   - `agentsWorking`

4. **Response Handling:**  
   If the response is successful (HTTP 200–202), it parses and returns the JSON output.

5. **Display Results:**  
   The returned data is printed to the console in a readable key-value format.

***

## Example Usage

Run the script from the terminal:

```bash
python skill_activity.py
```

You will be prompted to enter a **Skill ID**.  
Example input and output:

```
Enter Skill ID: 12345

agentsACW: 0
agentsIdle: 2
agentsLoggedIn: 5
agentsAvailable: 3
agentsUnavailable: 2
contactsActive: 1
agentsWorking: 4
```

***

## Error Handling

If the API request fails, an exception will be raised displaying the **HTTP status code** and **response message**.

Example:
```
Failed to Call Skill Activity: 401 Unauthorized
```

***

## Dependencies

This script uses the following Python libraries:
- `requests`

Install dependencies via pip if not already installed:

```bash
pip install requests
```

***

## Notes

- The `get_auth_token()` and `get_tenant_configuration()` helper functions are expected to be defined in `src/auth/auth.py`.
- Ensure your credentials are valid and your network allows outbound HTTPS requests to the CXone API endpoint.
