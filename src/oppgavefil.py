import requests
import matplotlib.pyplot as plt
import pandas as pd
import os
from geopy.geocoders import Nominatim

while True:
    print("1: Hent data")
    print("2: Plot data")
    print("3: Statistikk")
    print("4: Avslutt")
    svar = input()
    if svar == "1":
        hent_data()
    elif svar == "2":
        plot_data()
    elif svar == "3":
        statistikk()
    elif svar == "4":
        break