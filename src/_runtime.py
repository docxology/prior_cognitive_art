from __future__ import annotations

import logging
from pathlib import Path

try:
    from .project_paths import resolve_project_root
except ImportError:  # pragma: no cover — standalone load (no package context)
    from project_paths import resolve_project_root  # type: ignore[no-redef]


def project_root(caller: str = "src") -> Path:
    return resolve_project_root(caller)


def get_logger(module_name: str | None = None) -> logging.Logger:
    try:
        from infrastructure.core.logging.utils import get_logger as infra_get_logger

        return infra_get_logger(module_name or __name__)
    except ImportError:  # pragma: no cover
        logger = logging.getLogger(module_name or __name__)
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger


__all__ = [
    "get_logger",
    "project_root",
]
