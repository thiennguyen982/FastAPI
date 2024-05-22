import logging

# Create logger with specific name and level
def create_logger(logger_name: str, filename: str, level: str):
    logger = logging.getLogger(logger_name)
    log_levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    if level.upper() not in log_levels:
        raise ValueError(f"Invalid log level: {level}. Valid levels are {', '.join(log_levels.keys())}")
    
    logger.setLevel(log_levels[level.upper()])
    handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger