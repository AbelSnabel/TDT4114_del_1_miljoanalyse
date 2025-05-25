import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

# mappe plasering
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import av funksjon
from hent_lagre import hent


class TestHent(unittest.TestCase):
    @patch("hent_lagre.requests.get")
    @patch("hent_lagre.Nominatim")
    @patch("hent_lagre.os.path.exists", return_value=False)
    @patch("hent_lagre.os.path.getsize", return_value=0)
    @patch("hent_lagre.pd.DataFrame.to_csv")
    def test_hent_normal_case(
        self, fake_to_csv, fake_getsize, fake_exists, fake_nominatim, fake_requests_get
    ):
        # Lager fake geolocation
        fake_location = MagicMock()
        fake_location.raw = {"address": {"city": "Oslo"}}
        fake_location.address = "Oslo, Norway"
        fake_nominatim.return_value.reverse.return_value = fake_location

        # Lager fake NASA API respons
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            "properties": {
                "parameter": {
                    "ALLSKY_SFC_SW_DWN": {
                        "2025-01-01": 10.0,
                        "2025-01-02": -5.0
                    }
                }
            }
        }
        fake_requests_get.return_value = fake_response

        hent(59.91, 10.75, "20250101", "20250102", pd.DataFrame())

        fake_to_csv.assert_called_once() 
        df_saved = fake_to_csv.call_args[0][0] 

    @patch("hent_lagre.requests.get")
    @patch("hent_lagre.Nominatim")
    def test_hent_lokasjon_ikke_funnet(self, fake_nominatim, fake_requests_get):
        fake_nominatim.return_value.reverse.return_value = None
        result = hent(0, 0, "20250101", "20250102", pd.DataFrame())
        self.assertIsNone(result)

    @patch("hent_lagre.requests.get")
    @patch("hent_lagre.Nominatim")
    def test_hent_feil_statuskode(self, fake_nominatim, fake_requests_get):
        fake_location = MagicMock()
        fake_location.raw = {"address": {"city": "Oslo"}}
        fake_location.address = "Oslo, Norway"
        fake_nominatim.return_value.reverse.return_value = fake_location

        fake_requests_get.return_value.status_code = 500
        result = hent(59.91, 10.75, "20250101", "20250102", pd.DataFrame())
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()