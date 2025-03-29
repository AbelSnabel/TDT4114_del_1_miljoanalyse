def statistikk():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #leser data fra csv-fil
    df = pd.read_csv(r'data\lokasjonsdata.csv')

    def stat(by):
        data = df[by]
        average = np.mean(data)
        std_dev = np.std(data)
        stdev_max = average + std_dev
        stdev_min = average - std_dev
        print(f"Gjennomsnitt for lokasjon 1: {average:.3f}")
        print(f"Standardavvik for lokasjon 1: {std_dev:.3f}")
        plt.plot(data)
        plt.axhline(average, color='red', linewidth=1, label='Gjennomsnitt')
        plt.axhline(stdev_max, color='purple', linestyle='dashed', linewidth=1, label='Standardavvik')
        plt.axhline(stdev_min, color='purple', linestyle='dashed', linewidth=1)

    print("Lagrede byer", df.columns.tolist())
    byer = input("Skriv inn kommaseparerte byer: ")
    for by in byer.split(","):
        stat(by)

    plt.legend()
    plt.show()