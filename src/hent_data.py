def hent_data():
    from geopy.geocoders import Nominatim
    import os
    import pandas as pd
    from lagre_data import lagre_data
    import requests
    geolocator = Nominatim(user_agent="miljøanalyse_abel")
    location = geolocator.geocode(input("location: "))
    print(location.address)
    print((location.latitude, location.longitude))

    #api-parametre
    starttid = "20050101"  # YYYYMMDD
    sluttid = "20060101"  # YYYYMMDD
    type = "daily"
    #vi trekker fra og legger til 1.01 fordi det minste området api-en kan ta er 2x2 breddegrader
    lon_min, lon_max = location.longitude - 1.01, location.longitude + 1.01
    lat_min, lat_max = location.latitude - 1.01, location.latitude + 1.01

    # CSV-fil for samlet data
    csv_fil = r"data\lokasjonsdata.csv"
    if os.path.exists(csv_fil):
        df_tidligere = pd.read_csv(csv_fil, index_col=0, sep="\t", parse_dates=True)
    else: 
        df_tidligere = pd.DataFrame()
    if location[0].split(",")[0] in list(df_tidligere):
        print(f"Data for {location[0].split(',')[0]} finnes allerede i {csv_fil}.")
        return
    else:
        lagre_data(lon_min,lon_max,lat_min,lat_max,starttid,sluttid,type,location,csv_fil,df_tidligere)
