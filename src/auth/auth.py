import requests
from requests.auth import HTTPBasicAuth

def get_auth_token(client_id, client_secret, username, password,url):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }

    auth = HTTPBasicAuth(client_id, client_secret)
    response = requests.post(url=url, headers=headers, data=data, auth=auth)
    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("access_token")
    else:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")

def get_tenant_configuration(tenant_id):
    url = f"https://cxone.niceincontact.com/.well-known/cxone-configuration?tenantId={tenant_id}"
    response = requests.get(url)
    if response.status_code == 200:
        config = response.json()
        # Extract the required information
        api_endpoint = config.get("api_endpoint")
        domain = config.get("domain")
        area = config.get("area")
        cluster = config.get("cluster")
        auth_endpoint = config.get("auth_endpoint")
        return {
            "api_endpoint": api_endpoint,
            "domain": domain,
            "area": area,
            "cluster": cluster,
            "auth_endpoint": auth_endpoint
        }
    else:
        raise Exception(f"Failed to get tenant configuration: {response.status_code} {response.text}")
