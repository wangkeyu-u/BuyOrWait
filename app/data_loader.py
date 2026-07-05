from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


DATA_DIR = Path(__file__).parent / "mock_data"


@st.cache_data
def load_game_scores() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "game_scores.csv", parse_dates=["last_updated"])


@st.cache_data
def load_daily_stats() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "daily_stats.csv", parse_dates=["date"])


@st.cache_data
def load_alerts() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "alerts.csv", parse_dates=["alert_date"])


@st.cache_data
def load_benchmarks() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "benchmark_results.csv")


def get_game_names() -> list[str]:
    scores = load_game_scores()
    return scores.sort_values("game_name")["game_name"].tolist()


def get_game_score(game_name: str) -> pd.Series:
    scores = load_game_scores()
    return scores.loc[scores["game_name"] == game_name].iloc[0]


def get_daily_for_game(game_name: str) -> pd.DataFrame:
    daily = load_daily_stats()
    return daily.loc[daily["game_name"] == game_name].sort_values("date")


def get_alert_window(game_name: str, alert_date: pd.Timestamp, days: int = 21) -> pd.DataFrame:
    daily = get_daily_for_game(game_name).copy()
    start = alert_date - pd.Timedelta(days=days)
    end = alert_date + pd.Timedelta(days=days)
    return daily.loc[(daily["date"] >= start) & (daily["date"] <= end)]
