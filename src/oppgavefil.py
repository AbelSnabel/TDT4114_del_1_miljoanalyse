import matplotlib.pyplot as plt
from hent_data import hent_data
from plot import plot_data
from statistikk import statistikk
from prediktiv_analyse import prediktiv_analyse

while True:
    print("1: Hent data")
    print("2: Plot data")
    print("3: Statistikk")
    print("4: Prediktiv Analyse")
    print("5: Avslutt")
    svar = input()
    if svar == "1":
        hent_data()
    elif svar == "2":
        plot_data()
    elif svar == "3":
        statistikk()
    elif svar == "4":
        prediktiv_analyse()
    elif svar == "5":
        break