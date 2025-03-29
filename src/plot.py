import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    df = pd.read_csv(r'data\lokasjonsdata.csv')
    df.reset_index(drop=False, inplace=True)
    
    for by in list(df.columns):
        plt.plot(df[by])

    print(list(df.columns))
    plt.legend()
    plt.show()