from twisted.internet import reactor, endpoints, protocol


class Client(protocol.Protocol):
    def __init__(self):
        reactor.callInThread(self.send_data)

    def dataReceived(self, data):
        print(data.decode('utf-8'))

    def send_data(self):
        while True:
            self.transport.write(input('> ').encode('utf-8'))


class ClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return Client()


if __name__ == '__main__':
    endpoint = endpoints.TCP4ClientEndpoint(
        reactor, 'ws://servergarecatta.herokuapps.com/', 20307)
    endpoint.connect(ClientFactory())
    reactor.run()
