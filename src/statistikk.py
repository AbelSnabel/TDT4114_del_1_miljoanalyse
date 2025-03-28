def statistikk():
    
    def average(data):
        return np.mean(data)

    def std_dev(data):
        return np.std(data)

    def median(data):
        return np.median(data)

    std_dev_max = average(df) + std_dev(df)
    std_dev_min = average(df) - std_dev(df)   

    print(f"Gjennomsnitt: {average(df[0]):.3f}")
    print(f"Standardavvik: {std_dev(df[0]):.3f}")
    print(f"Median: {median(df[0]):.3f}")

    plt.plot(range(0,len(data.values())),data.values())
    plt.axhline(average(df[0]), color='red', linestyle='dashed', linewidth=1, label='Gjennomsnitt')
    plt.axhline(median(df[0]), color='green', linestyle='dashed', linewidth=1, label='Median')
    plt.axhline(std_dev_max, color='purple', linestyle='dashed', linewidth=1, label='Standardavvik')
    plt.axhline(std_dev_min, color='purple', linestyle='dashed', linewidth=1)
    plt.legend()
    plt.show()