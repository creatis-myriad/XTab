# Fixes logger in Kaggle to show logs in notebook.
from .utils.log_utils import fix_logging_if_kaggle as __fix_logging_if_kaggle
from .version import __version__

__fix_logging_if_kaggle()
