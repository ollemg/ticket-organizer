from loguru import logger

format_logger="<green>{time}</green> | <level>{level}</level> | <blue>{name}:{function}:{line}</blue> - <level>{message}</level>"

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format=format_logger,
)

logger.add(
    "ticket-organizer.log", 
    rotation="10 KB",
    level="DEBUG",
    format=format_logger,
)