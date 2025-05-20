def prediktiv_analyse(antall_år, df):
    import pandas as pd
    from prophet import Prophet
    from prophet.plot import plot_plotly

    #laster inn data fra df, må velge en by
    df.columns = ['ds', 'y']

    df.loc[:, 'y'] = pd.to_numeric(df['y'], errors='coerce')
    df.loc[:, 'ds'] = pd.to_datetime(df['ds'])

    #initialiserer prophet modellen, med årlig og daglig sesongvariasjon
    modell = Prophet(yearly_seasonality=True,weekly_seasonality=False,daily_seasonality=True)

    #lag en modell til de historiske dataene
    modell.fit(df)

    #lager en dataframe for prediksjonen
    predikasjon = modell.make_future_dataframe(freq='D', periods=365*antall_år)

    #bruker modellen for å finne de forutsette verdiene
    forecast = modell.predict(predikasjon)

    fig = plot_plotly(modell, forecast)
    
    return fig