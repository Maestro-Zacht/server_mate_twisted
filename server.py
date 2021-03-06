import os
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

PORT = int(os.environ.get('PORT', 12345))
USERS = []


class Server(WebSocket):
    def handleConnected(self):
        print(f'{self.address} connesso')
        USERS.append(self)

    def handleClose(self):
        print(f'{self.address} disconnesso')
        USERS.remove(self)

    def handleMessage(self):
        if self.data != 'ping555':
            for u in USERS:
                if u != self:
                    u.sendMessage(self.data)
        else:
            self.sendMessage("pong555")


if __name__ == "__main__":
    server = SimpleWebSocketServer('', PORT, Server)
    server.serveforever()
