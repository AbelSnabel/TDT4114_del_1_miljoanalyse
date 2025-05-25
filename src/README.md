# Source Code Directory

Denne mappen inneholder kildekoden for prosjektet. Hver modul er designet for å utføre spesifikke oppgaver som datainnhenting, visualisering, statistisk analyse og prediktiv modellering.

## Innhold
- **`hent_lagre.py`**:
  - Inneholder funksjoner for å hente data fra eksterne kilder basert på geografiske koordinater og tidsintervaller.
  - Dataene lagres i en CSV-fil for videre behandling.
  - Viktige funksjoner:
    - `hent(lat, lon, starttid, sluttid, csv_fil)`: Henter data for en gitt lokasjon og tidsperiode og lagrer det i en CSV-fil.

- **`plot.py`**:
  - Inneholder funksjoner for å lage visualiseringer av dataene.
  - Bruker `plotly` for å lage interaktive grafer.
  - Viktige funksjoner:
    - `plot_data(by, df)`: Lager en graf for en valgt by basert på datasettet.

- **`prediktiv_analyse.py`**:
  - Inneholder funksjoner for å utføre prediktiv analyse ved hjelp av lineær regresjon.
  - Bruker `prophet` for å lage prognoser.
  - Viktige funksjoner:
    - `prediktiv_analyse(antall_år, df)`: Utfører prediktiv analyse for et valgt antall år basert på datasettet.

- **`statistikk.py`**:
  - Inneholder funksjoner for å beregne statistiske mål som gjennomsnitt, median og standardavvik.
  - Viktige funksjoner:
    - `statistikk(by, df)`: Beregner og returnerer statistiske mål for en valgt by.

## Bruk
- Funksjonene i denne mappen importeres og brukes i applikasjonen (`app.py`) og i Jupyter Notebooks (`notebooks/app.ipynb`) for å utføre spesifikke oppgaver som datainnhenting, visualisering og analyse.
- Sørg for at denne mappen er inkludert i `PYTHONPATH` for å kunne importere modulene. Dette kan gjøres ved å legge til følgende i koden:
  ```python
  import sys
  import os
  project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
  sys.path.append(os.path.join(project_root, 'src'))
  ```