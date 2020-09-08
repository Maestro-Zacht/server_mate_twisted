import os

from twisted.internet import reactor, endpoints, protocol

PORT = int(os.environ.get('PORT', 12345))


class Server(protocol.Protocol):

    def __init__(self, collegati):
        self.collegati = collegati

    def dataReceived(self, data):
        self.transport.write(data)

    def connectionMade(self):
        print('New connection')


class ServerFactory(protocol.ServerFactory):

    def __init__(self):
        self.collegati = {}

    def buildProtocol(self, addr):
        return Server(self.collegati)


if __name__ == '__main__':
    print(f'ascolto sulla porta {PORT}')
    endpoint = endpoints.TCP4ServerEndpoint(reactor, PORT)
    endpoint.listen(ServerFactory())
    reactor.run()
