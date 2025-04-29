def hent_data(input,starttid,sluttid):
    import folium
    from geopy.geocoders import Nominatim
    import os
    import pandas as pd
    from datetime import datetime
    from lagre_data import lagre_data
    import webbrowser


    valg = input

    geolocator = Nominatim(user_agent="miljøanalyse_abel")

    location = geolocator.geocode(by)
    if not location:
        print("Stedet finne ikke :(")
        return
    lon, lat = location.longitude, location.latitude


    #API-parametre
    starttid = "starttid"
    sluttid = "slutttid"
    type = "daily"
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