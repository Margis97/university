import json

import logger


class JsonUtils:
    @staticmethod
    def is_json(obj: str) -> bool:
        try:
            json.loads(obj)
        except json.JSONDecodeError as e:
            logger.MyLogger.logger.info("Некорректный JSON:", e)
            return False
        except TypeError as e:
            logger.MyLogger.logger.info("Передан некорректный тип:", e)
            return False
        return True
