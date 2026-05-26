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

## License
MIT