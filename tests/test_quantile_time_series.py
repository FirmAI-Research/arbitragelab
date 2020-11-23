# Copyright 2019, Hudson and Thames Quantitative Research
# All rights reserved
# Read more: https://github.com/hudson-and-thames/mlfinlab/blob/master/LICENSE.txt

"""
Tests AUTO ARIMA prediction functions.
"""

import unittest
import os
import numpy as np
import pandas as pd

from arbitragelab.other_approaches import QuantileTimeSeriesTradingStrategy


class TestQuantileTimeSeries(unittest.TestCase):
    """
    Tests Auto ARIMA predictions.
    """

    def setUp(self):
        """
        Set the file path for the tick data csv
        """
        spread_data = [-0.2, 0.3, 0.5, 1.7, 1.0, 0.0, -5, -6, -9, -7, -2, 1, 1.1, 1.2, 1.3, 1.4, 1.8, 3, 0.2]
        forecast_data = [-0.21, 0.35, 0.55, 1.6, 1.0, 0.0, -5.5, -6, -9.1, -7.1, -2.1, 1, 1.1, 1.3, 1.5, 1.9, 2, 0.2]
        self.spred_series = pd.Series(spread_data)
        self.forecast_series = pd.Series(forecast_data)

    def test_time_series_strategy(self):
        """
        Tests get_trend_order function.
        """
        trading_strategy = QuantileTimeSeriesTradingStrategy()
        trading_strategy.fit_thresholds(self.spred_series)
        trading_strategy.plot_thresholds()

