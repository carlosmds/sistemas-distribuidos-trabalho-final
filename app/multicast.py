from Pyro4 import expose, Proxy
from helpers.utils import get_servers

@expose
class MultiCast:
    def __init__(self):
        self._messages = []
        servers = get_servers()
        print("Número de servidores replica no name server:", (len(list(servers.keys()))))

    def echo(self, message):
        self._messages.append(message)
        servers = get_servers()

        if servers:
            for server in list(servers.keys()):
                conn = Proxy(servers[server])
                conn.overwrite_messages(self._messages)
        
        return "Message received: {}".format(message)

    @property
    def get_messages(self):
        return self._messages

    def overwrite_messages(self, messages):
        self._messages = messages
