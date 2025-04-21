#beregne gjennomsnitt av hver dag, helst for 5 år. Bruke en metode for å lage forecast for neste år.
def forecast(by):
    import pandas as pd
    from prophet import Prophet
    from prophet.plot import plot_plotly, plot_components_plotly
    import matplotlib.pyplot as plt

    # Load the data
    df =  pd.read_csv(r'data/lokasjonsdata.csv')  # Les inn dataen
    df = df.rename(columns={"dato": "ds", "verdi": "y"})  # Omdøp kolonner

    # Print the first few rows of the dataframe
    print(df.head())

    # Initialize the Prophet model
    m = Prophet()
    
    # Fit the model to the data
    m.fit(df)

    # Create a dataframe for future predictions
    future = m.make_future_dataframe(periods=365)
    
    # Make predictions
    forecast = m.predict(future)
    
    # Plot the forecast
    fig1 = m.plot(forecast)
    fig2 = m.plot_components(forecast)

    plot_plotly(m, forecast)
    plot_components_plotly(m, forecast)

    print("Lagrede byer", df.columns.tolist())
    byer = input("Skriv inn kommaseparerte byer: ")
    for by in byer.split(","):
        forecast(df[by])

    plt.legend()
    plt.show()





