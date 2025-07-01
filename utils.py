"""utils"""

import logging
import structlog


def configure_logging(logformat, level):
    """Configure logging for a Python program using the structlog framework.

    Args:
      logformat: The format of the log messages. Can be `json` or `text`.
      level: The log level. Can be `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`.

    Returns:
      A logging configuration object.
    """

    processorrender = ""
    if logformat == "json":
        processorrender = structlog.processors.JSONRenderer()
    else:
        processorrender = structlog.dev.ConsoleRenderer()

    loglevel = logging.getLevelName(level)
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            processorrender,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(loglevel),
        cache_logger_on_first_use=True,
    )

    logger = structlog.getLogger()

    return logger
