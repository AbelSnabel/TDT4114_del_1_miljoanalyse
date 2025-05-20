#plotter dataene med plotly, og returnerer en figur
def plot_data(by, df):

    import pandas as pd
    import plotly.express as px

    city_data = df[f'{by}']

    fig = px.line(city_data, 
                x=city_data.index, 
                y=city_data.values, 
                labels={'x': 'datoer', 'y': 'solstråling(kwh/m^2)'}, 
    )
    return fig