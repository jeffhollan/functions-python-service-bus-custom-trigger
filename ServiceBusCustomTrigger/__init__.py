import logging
import time

import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s')
    logging.info(msg.get_body().decode('utf-8'))
    logging.info('sleeping....')
    time.sleep(900)
    logging.info('completing')
    logging.info(msg.get_body().decode('utf-8'))
