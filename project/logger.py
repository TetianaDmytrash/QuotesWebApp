import logging

class NoSQLFilter(logging.Filter):
    def filter(self, record):
        # Вернуть False для записей, которые вы хотите исключить из обработки
        return not record.getMessage().startswith("sqlalchemy.engine.Engine")

# Настройка логгера
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Настройка обработчика для записи в файл
file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.WARNING)

# Определение формата записей в логе
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Примеры логирования
#logger.warning("WARNING")
#logger.error("ERROR")
#logger.critical("CRITICAL")