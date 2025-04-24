def statistikk(by, df_1):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.express as px

    #leser data fra csv-fil
    df = df_1
    data = df[by]

    average = np.mean(data)
    std_dev = np.std(data)
    stdev_max = average + std_dev
    stdev_min = average - std_dev
    fig1 = px.line(data, title=f"Statistikk for {by}", labels={'value': 'Antall', 'index': 'Tid'})
    fig1.add_hline(y=average, line_color='red', annotation_text="Gjennomsnitt", annotation_position="top left")
    fig1.add_hline(y=stdev_max, line_color='green', annotation_text="Stdev max", annotation_position="top left")
    fig1.add_hline(y=stdev_min, line_color='blue', annotation_text="Stdev min", annotation_position="top left")
    fig1.update_layout(xaxis_title="Tid", yaxis_title="Antall")
    return fig1