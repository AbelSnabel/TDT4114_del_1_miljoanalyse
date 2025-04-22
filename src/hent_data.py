def hent_data():
    import folium
    from geopy.geocoders import Nominatim
    import os
    import pandas as pd
    from lagre_data import lagre_data
    import webbrowser

    #Lager Folium-kart
    m = folium.Map(location=[20, 0], zoom_start=2)
    m.add_child(folium.LatLngPopup())
    html_fil = "kart.html"
    m.save(html_fil)

    print("\nVerdenkart åpnes i firefox")
    print("Du MÅ kopiere LATITUDE og LONGITUDE og lim dem inn når du blir bedt om det\n")

    webbrowser.open(f"file://{os.path.abspath(html_fil)}")

    valg = input("Velg 1 for å skrive longitude og latitude, velg 2 for å skrive inn en by :)").strip()

    geolocator = Nominatim(user_agent="miljøanalyse_abel")

    if valg == "1":

        lat = float(input("Lim inn LATITUDE: "))
        lon = float(input("Lim inn LONGITUDE: "))
        location = geolocator.reverse((lat, lon))
    elif valg == "2":
        by = input("Skriv inn navnet på byen: ").strip()
        location = geolocator.geocode(by)
        if not location:
            print("Stedet finne ikke :(")
            return
        lon, lat = location.longitude, location.latitude


    else:
        print("Ugyldig valg. Avslutter...")
        return

    if not location:
        print("Stedet finne ikke :(")
        return

    print("Valgt sted:", location.address)


    #API-parametre
    starttid = "20050101"
    sluttid = "20060101"
    type = "daily"
    #vi trekker fra og legger til 1.01 fordi det minste området api-en kan ta er 2x2 breddegrader
    lon = location.longitude
    lat = location.latitude

    #CSV-fil
    csv_fil = r"data\lokasjonsdata.csv"
    if os.path.exists(csv_fil):
        df_tidligere = pd.read_csv(csv_fil, index_col=0, sep=",", parse_dates=True)
    else:
        df_tidligere = pd.DataFrame()

    # Unngå å hente dobbelt data
    stedsnavn = location.address.split(",")[0]
    if stedsnavn in list(df_tidligere):
        print(f"Data for {stedsnavn} finnes allerede i {csv_fil}.")
        return
    else:
        lagre_data(lon,lat,starttid,sluttid,type,location,csv_fil,df_tidligere)
