<p align="center">
  <img src="images/image1.png" alt="Anime Recommendation System Preview" width="800">
</p>
<p align="center">
  <img src="images/image2.png" alt="Anime Recommendation System Preview" width="800">
</p>
<h1 align="center">Anime Recommendation System</h1>

<p align="center">
  <em>Discover your next favorite anime through intelligent content-based recommendations.</em>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-App-FF4B4B.svg" alt="Streamlit"></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/Scikit--learn-ML-orange.svg" alt="Scikit-learn"></a>
</p>

---

Anime Recommendation System is an interactive **content-based recommendation application** built with Python and Streamlit. It analyzes anime metadata and textual features to recommend titles that are similar to the anime selected by the user.

The project demonstrates a complete machine learning workflow — from **data preprocessing and feature engineering to vectorization, cosine similarity, recommendation generation, and interactive application development**.

## Features

* **Interactive search** — Select an anime and instantly receive recommendations.
* **Content-based recommendations** — Finds similar anime using metadata and textual features.
* **Anime posters** — Displays poster images alongside recommendations.
* **Precomputed recommendations** — Uses a stored recommendation mapping for fast results.
* **Feature engineering** — Combines relevant anime attributes to improve similarity.
* **Data preprocessing** — Includes notebooks for cleaning and preparing the dataset.
* **Streamlit interface** — Provides a simple and interactive user experience.

## Screenshots

### Home Page

<p align="center">
  <img src="screenshots/home.png" alt="Anime Recommendation System Home Page" width="850">
</p>

### Recommendations

<p align="center">
  <img src="screenshots/recommendations.png" alt="Anime Recommendations" width="850">
</p>

## Technologies

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| Python           | Core programming language                |
| Streamlit        | Interactive web application              |
| Pandas           | Data processing and manipulation         |
| NumPy            | Numerical operations                     |
| Scikit-learn     | Vectorization and similarity computation |
| Jupyter Notebook | Data analysis and experimentation        |
| Pickle           | Storing precomputed recommendations      |

## How it works

The recommendation system follows a content-based filtering approach.

```text
Raw Anime Data
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering
      ↓
Text / Metadata Vectorization
      ↓
Cosine Similarity
      ↓
Top-N Similar Anime
      ↓
Recommendation Mapping
      ↓
Streamlit Application
```

### 1. Data preprocessing

Anime metadata is loaded from the raw datasets and cleaned using Pandas.

Relevant features are combined and prepared for the recommendation pipeline.

### 2. Feature engineering

Textual and categorical anime information is transformed into useful features.

Depending on the experiment, techniques such as **CountVectorizer** or **TF-IDF** can be used to convert textual information into numerical representations.

### 3. Similarity calculation

The system calculates **cosine similarity** between anime feature vectors.

Anime with more similar feature representations receive higher similarity scores.

### 4. Recommendation generation

For every anime, the most similar titles are identified and stored in:

```text
datasets/processed/recommendations.pkl
```

The Streamlit application then retrieves these precomputed recommendations instead of recalculating the complete similarity matrix for every request.

## Dataset

The project uses anime metadata stored in CSV format.

### Raw data

```text
datasets/raw/
├── anime.csv
└── entities.csv
```

### Processed data

```text
datasets/processed/
├── merged.csv
└── recommendations.pkl
```

`merged.csv` contains the processed anime data used by the application.

`recommendations.pkl` contains the precomputed recommendation mapping.

## Similarity Matrix

During model development, a complete similarity matrix was generated and stored locally as:

```text
datasets/external/similarity.pkl
```

The matrix is approximately **530 MB** and is intentionally excluded from the GitHub repository to keep the repository lightweight.

The application does **not** require the full similarity matrix to run.

Instead, it uses the smaller:

```text
datasets/processed/recommendations.pkl
```

which contains the top recommendations for each anime.

## Project Structure

```text
anime-recommendation-system/
│
├── app/
│   └── app.py
│
├── datasets/
│   ├── raw/
│   │   ├── anime.csv
│   │   └── entities.csv
│   │
│   ├── processed/
│   │   ├── merged.csv
│   │   └── recommendations.pkl
│   │
│   └── external/
│       ├── 02_notebook.ipynb
│       ├── 03_notebook.ipynb
│       └── similarity.pkl
│
├── screenshots/
│   ├── home.png
│   └── recommendations.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

> `similarity.pkl` is generated during development but is not included in the GitHub repository because of its large file size.

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### Create a virtual environment

#### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Quick Start

Start the Streamlit application from the project root:

```bash
streamlit run app/app.py
```

Streamlit will provide a local address similar to:

```text
http://localhost:8501
```

Open the address in your browser and select an anime to receive recommendations.

## Precomputed Recommendations

The application uses:

```text
datasets/processed/recommendations.pkl
```

This file stores a mapping similar to:

```text
Anime Title
    ↓
Recommendation 1
Recommendation 2
Recommendation 3
Recommendation 4
Recommendation 5
```

Using precomputed recommendations allows the application to respond quickly without loading the complete similarity matrix.

## Machine Learning Concepts

This project demonstrates several important machine learning concepts:

* Data preprocessing
* Feature engineering
* Text vectorization
* Cosine similarity
* Content-based filtering
* Similarity matrices
* Recommendation generation
* Model artifact serialization

## Limitations

* Recommendations depend on the quality of available anime metadata.
* The system does not currently learn individual user preferences.
* New anime require the recommendation data to be regenerated.
* The complete similarity matrix requires significant storage and memory.
* Content-based recommendations may not capture subjective user preferences.

## Future Improvements

* Add genre filters.
* Add rating and year filters.
* Add anime type filters.
* Introduce personalized recommendations.
* Add user ratings and feedback.
* Improve feature engineering.
* Add automated preprocessing scripts.
* Add recommendation evaluation metrics.
* Deploy the application online.
* Experiment with more advanced recommendation techniques.

## Learning Outcomes

Through this project, I gained practical experience with:

* Python for machine learning
* Pandas and NumPy
* Data preprocessing
* Feature engineering
* Text vectorization
* Scikit-learn
* Cosine similarity
* Recommendation systems
* Streamlit application development
* Managing machine learning artifacts with Git and GitHub

## Author

**Eman Fatima**

BS Artificial Intelligence Student

GitHub: `https://github.com/YOUR-USERNAME`

---

## License

This project is created for **educational and portfolio purposes**.

