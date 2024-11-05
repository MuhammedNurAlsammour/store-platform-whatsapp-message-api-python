import pika
from contracts.rabbit_mq_conf import RabbitMQConf

class Consumer():
    def __init__(self, queue_list:list, config: RabbitMQConf):
        self.queue_list:list = queue_list
        self.host = config.host
        self.port = config.port
        self.user = config.username
        self.password = config.password

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.host,
                                    self.port,
                                    credentials=
                                    pika.PlainCredentials(self.user, self.password)))
        
        self.channel = self.connection.channel()

    def set_queue_list(self, queue_list):
        self.queue_list = queue_list

    def queue_declare(self):
        for queue in self.queue_list:
            self.channel.queue_declare(queue=queue["queue_name"])
            self.channel.basic_consume(queue=queue["queue_name"], on_message_callback=queue["callback"], auto_ack=True)

    def consume(self):
        self.queue_declare()

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()