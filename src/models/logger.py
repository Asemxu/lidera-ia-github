import logging

class SingletonLogger:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SingletonLogger, cls).__new__(cls, *args, **kwargs)
            cls._initialize_logger(cls.instance)
        return cls.instance

    @staticmethod
    def _initialize_logger(instance):
        instance.logger = logging.getLogger("logger")
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        instance.logger.addHandler(handler)
        instance.logger.setLevel(logging.INFO)

    @classmethod
    def get_logger(cls):
        if not cls.instance:
            cls.instance = SingletonLogger()
        return cls.instance.logger

logger = SingletonLogger.get_logger()
