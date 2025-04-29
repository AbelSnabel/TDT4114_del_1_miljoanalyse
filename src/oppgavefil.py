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



#legger kart-funksjonen her fordi veit ikke hvor den skal være atm
    """ m = folium.Map(location=[20, 0], zoom_start=2)
    m.add_child(folium.LatLngPopup())
    html_fil = "kart.html"
    m.save(html_fil)
    print("\nVerdenkart åpnes i firefox")
    print("Du MÅ kopiere LATITUDE og LONGITUDE og lim dem inn når du blir bedt om det\n")
    webbrowser.open(f"file://{os.path.abspath(html_fil)}")
    lat = float(input("Lim inn LATITUDE: "))
    lon = float(input("Lim inn LONGITUDE: "))
    location = geolocator.reverse((lat, lon))  """