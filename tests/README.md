# Tests Directory

Denne mappen inneholder tester for prosjektet. Testene er skrevet med `unittest`-rammeverket og dekker funksjonaliteten til modulene i `src/`.

## Innhold
- **`testHentCSV`**: Tester funksjonen `hent` for å sikre at data hentes og lagres korrekt i CSV-filen.
- **`tearDown`**: Sørger for at testmiljøet ryddes opp ved å slette den genererte CSV-filen etter hver test.

## Hvordan testene fungerer
1. **Oppsett**:
   - Testene bruker en midlertidig CSV-fil (`lokasjonsdata.csv`) som lagres i `data/`-mappen.
   - Testene simulerer kall til funksjoner i `src/`-modulene med testdata.

2. **Testprosess**:
   - `testHentCSV`: Kaller funksjonen `hent` med testparametere (latitude, longitude, starttid, sluttid) og sjekker om CSV-filen opprettes korrekt.
   - `tearDown`: Etter hver test slettes den midlertidige CSV-filen for å sikre at testene ikke påvirker hverandre.

3. **Feilhåndtering**:
   - Hvis en test feiler, gir `unittest` detaljer om hva som gikk galt, inkludert forventet og faktisk resultat.

## Hvordan kjøre testene
1. Naviger til prosjektmappen i terminalen.
2. Kjør følgende kommando for å kjøre alle testene:
   ```bash
   python3 -m unittest src_tester.py