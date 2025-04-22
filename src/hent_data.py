def hent_data():
    from geopy.geocoders import Nominatim
    import os
    import pandas as pd
    from datetime import datetime
    from lagre_data import lagre_data
    import requests
    geolocator = Nominatim(user_agent="miljøanalyse_abel")
    location = geolocator.geocode(input("location: "))
    print(location.address)
    print((location.latitude, location.longitude))

    #api-parametre
    starttid = "20050101"  # YYYYMMDD
    sluttid = datetime.today().strftime("%Y%m%d")  # YYYYMMDD
    type = "daily"
    lon = location.longitude
    lat = location.latitude

    # CSV-fil for samlet data
    csv_fil = r"data\lokasjonsdata.csv"
    if os.path.exists(csv_fil):
        df_tidligere = pd.read_csv(csv_fil, index_col=0, sep=",", parse_dates=True)
    else: 
        df_tidligere = pd.DataFrame()
    if location[0].split(",")[0] in list(df_tidligere):
        print(f"Data for {location[0].split(',')[0]} finnes allerede i {csv_fil}.")
        return
    else:
        lagre_data(lon,lat,starttid,sluttid,type,location,csv_fil,df_tidligere)