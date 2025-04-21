def lagre_data(lon,lat,starttid,sluttid,type,location,csv_fil,df_tidligere):  
    import requests
    import pandas as pd
    import os

    #SIDEN vi har data for solinnstrålig, er det ikke urimelig å anta at verdien er lik i området rundt punktet
    #derfor er det tilstrekkelig å hente data for ett punkt i området.

    url = f"https://power.larc.nasa.gov/api/temporal/{type}/point?parameters=ALLSKY_SFC_SW_DWN&community=SB&longitude={lon}&latitude={lat}&start={starttid}&end={sluttid}&format=JSON"

    response = requests.get(url)
    if response.status_code == 422:
        print("Ugyldig forespørsel.")
    elif response.status_code == 429:
        print("For mange forespørsler. Prøv igjen senere.")
    elif response.status_code == 200:
        print(f"Success")

    print(response.status_code)
    print(response.json())

    response_json = response.json()

    #Henter ut data fra responsen
    data = response_json["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]

    #Konverter data til en pandas DF
    df = pd.DataFrame(list(data.values()), index=pd.to_datetime(list(data.keys())), columns=[location[0].split(",")[0]])

    if df.isna().any().any() != 0:
        df.interpolate(method='time', inplace=True)
        print("data inneholder NaN verdier")
    else:
        print("dataen inneholder ikke NaN verdier")

    if os.path.exists(csv_fil):
        df_sammensatt = pd.concat([df_tidligere, df], axis=1)
    else:
        df_sammensatt = df

    #lagre df til csv
    df_sammensatt.to_csv(csv_fil, sep=",", encoding="utf-8")
    print(f"Data lagret i {csv_fil}")
