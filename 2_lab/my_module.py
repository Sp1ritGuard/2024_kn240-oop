import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(filename="module.log", encoding='utf-8')
std_handler = logging.StreamHandler()


format = logging.Formatter("%(name)s:%(filename)s:%(levelname)s::::===%(message)s ===")
file_handler.setFormatter(format)

std_format = logging.Formatter("%(name)s:^^^%(message)s^^^")
std_handler.setFormatter(std_format)

logger.addHandler(file_handler)
logger.addHandler(std_handler)

logger.setLevel(level = logging.WARNING)

logger.warning("Логи з модуля!")

logger.info("Інфо з модуля")

logger.error("Помилка з модуля")