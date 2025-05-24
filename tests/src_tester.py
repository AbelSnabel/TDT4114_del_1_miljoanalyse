import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(project_root, 'src'))

import unittest
import pandas as pd
import plotly.graph_objects as go

from plot import plot_data
from statistikk import statistikk
from hent_lagre import hent
from prediktiv_analyse import prediktiv_analyse


class TestPlotData(unittest.TestCase):
    def setUp(self):
        self.dates = pd.date_range(start="2025-01-01", periods=3)
        self.df = pd.DataFrame({"Oslo": [4.2, 6.9, 42.0]}, index=self.dates)

    def testFigur(self):
        fig = plot_data("Oslo", self.df)
        self.assertIsInstance(fig, go.Figure)

    def testFigurData(self):
        fig = plot_data("Oslo", self.df)
        y_values = fig.data[0].y
        expected = [4.2, 6.9, 42.0]
        self.assertEqual(list(y_values), expected)

    def testIngenData(self):
        with self.assertRaises(KeyError):
            plot_data("Bergen", self.df)

class TestStatistikk(unittest.TestCase):
    def setUp(self):
        self.dates = pd.date_range("2025-01-01", periods=5)
        self.data = [10, 12, 14, 16, 18]
        self.df = pd.DataFrame({"Oslo": self.data}, index=self.dates)

    def testFigur(self):
        fig = statistikk("Oslo", self.df)
        self.assertIsInstance(fig, go.Figure)

class TestPrediktivAnalyse(unittest.TestCase):
    def setUp(self):
        # Lager et lite datasett med dato og verdi
        self.df = pd.DataFrame({
            'ds': pd.date_range('2024-01-01', periods=10, freq='D'),
            'y': range(10)
        })

    def testFigur(self):
        fig = prediktiv_analyse(1, self.df.copy())
        self.assertIsInstance(fig, go.Figure)

    def testFeilInput(self):
        df = self.df.copy()
        df.loc[0, 'y'] = 'not_a_number'
        fig = prediktiv_analyse(1, df)
        self.assertIsInstance(fig, go.Figure)


class TestHentLagre(unittest.TestCase):
    def setUp(self):
        self.lat = 60.0
        self.long = 10.0
        self.starttid = "20250101"
        self.sluttid = "20250131"
        self.csv_fil = os.path.join(project_root, 'data', 'lokasjonsdata.csv')

    def testHentCSV(self):
        hent(self.lat, self.long, self.starttid, self.sluttid,self.csv_fil)
        self.assertTrue(os.path.exists(self.csv_fil))

    def tearDown(self):
        if os.path.exists(self.csv_fil):
            os.remove(self.csv_fil)


if __name__ == "__main__":
    unittest.main()