# Anime Recommendation System

A portfolio Streamlit application that recommends similar anime titles based on precomputed similarity data. Built as a demonstrable project to showcase data processing, feature engineering, and an interactive UI.

---

## Project overview

This project contains a Streamlit web application that allows users to select an anime title and receive tailored recommendations. The app uses precomputed recommendations (and optionally a similarity matrix used during model development) so the app runs quickly without expensive on-the-fly computations.

## Features

- Interactive Streamlit interface for searching anime and viewing recommendations
- Poster images displayed alongside recommended titles
- Precomputed recommendation mapping for fast response times
- Notebooks and scripts for reproducing dataset processing and building the similarity matrix

## Technologies used

- Python
- Streamlit
- Pandas, NumPy
- scikit-learn (used to build the similarity matrix in notebooks)
- Jupyter notebooks for experimentation and preprocessing

## How the recommendation system works

1. Data is loaded and preprocessed in Jupyter notebooks (text/metadata features are combined and cleaned).
2. Textual features are vectorized (for example, with CountVectorizer or TF-IDF) and cosine similarity is computed between items to build a similarity matrix.
3. The similarity matrix is used to generate a recommendations map (top-N similar titles per anime) which is saved as `recommendations.pkl`.
4. The Streamlit app (`app/app.py`) loads `datasets/processed/merged.csv` and `datasets/processed/recommendations.pkl` at runtime and serves recommendations instantly.

## Dataset information

- Raw source CSV files are included under `datasets/raw/` (for example: [datasets/raw/anime.csv](C:/Users/emanf/Desktop/anime recomendation system/datasets/raw/anime.csv) and [datasets/raw/entities.csv](C:/Users/emanf/Desktop/anime recomendation system/datasets/raw/entities.csv)).
- Processed data used by the app is stored in `datasets/processed/merged.csv` and `datasets/processed/recommendations.pkl` (both included in this repository to allow the app to run out-of-the-box).
- A large precomputed similarity matrix was generated during model development and is stored locally at `datasets/external/similarity.pkl`. This file is large (~530 MB) and is NOT included in the repository. See the note below.

## Important: similarity.pkl (NOT included)

The similarity matrix `datasets/external/similarity.pkl` is large (~530 MB). It is intentionally excluded from the repository to keep the repo lightweight. The repository includes `recommendations.pkl`, a smaller (precomputed) mapping of recommendations, so the app can run without the full matrix.

If you wish to reproduce the full similarity matrix locally, either:

- Run the notebook that generates it (see `notebooks/` and `datasets/external/` notebooks) — be aware this can be computationally expensive and may require significant memory, or
- Download the matrix from an externally hosted location (if provided) into `datasets/external/` as `similarity.pkl`.

## Project structure

- [app/app.py](C:/Users/emanf/Desktop/anime recomendation system/app/app.py) — Streamlit application (main entrypoint)
- [datasets/raw/](C:/Users/emanf/Desktop/anime recomendation system/datasets/raw/) — raw CSVs
- [datasets/processed/merged.csv](C:/Users/emanf/Desktop/anime recomendation system/datasets/processed/merged.csv) — processed data used by the app
- [datasets/processed/recommendations.pkl](C:/Users/emanf/Desktop/anime recomendation system/datasets/processed/recommendations.pkl) — precomputed recommendations used by the app
- [datasets/external/similarity.pkl](C:/Users/emanf/Desktop/anime recomendation system/datasets/external/similarity.pkl) — large similarity matrix (NOT included in repo)
- [notebooks/](C:/Users/emanf/Desktop/anime recomendation system/notebooks/) — analysis and preprocessing notebooks

## Installation (Quick start)

1. Create and activate a Python virtual environment (recommended):

   Windows (PowerShell):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install runtime dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Streamlit app

From the repository root run:

```bash
streamlit run app/app.py
```

The app will open in your browser (usually at http://localhost:8501) and is ready to use with the included `datasets/processed/recommendations.pkl` and `merged.csv`.

## recommendations.pkl

`datasets/processed/recommendations.pkl` is a small pickled object (~2.8 MB) that contains a mapping of anime title -> list of recommended titles. This file is included in the repository so the app can serve recommendations quickly without recomputing the similarity matrix.

## Future improvements

- Add automated data processing scripts (CLI) to create the similarity matrix and recommendations mapping.
- Provide a hosted download for the similarity matrix or use GitHub Releases / cloud storage for sharing large artifacts.
- Add tests for data processing and recommendation outputs.
- Improve CharMood feature and add more user controls (filters by genre, year, rating, etc.).

## Author

- Your Name (replace with your preferred name)
- Portfolio: (add link)
- Contact: (add email/github)

---

If you want, I can now show a dry-run list of files that will be committed (based on the current workspace, honoring the `.gitignore`), and the list of files that will be ignored. I will not run any git commands or push until you explicitly approve.