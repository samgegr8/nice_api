from src.auth.auth import get_auth_token, get_tenant_configuration
import src.auth.config as config 
import requests


def start_script(api_endpoint, access_token, scriptPath, skillID,recordId,phoneNumber,agent):
    url = f"{api_endpoint}/inContactAPI/services/v33.0/scripts/start?skillId={skillID}&scriptPath={scriptPath}&Parameters={recordId}|{phoneNumber}|{agent}|{skillID}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)

    # If response body is not empty, try parse JSON else return status code and text
    if response.status_code in (200, 201, 202):
        try:
            return response.json()
        except ValueError:
            # No JSON in response, just return status and text
            return {"status_code": response.status_code, "message": response.text}
    else:
        raise Exception(f"Failed to send transcript: {response.status_code} {response.text}")


if __name__ == "__main__":
    try:
        token = get_auth_token(config.CLIENT_ID, config.CLIENT_SECRET, config.USERNAME, config.PASSWORD,config.TOKEN_URL)
        print("Access Token:", token)

        tenant_info = get_tenant_configuration(config.TENANT_ID)
        api_endpoint = tenant_info.get("api_endpoint")

        # Take inputs from user
        skillID = input("Enter Skill ID: ").strip()
        scriptPath = input("Enter The Script Path: ").strip()
        recordId = input("Enter recordId: ").strip()
        phoneNumber = input("Enter phoneNumber: ").strip()
        agent = input("Enter agent: ").strip()

        result = start_script(api_endpoint, token, scriptPath, skillID, recordId,phoneNumber,agent)
        print("Script Started:", result)

    except Exception as e:
        print("Error:", e)
