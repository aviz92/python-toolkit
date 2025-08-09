import logging
from dataclasses import is_dataclass
from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum
from pathlib import Path

logger = logging.getLogger(__name__)


def default_serialize(obj: object) -> object:
    if isinstance(obj, type):
        return obj.__name__
    if is_dataclass(obj) and not isinstance(obj, type):
        return obj.__dict__
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, tuple):
        return list(obj)
    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, Path):
        return str(obj)
    logger.error(f'Object is not serializable: {obj}')
    raise TypeError(f"Type {type(obj)} not serializable")
