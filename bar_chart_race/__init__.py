from . import _pandas_accessor
from ._bar_chart_race import bar_chart_race
from ._utils import load_dataset, prepare_wide_data, prepare_long_data

__version__ = '0.2.0'
__all__ = [
    'bar_chart_race',
    'load_dataset',
    'prepare_wide_data',
    'prepare_long_data',
]
