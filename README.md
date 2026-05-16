# Engineering Data Pipeline - Corrosion Rate Analysis

**Developer:** Jefrey Ferrer  
**Section:** BSME 1B  
**Student ID:** TUPM-25-0577  

## Project Overview
This Python data pipeline automates the ingestion, cleaning, and processing of experimental material degradation data. It calculates the cumulative mass loss (g) over time for both an uncoated control specimen and a coated protective specimen.

## Project Architecture
```text
📁 EDS_TUPM-25-0577_Ferrer
│
├── 📁 data/
│   └── 📄 dataset_original.csv    # Raw laboratory spreadsheet data
│
├── 📁 outputs/
│   └── 📄 dataset_filtered.csv    # Processed engineering metrics
│
├── 📄 main.py                     # Core automated data pipeline script
├── 📄 requirements.txt            # Required software environment packages
└── 📄 README.md                   # Project documentation