def lagre_data(lon_min,lon_max,lat_min,lat_max,starttid,sluttid,type,location,csv_fil,df_tidligere):  
    import requests
    import pandas as pd
    import os

    #API-kall
    url = f"https://power.larc.nasa.gov/api/temporal/{type}/regional?parameters=ALLSKY_SFC_SW_DWN&community=SB&longitude-min={lon_min}&longitude-max={lon_max}&latitude-min={lat_min}&latitude-max={lat_max}&start={starttid}&end={sluttid}&format=JSON"

    response = requests.get(url)
    if response.status_code == 422:
        print("Ugyldig forespørsel.")
    elif response.status_code == 429:
        print("For mange forespørsler. Prøv igjen senere.")
    elif response.status_code == 200:
        print(f"Success")

    #Henter ut data fra responsen
    data = response.json()["features"][0]["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]

    #Konverter data til en pandas DF
    df = pd.DataFrame(list(data.values()), index=pd.to_datetime(list(data.keys())), columns=[location[0].split(",")[0]])

    #sjekk etter csv fil, og oppdater eller lagre ny data 
    if os.path.exists(csv_fil):
        df_sammensatt = pd.concat([df_tidligere, df], axis=1)
    else:
        df_sammensatt = df

    #lagre df til csv
    df_sammensatt.to_csv(csv_fil, sep="\t", encoding="utf-8")
    print(f"Data lagret i {csv_fil}")