import logging


class MyLogger:

    logging.basicConfig(level=logging.INFO,
                        # filename=LOGS_FILE_NAME,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S',
                        encoding='UTF-8')
    logger = logging.getLogger("mylogger")

    # logger.info("Инфо сообщение")

