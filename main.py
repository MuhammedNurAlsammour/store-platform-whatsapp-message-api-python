from utils.consumer import Consumer
from utils.config import Config
import json, constants.queue_names as queue_names
from utils.messager import Messager 
_config = Config()
_rabbit_mq_conf = _config.rabbit_mq_conf()

class Main():
    def __init__(self) -> None:
        self.queue_list = []
        self._consumer = Consumer(self.queue_list, config=_rabbit_mq_conf)
        self.messager = Messager()

    def run(self):
        try:
            self.queue_list = [
                {
                    "queue_name": queue_names.WP_MESSAGE,
                    "callback": self.wpMessage
                }
            ]

            self._consumer.set_queue_list(self.queue_list)
            self._consumer.consume()
        except Exception as e:
            print(e)
            self.run()

    def wpMessage(self, ch, method, properties, body):
        print(" [x] wpMessage Received...")

        data = json.loads(body)

        self.messager.send(data['phone'], data['message'], data['waitTime'])
        print(data)
        
def Run():
    if __name__ == '__main__':
        try:
            _main = Main()
            _main.run()
        except Exception as e:
            print(e)
            Run()

Run()