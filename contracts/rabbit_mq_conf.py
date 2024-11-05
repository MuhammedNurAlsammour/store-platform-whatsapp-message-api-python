class RabbitMQConf:
    def __init__(self, host = 'localhost', port = 5672, username = 'guest', password = 'guest'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password