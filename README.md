# E-handel – snabbrapport

## Syfte

Syftet med projektet är att ta fram en kort, körbar snabbrapport till ledningen för en fiktiv e-handelsplattform. Med hjälp av datasetet `ecommerce_sales.csv` analyserar vi vad som säljer mest, var och när försäljningen sker, hur en typisk order ser ut samt tar fram topp-listor och eventuella avvikelser. Resultatet presenteras i en Jupyter-notebook med nyckeltal och visualiseringar och avslutas med 2–3 konkreta rekommendationer inför nästa kampanjperiod.


## Struktur

Repo:t är uppbyggt enligt kursens rekommenderade struktur:

- `data/ecommerce_sales.csv` – rådata med alla orders.
- `notebooks/report.ipynb` – huvudnotebooken där all analys och alla visualiseringar finns.
- `src/metrics.py` – hjälpfunktioner för att räkna ut nyckeltal (t.ex. intäkt, AOV, toppkategorier).
- `src/diagrams.py` – funktioner för att skapa diagram som används i rapporten.
- `tests/test_diagrams.py` – enkel testfil för att säkerställa att diagram-funktionerna kör utan fel (frivilligt inslag för bättre kodkvalitet).
- `requirements.txt` – lista över alla Python-paket som behövs för att köra projektet.
- `README.md` – den här filen, med beskrivning av projektet och hur man kör det.


## Så kör du

### Skapa virtuell miljö
`python -m venv .venv`

### Aktivera virtuell miljö
`.\.venv\Scripts\Activate`

### Installera beroenden
`pip install -r requirements.txt`

## Paket som ingår (från requirements.txt) och varför de används
- Pandas – för att läsa in CSV-filen och hantera all data i projektet
- Numpy – används av Pandas och för grundläggande numeriska operationer
- Matplotlib – för grafer och visualiseringar i rapporten
- Seaborn – för mer avancerade och snyggare visualiseringar
- Jupyter – för att köra report.ipynb

## Roller i gruppen

- `Soroush Gholamreza` – diagram och visualiseringar
- `Katja Marjaana Christine Drugg` – nyckeltal och beräkningar
- `Ömer Berk Kilicasan` – struktur och innehåll i notebooken
- `Waraporn Chainakhon` – README och strukturering av dokumentation
- `Emmad Abd Alsalam` – markdowntexter och förklaringar i notebooken