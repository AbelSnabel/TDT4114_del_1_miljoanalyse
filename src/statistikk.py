def statistikk():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #leser data fra csv-fil
    df = pd.read_csv(r'data\lokasjonsdata.csv')

    print("Lagrede byer", df.columns.tolist())
    by1 = input("1")
    by2 = input("2")

    if by1 not in df.columns and by2 not in df.columns:
        print("kys")
        return
    elif by2 not in df.columns and by1 in df.columns:
        data1 = df[by1]
        average1 = np.mean(data1)
        std_dev1 = np.std(data1)
        stdev_1_max = average1 + std_dev1
        stdev_1_min = average1 - std_dev1
        print(f"Gjennomsnitt for lokasjon 1: {average1:.3f}")
        print(f"Standardavvik for lokasjon 1: {std_dev1:.3f}")
    elif by1 in df.columns and by2 in df.columns:
        data1 = df[by1]
        average1 = np.mean(data1)
        std_dev1 = np.std(data1)
        stdev_1_max = average1 + std_dev1
        stdev_1_min = average1 - std_dev1
        print(f"Gjennomsnitt for lokasjon 1: {average1:.3f}")
        print(f"Standardavvik for lokasjon 1: {std_dev1:.3f}")

        data2 = df[by2]
        average2 = np.mean(data2)
        std_dev2 = np.std(data2)
        stdev_2_max = average2 + std_dev2
        stdev_2_min = average2 - std_dev2
        print(f"Gjennomsnitt for lokasjon 2: {average2:.3f}")
        print(f"Standardavvik for lokasjon 2: {std_dev2:.3f}")
        


    plt.plot(data1)
    plt.plot(data2)
    plt.axhline(average1, color='red', linewidth=1, label='Gjennomsnitt')
    plt.axhline(stdev_1_max, color='purple', linestyle='dashed', linewidth=1, label='Standardavvik')
    plt.axhline(stdev_1_min, color='purple', linestyle='dashed', linewidth=1)
    plt.axhline(average2, color='red', linewidth=1, label='Gjennomsnitt')
    plt.axhline(stdev_2_max, color='purple', linestyle='dashed', linewidth=1, label='Standardavvik')
    plt.axhline(stdev_2_min, color='purple', linestyle='dashed', linewidth=1)

    plt.legend()
    plt.show()