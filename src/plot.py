import pandas as pd
import matplotlib.pyplot as plt

def plot_data(csv_fil):
    """
    Plotter data for to spesifikke steder fra en CSV-fil.
    
    Args:
        csv_fil (str): Stien til CSV-filen.
        sted1 (str): Navnet på det første stedet.
        sted2 (str): Navnet på det andre stedet.
    """

    sted1, sted2 = input("sted1,sted2")
    # Les data fra CSV-filen
    df = pd.read_csv(csv_fil, index_col=0, sep="\t", parse_dates=True)
    # Gjør kolonnenavn små bokstaver for konsistens
    df.columns = [col.lower() for col in df.columns]
    sted1 = sted1.lower()
    sted2 = sted2.lower()

    # Sjekk om stedene finnes i dataene
    if sted1 not in df.columns or sted2 not in df.columns:
        print(f"En eller begge stedene ({sted1}, {sted2}) finnes ikke i dataene.")
        print("Tilgjengelige steder:", df.columns.tolist())
        return

    # Filtrer data for de to stedene
    df_to_plot = df[[sted1, sted2]]

    # Plot data
    df_to_plot.plot(figsize=(10, 5))
    plt.xlabel("Dag")
    plt.ylabel("Solinnstråling (W/m^2)")
    plt.title(f"Sammenligning av solinnstråling: {sted1} vs {sted2}")
    plt.legend([sted1, sted2])
    plt.show()