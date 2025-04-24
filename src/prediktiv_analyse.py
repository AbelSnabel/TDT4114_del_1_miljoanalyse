def prediktiv_analyse(antall_år, by, df_1):
    import pandas as pd
    from prophet import Prophet
    from prophet.plot import plot_plotly, plot_components_plotly
    import matplotlib.pyplot as plt
    print(df_1.head())

    #laster inn data fra df, må velge en by
    df = df_1  # Explicitly create a copy
    df.columns = ['ds', 'y']

    df['y'] = pd.to_numeric(df['y'], errors='coerce')

    #skriver dato-kolonnen til rett format
    df['ds'] = pd.to_datetime(df['ds'])

    #initialiserer prophet modellen, med årlig og daglig sesongvariasjon
    modell = Prophet(yearly_seasonality=True,weekly_seasonality=False,daily_seasonality=True)

    #lag en modell til de historiske dataene
    modell.fit(df)

    #lager en dataframe for prediksjonen
    predikasjon = modell.make_future_dataframe(freq='D', periods=365*antall_år)

    #bruker modellen for å finne de forutsette verdiene
    forecast = modell.predict(predikasjon)

    return modell, forecast