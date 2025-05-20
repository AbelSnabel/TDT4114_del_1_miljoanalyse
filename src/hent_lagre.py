def hent(lat, long, starttid, sluttid, df_tidligere):
    import requests
    from geopy.geocoders import Nominatim
    import pandas as pd
    import os

    geolocator = Nominatim(user_agent="miljøanalyse_abel")
    location = geolocator.reverse((lat, long))
    if location is None:
        print("Ingen lokasjon funnet.")
        return
    address = location.raw.get('address', {})
    stedsnavn = (
        address.get('city') or address.get('town') or address.get('village') or address.get('municipality') 
        or location.address.split(",")[-1].strip()
    )
    #legger til koordinater i stedsnanvet, gjorde det lettere å håndtere flere trykk på samme sted
    stedsnavn = f"{stedsnavn} ({lat:.1f},{long:.1f})"
    csv_fil = r'../data/lokasjonsdata.csv'

    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=SB&longitude={long}&latitude={lat}&start={starttid}&end={sluttid}&format=JSON"

    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    print(f"Response URL: {response.url}")

    if response.status_code != 200:
        return

    data = response.json()["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]


    df_new = pd.DataFrame({
        "Date": list(data.keys()),
        stedsnavn: list(data.values())
    })
    df_new["Date"] = pd.to_datetime(df_new["Date"])

    #setter negative verdier til None, opplever ofte at det er negative verdier, 
    #vanligvis starter det en måned før dags dato, nasa sin feil
    df_new.loc[df_new[stedsnavn] < 0, stedsnavn] = None

    #helt jævlig måte å gjøre dette på
    if os.path.exists(csv_fil) and os.path.getsize(csv_fil) > 0:
        df_old = pd.read_csv(csv_fil, parse_dates=["Date"])
    else:
        df_old = pd.DataFrame(columns=["Date"])

    df_old.set_index("Date", inplace=True)
    df_new.set_index("Date", inplace=True)

    #bro jeg hater dataframes
    if stedsnavn in df_old.columns:
        df_merged = df_old
    else:
        df_merged = df_old.join(df_new, how="outer")

    df_merged = df_merged.sort_index().reset_index()
    df_merged.to_csv(csv_fil, index=False)
    print(f"Data lagret i {csv_fil}.")