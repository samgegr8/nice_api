from src.auth.auth import get_auth_token, get_tenant_configuration
import src.auth.config as config  # use alias here

if __name__ == "__main__":
    try:
        token = get_auth_token(
            config.CLIENT_ID,
            config.CLIENT_SECRET,
            config.USERNAME,
            config.PASSWORD
        )
        print("Access Token:", token)
        
        tenant_info = get_tenant_configuration(config.TENANT_ID)
        
        print("Tenant Configuration Details:")
        print("API Endpoint:", tenant_info.get("api_endpoint"))
        print("Auth Endpoint:", tenant_info.get("auth_endpoint"))
        print("Domain:", tenant_info.get("domain"))
        print("Area:", tenant_info.get("area"))
        print("Cluster:", tenant_info.get("cluster"))

    except Exception as e:
        print("Error:", e)
