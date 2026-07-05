# BuyOrWait

BuyOrWait is a Streamlit demo for AI-assisted game purchase decisions. It uses mock data today and keeps the data-loading layer isolated so backend, BigQuery, or GPU batch outputs can replace CSVs later.

## Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Pages

- BuyOrWait Demo
- Review Bombing Alerts
- Why GPU / Acceleration Evidence

## Data

Mock CSVs live in `app/mock_data/`:

- `game_scores.csv`
- `daily_stats.csv`
- `alerts.csv`
- `benchmark_results.csv`

`app/data_loader.py` is the only place that should need changing when real aggregate tables are available.

## Visual Asset

The homepage hero uses a generated local 3D game-decision visual at `app/assets/buyorwait-shopping-orb.png`. The app does not depend on external image URLs at runtime.
