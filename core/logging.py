"""App-wide logging setup + a request-scoped logger helper.

Kept intentionally simple (stdlib logging, structured-ish single-line
format) so it works the same locally and on any of the recommended
hosts (Render/Railway/PythonAnywhere) without extra dependencies.
"""
import logging
import sys


def configure_logging(level="INFO"):
    root = logging.getLogger()
    if root.handlers:
        # Avoid duplicate handlers on reload (Flask debug mode reimports this).
        return root

    root.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s :: %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
    )
    root.addHandler(handler)
    return root


def get_logger(name):
    return logging.getLogger(name)
