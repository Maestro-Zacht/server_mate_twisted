from twisted.internet import protocol, reactor
import os

PORT = int(os.environ.get('PORT', 12345))


class Server(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class ServerFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return Server()


if __name__ == '__main__':
    reactor.listenTCP(PORT, ServerFactory())
    reactor.run()
