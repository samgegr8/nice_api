from src.auth.auth import get_auth_token, get_tenant_configuration
import src.auth.config as config 
import requests


def change_status(api_endpoint, access_token, caseId):
    url = f"{api_endpoint}/dfo/3.0/contacts/{caseId}/status"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    body = {
        "status": "closed"
    }

    response = requests.put(url, headers=headers, json=body)

    # If response body is not empty, try parse JSON else return status code and text
    if response.status_code in (200, 201, 202,204):
        try:
            return response.json()
        except ValueError:
            # No JSON in response, just return status and text
            return {"status_code": response.status_code, "message": response.text}
    else:
        raise Exception(f"Failed to change Status: {response.status_code} {response.text}")


if __name__ == "__main__":
    try:
        token = get_auth_token(config.CLIENT_ID, config.CLIENT_SECRET, config.USERNAME, config.PASSWORD,config.TOKEN_URL)
        print("Access Token:", token)

        tenant_info = get_tenant_configuration(config.TENANT_ID)
        api_endpoint = tenant_info.get("api_endpoint")

        # Take inputs from user
        caseId = input("Enter Case ID To Change Status: ").strip()

        result = change_status(api_endpoint, token, caseId)
        print("Transcript API response:", result)

    except Exception as e:
        print("Error:", e)
