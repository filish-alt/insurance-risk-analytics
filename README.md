# Insurance Risk Analytics

Repository for the 10 Academy **Insurance Risk Analytics** project.

## Project Structure

```
insurance-risk-analytics/
├── .github/workflows/ci.yml
├── data/                 # tracked by DVC, not Git
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── reports/
│   └── final_report.md
├── tests/
├── .dvc/
├── .gitignore
├── dvc.yaml
├── requirements.txt
└── README.md
```

## Getting Started
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `insurance_data.csv` in the `data/` folder (provide the dataset).
4. Run the notebooks for exploratory analysis and modeling.

## Data Pipeline Reproduction (DVC)
This repository uses DVC to track data versions.
To pull the dataset tracked by DVC:
1. Ensure the python DVC module is installed (`pip install dvc`).
2. Run `python -m dvc pull` to fetch the tracked datasets from local remote storage into the `data/` folder.
3. You can explore the `task-2` branch for the cleaned data version. To fetch old raw datasets, just check out the git commit you wish, then execute `python -m dvc pull`.

## License
MIT