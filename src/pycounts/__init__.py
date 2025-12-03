from importlib.metadata import version
from .pycounts import count_words

__all__ = ["count_words", "__version__"]
__version__ = version("pycounts")
