def plot_data():
    #plot all eksisterende data.
    df_sammensatt.columns = [col.split("_")[0] for col in df_sammensatt.columns]
    df_sammensatt.plot(figsize=(10, 5))
    plt.xlabel("Dag")
    plt.ylabel("Solinnstråling (W/m^2)")
    plt.title("Sammenligning av solinnstråling over tid")
    plt.legend(df_sammensatt.columns)
    plt.show()