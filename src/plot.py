import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    df = pd.read_csv(r'data\lokasjonsdata.csv', index_col=0, parse_dates=True)
    
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)
    
    plt.xlabel("datoer")
    plt.ylabel("solstråling(kwh/m^2)")
    plt.title("Graf over solstråling på lokasjonene")
    plt.legend()
    plt.grid()
    plt.show()