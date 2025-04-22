def prediktiv_analyse():
    import pandas as pd
    from prophet import Prophet
    from prophet.plot import plot_plotly, plot_components_plotly
    import matplotlib.pyplot as plt

    #laster inn data fra df, må velge en by
    df = pd.read_csv(r'data\lokasjonsdata.csv') 
    byer = df.columns[1:]
    df = df[[df.columns[0],byer[-1+int(input(f"(tall 1-{len(byer)}){list(byer)}"))]]] 
    df.columns = ['ds', 'y']  

    #skriver dato-kolonnen til rett format
    df['ds'] = pd.to_datetime(df['ds'])

    #initialiserer prophet modellen, med årlig sesongvariasjon
    modell = Prophet(yearly_seasonality=True,weekly_seasonality=False,daily_seasonality=True)

    #lag en modell til de historiske dataene
    modell.fit(df)

    antall_år = 2

    #lager en dataframe for prediksjonen
    predikasjon = modell.make_future_dataframe(freq='D', periods=365*antall_år)

    #bruker modellen for å finne de forutsette verdiene
    forecast = modell.predict(predikasjon)


    #resten er plotting
    figur1 = modell.plot(forecast)
    figur2 = modell.plot_components(forecast)

    plot_plotly(modell, forecast)
    plot_components_plotly(modell, forecast)

    plt.legend()
    plt.show()