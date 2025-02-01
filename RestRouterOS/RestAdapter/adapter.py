import httpx
import ssl


class RestAdapter:
    # Initialize the adapter defaults on port 8443
    # with SSL and using httpx trust
    def __init__(self, hostname, api_user, api_pass,
                 port='8443', verify=True, capath=None):
        # Format the base REST url and port
        self.api_url = f"https://{hostname}:{port}/rest"
        # Use basic auth
        self.api_auth = httpx.BasicAuth(username=api_user, password=api_pass)
        # Check for trustred CA Path
        if capath is not None:
            self.api_client = httpx.Client(
                verify=ssl.create_default_context(capath=capath))
        else:
            self.api_client = httpx.Client(verify=verify)

    # Get calls to the REST API
    def get(self, endpoint):
        # Build url from endpoint path
        url = f"{self.api_url}/{endpoint}"
        response = self.api_client.get(url, auth=self.api_auth)

        # Raise an exception for bad status codes
        response.raise_for_status()
        return response.json()
