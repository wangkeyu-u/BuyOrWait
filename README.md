# BuyOrWait 🎮 — To Buy or Not to Buy

> AI 辅助游戏购买决策 Demo —— 识别差评轰炸，给出「买 / 等 / 跳」建议。
>
> An AI-assisted game purchase decision demo — detects review bombing and suggests Buy / Wait / Skip.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-FF4B4B)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 💡 这是 BuyOrWait 的**轻量 Mock 数据版**，用于快速演示产品概念。完整版（1.14 亿条 Steam 真实评测 + GPU 加速 + BigQuery + Cloud Run）请见 → [buyorwait-wang](https://github.com/wangkeyu-u/buyorwait-wang)
>
> 💡 This is the **lightweight mock-data version** of BuyOrWait for quick demos. The full version (114M+ real Steam reviews + GPU acceleration + BigQuery + Cloud Run) lives at → [buyorwait-wang](https://github.com/wangkeyu-u/buyorwait-wang)

---

## 简介 / Overview

Steam 的总体评分把几年前的评价和今天的混在一起——修复了的游戏评分虚低，正在被差评轰炸的游戏评分虚高。BuyOrWait 用**游戏时长加权 + 90 天半衰期衰减**计算「购买信心指数」，并检测差评轰炸，给出清晰的 🟢 买 / 🟡 等 / 🔴 跳 建议。

Steam's overall rating blends years-old sentiment with today's — hiding both games that have been fixed and games being review-bombed right now. BuyOrWait computes a playtime-weighted, 90-day half-life **Purchase Confidence Score** and detects bombing, then gives a clear 🟢 Buy / 🟡 Wait / 🔴 Skip signal.

本仓库使用 Mock CSV 数据，数据加载层已隔离，后续可替换为真实聚合表。/ This repo uses mock CSVs; the data-loading layer is isolated so real aggregate tables can replace them later.

---

## 功能页面 / Pages

| 页面 / Page | 说明 / Description |
|---|---|
| 🛒 BuyOrWait Demo | 购买信心指数（买/等/跳）+ 评分趋势图 / Purchase confidence score + rating trend |
| 🚨 Review Bombing Alerts | 滚动 z-score 异常检测，差评轰炸预警 / Rolling z-score anomaly detection for bombing alerts |
| ⚡ Why GPU / Acceleration Evidence | GPU vs CPU 加速对比证据 / GPU vs CPU acceleration evidence |

---

## 快速开始 / Quick Start

```bash
# 安装依赖 / Install dependencies
pip install -r requirements.txt

# 启动应用 / Run the app
streamlit run app/app.py
```

打开终端输出的地址（通常 `http://localhost:8501`）。/ Open the URL printed in the terminal (usually `http://localhost:8501`).

---

## 数据说明 / Data

Mock CSV 文件位于 `app/mock_data/` / Mock CSVs live in `app/mock_data/`：

- `game_scores.csv` — 游戏信心指数 / Game confidence scores
- `daily_stats.csv` — 每日评分统计 / Daily rating stats
- `alerts.csv` — 差评轰炸警报 / Bombing alerts
- `benchmark_results.csv` — CPU/GPU 性能基准 / CPU/GPU benchmarks

`app/data_loader.py` 是唯一需要修改的数据加载入口——当真实聚合表就绪时，只改这一个文件。/ `app/data_loader.py` is the only file to change when real aggregate tables are available.

---

## 项目结构 / Project Structure

```
BuyOrWait/
├── app/
│   ├── app.py              # Streamlit 主应用 / Main Streamlit app
│   ├── data_loader.py      # 数据加载层（隔离层）/ Data loader (isolated)
│   ├── mock_data/          # Mock CSV 数据 / Mock CSV data
│   └── assets/             # 本地视觉资源 / Local visual assets
├── requirements.txt
└── README.md
```

---

## 指标定义 / Metric Definitions

- **购买信心指数 / Purchase Confidence Score**：`score = Σ(wᵢ·voteᵢ) / Σ(wᵢ) × 100`，其中 `wᵢ = log(1+playtime) × exp(−age_days/90)`。游戏时长权重过滤"随便评"噪声，90 天半衰期确保近期评价占主导。/ Playtime weight filters casual-review noise; 90-day half-life ensures recent sentiment dominates.
- **差评轰炸检测 / Bombing Detection**：每日差评率 z-score（相对 30 天滚动均值）> 3 且每日评测数 > 30 天均值的 2 倍。/ Daily negative-rate z-score (vs 30-day rolling avg) > 3 and daily count > 2× rolling avg.

---

## 视觉资源 / Visual Asset

首页 hero 图使用本地生成的 3D 游戏决策视觉 `app/assets/buyorwait-shopping-orb.png`，运行时不依赖外部图片 URL。/ The homepage hero uses a generated local 3D visual; no external image URL at runtime.

---

## 许可证 / License

MIT
