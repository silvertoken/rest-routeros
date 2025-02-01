
from .RestAdapter.adapter import RestAdapter


class RestRouterOS:
    # Initialize the class with port 8443 and default SSL
    def __init__(self, hostname, username, password,
                 port='8443', verify=True, capath=None):
        self.adapter = RestAdapter(hostname, username,
                                   password, port, verify, capath)

    def identity(self):
        return self.adapter.get("system/identity")

    def routerboard(self):
        return self.adapter.get("system/routerboard")

    def health(self):
        return self.adapter.get("system/health")

    def resource(self):
        return self.adapter.get("system/resource")
