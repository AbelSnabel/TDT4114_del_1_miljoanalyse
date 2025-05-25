# Data Directory

Denne mappen inneholder datasett som brukes i prosjektet. Datasettet lagres som en CSV-fil og oppdateres dynamisk basert på brukerens interaksjoner med applikasjonen.

## Innhold
- **`lokasjonsdata.csv`**:
  - En CSV-fil som inneholder miljødata for ulike geografiske lokasjoner og tidsintervaller.
  - Kolonner:
    - `Date`: Dato for datapunktet.
    - Andre kolonner representerer data for spesifikke byer eller lokasjoner (f.eks. temperatur, luftkvalitet, etc.).
  - Filen oppdateres automatisk når brukeren henter nye data via applikasjonen.

## Hvordan dataene brukes
- **Datainnhenting**:
  - Når brukeren klikker på kartet og velger et tidsintervall, hentes data fra eksterne kilder og lagres i `lokasjonsdata.csv`.
  - Hvis filen ikke eksisterer, opprettes en ny fil med en `Date`-kolonne.

- **Databehandling**:
  - Dataene leses av funksjoner i `src/`-modulene for videre behandling, visualisering og analyse.
  - Eksempel: Funksjonen `hent` i `hent_lagre.py` oppdaterer filen med nye data.

- **Analyse og visualisering**:
  - Dataene brukes i applikasjonen (`app.py`) og i Jupyter Notebooks (`notebooks/`) for å lage grafer, statistiske analyser og prediktive modeller.

## Viktig
- **Filstruktur**:
  - `lokasjonsdata.csv` må ligge i `data/`-mappen for at applikasjonen skal fungere korrekt.
  - Sørg for at mappen `data/` eksisterer før du kjører applikasjonen.

- **Automatisk opprettelse**:
  - Hvis `lokasjonsdata.csv` ikke eksisterer, oppretter applikasjonen en ny fil med følgende kode:
    ```python
    if not os.path.exists(csv_path):
        df = pd.DataFrame(columns=['Date'])
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        df.to_csv(csv_path, index=True)
    ```

## Eksempel på CSV-struktur
```csv
Date,Oslo,Bergen,Trondheim
2023-01-01,5.2,4.8,3.1
2023-01-02,5.5,5.0,3.3
2023-01-03,5.1,4.7,3.0
