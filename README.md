# Interaktiv Visualiseringsapp

Denne applikasjonen er en interaktiv visualiseringsplattform bygget med Dash. Den lar brukere utforske, analysere og visualisere miljødata basert på geografiske koordinater og tidsintervaller. Appen kombinerer datavisualisering, statistikk og prediktiv analyse for å gi innsikt i dataene.

## Funksjonalitet

### 1. **Datainnhenting og lagring**
- **CSV-håndtering**: Applikasjonen laster inn eksisterende data fra `lokasjonsdata.csv`. Hvis filen ikke finnes eller er tom, opprettes en ny CSV-fil med en tom `Date`-kolonne.
- **Dynamisk datainnhenting**: Brukeren kan klikke på kartet for å hente data basert på geografiske koordinater og et valgt tidsintervall. Dataene lagres automatisk i CSV-filen.

### 2. **Brukergrensesnitt**
- **Dato-velgere**: Brukeren kan velge start- og sluttdato for dataene som skal analyseres.
- **Plot-type**: Brukeren kan velge mellom tre typer analyser:
  - **Visualisering**: Grafisk fremstilling av data.
  - **Statistikk**: Beregning av statistiske mål som gjennomsnitt og standardavvik.
  - **Prediktiv Analyse**: Prognoser basert på lineær regresjon.
- **By-velger**: Dynamisk dropdown-meny for å velge en by (kolonne) fra datasettet.
- **Prediksjons-slider**: Lar brukeren velge antall år for prediktiv analyse.
- **Kart**: Et interaktivt kart hvor brukeren kan klikke for å velge koordinater. Markører vises på kartet for å indikere valgte punkter.

### 3. **Visualisering og analyse**
- **Graf**: Viser resultatene av den valgte analysen (visualisering, statistikk eller prediktiv analyse).
- **Koordinatvisning**: Viser de valgte koordinatene fra kartet.
- **Markører**: Viser markører på kartet for valgte koordinater.

## Teknologier og avhengigheter
- **Dash**: For å bygge det interaktive brukergrensesnittet.
- **Dash Leaflet**: For å integrere det interaktive kartet.
- **Pandas**: For databehandling og manipulering.
- **Plotly**: For å lage interaktive grafer.
- **Egendefinerte moduler**:
  - `plot.py`: Funksjoner for datavisualisering.
  - `statistikk.py`: Funksjoner for statistiske beregninger.
  - `prediktiv_analyse.py`: Funksjoner for prediktiv analyse.
  - `hent_lagre.py`: Funksjoner for å hente og lagre data.

## Hvordan bruke applikasjonen
1. **Start applikasjonen**:
   - Sørg for at alle nødvendige avhengigheter er installert.
   - Kjør applikasjonen ved å bruke kommandoen:
     ```bash
     python app.py
     ```
2. **Velg parametere**:
   - Velg start- og sluttdato for dataene.
   - Velg ønsket plot-type og by for analyse.
   - Klikk på kartet for å hente data for spesifikke koordinater.
3. **Analyser dataene**:
   - Se resultatene i grafen og på kartet.
   - Bruk slideren for å justere antall år for prediktiv analyse.

## Filstruktur
- **`app.py`**: Hovedfilen som kjører applikasjonen.
- **`src/`**: Inneholder moduler for databehandling, visualisering og analyse.
- **`data/`**: Inneholder datasettet `lokasjonsdata.csv`.
- **`notebooks/`**: Inneholder Jupyter Notebooks for testing og utvikling.
- **`resources/`**: Inneholder ressurser som bilder og dokumentasjon.

## Viktige detaljer
- **Dynamisk datainnhenting**: Data hentes kun for gyldige koordinater. Klikk på kartet i områder med tilgjengelige data.
- **Feilhåndtering**: Hvis ingen data er tilgjengelige for valgte koordinater eller tidsintervaller, vises en melding i brukergrensesnittet.

## Fremtidige forbedringer
- Legge til flere visualiseringstyper.
- Forbedre feilhåndtering og brukeropplevelse.
- Optimalisere ytelsen for store datasett.