import streamlit as st
import pandas as pd
import pickle
from pathlib import Path


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Anime Recommendation System",
    page_icon="🎌",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    /* Hide default streamlit padding at top so navbar sits snug */
    .block-container {
        padding-top: 2rem;
    }

    /* ---------------- NAVBAR BUTTONS ---------------- */
     div[data-testid="column"] div.stButton > button {
    background-color: transparent;
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: inherit;
    font-weight: 600;
    font-size: 0.9rem;
    height: 2.4rem;
    padding: 0 1rem;
    border-radius: 8px;
    line-height: 1;
    transition: background-color 0.2s ease;
}

    div[data-testid="column"] div.stButton > button:hover {
        background-color: rgba(120, 120, 120, 0.15);
        color: inherit;
    }

    /* ---------------- CENTERED TEXT ---------------- */
    h1 {
        text-align: center;
    }

    .intro-text {
        text-align: center;
        font-size: 1rem;
        color: #888;
        margin-bottom: 1.5rem;
    }

    /* Center the selectbox + search button */
    div[data-testid="stSelectbox"] {
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }

    /* ---------------- HERO SECTION (Home page) ---------------- */
    .hero {
        text-align: center;
        padding: 4rem 1rem 3rem 1rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #999;
        max-width: 650px;
        margin: 0 auto 2rem auto;
    }

    .feature-card {
        border: 1px solid #333;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background-color: rgba(255, 255, 255, 0.02);
    }

    .feature-card h3 {
        margin-bottom: 0.5rem;
    }

    .feature-card p {
        color: #999;
        font-size: 0.9rem;
    }

    /* ---------------- EQUAL-SIZE ANIME CARDS ---------------- */
    .anime-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        height: 380px;
        width: 100%;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 10px;
        box-sizing: border-box;
        overflow: hidden;
        background-color: rgba(255, 255, 255, 0.02);
    }

    .anime-card img {
        height: 260px;
        width: 100%;
        object-fit: cover;
        border-radius: 6px;
        margin-bottom: 10px;
    }

    .anime-card .anime-title {
        text-align: center;
        font-weight: 600;
        font-size: 0.9rem;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
    }
    /* Hide Streamlit's default header/toolbar (Deploy button, menu, etc.) */
header[data-testid="stHeader"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "datasets" / "processed" / "merged.csv"
RECOMMENDATIONS_PATH = (
    BASE_DIR / "datasets" / "processed" / "recommendations.pkl"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


@st.cache_data
def load_recommendations():
    with open(RECOMMENDATIONS_PATH, "rb") as file:
        return pickle.load(file)


df = load_data()
recommendations_map = load_recommendations()

anime_titles = df["title"].dropna().unique().tolist()
poster_lookup = df.set_index("title")["image_url"].to_dict()


def recommend(anime):
    return recommendations_map.get(anime, [])


# --------------------------------------------------
# SESSION STATE (simple router)
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"


def go_to(page_name):
    st.session_state.page = page_name


# --------------------------------------------------
# NAVBAR (top right)
# --------------------------------------------------

nav_spacer, nav_home, nav_explore, nav_charmood = st.columns(
    [6, 1, 1, 1.3]
)

with nav_home:
    if st.button("Home", key="nav_home", use_container_width=True):
        go_to("Home")

with nav_explore:
    if st.button("Explore", key="nav_explore", use_container_width=True):
        go_to("Explore")

with nav_charmood:
    if st.button("CharMood", key="nav_charmood", use_container_width=True):
        go_to("CharMood")

#st.divider()


# --------------------------------------------------
# PAGE: HOME (Landing page)
# --------------------------------------------------

def render_home():

    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">🎌 Anime Recommendation System</div>
            <div class="hero-subtitle">
                Discover your next favorite anime. Pick a title you already
                love and get instantly matched with similar shows —
                powered by smart recommendations.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    spacer_l, cta_col, spacer_r = st.columns([2, 1, 2])
    with cta_col:
        if st.button(
            "🚀 Start Exploring",
            use_container_width=True,
            type="primary"
        ):
            go_to("Explore")

    st.write("")
    st.write("")

    feat1, feat2, feat3 = st.columns(3)

    with feat1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🔍 Explore</h3>
                <p>Search any anime and get 5 tailored recommendations
                instantly.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with feat2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🎭 CharMood</h3>
                <p>Find anime that match the mood or vibe you're
                looking for.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with feat3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>⭐ Curated</h3>
                <p>Recommendations built from real similarity data,
                not guesswork.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# PAGE: EXPLORE (search + recommendations)
# --------------------------------------------------

def render_explore():

    st.title("🎌 Anime Recommendation System")

    st.markdown(
        "<p class='intro-text'>Enter an anime you like and get similar "
        "anime recommendations.</p>",
        unsafe_allow_html=True
    )

    left_spacer, center_col, right_spacer = st.columns([1, 2, 1])

    with center_col:
        anime = st.selectbox("Select an anime", anime_titles)
        recommend_clicked = st.button(
            "Recommend Anime",
            use_container_width=True
        )

    if recommend_clicked:

        recommendations = recommend(anime)[:5]

        st.subheader("✨ Recommended Anime")

        if recommendations:

            columns = st.columns(5)

            for column, recommendation in zip(columns, recommendations):

                poster_url = poster_lookup.get(recommendation)

                with column:
                    st.markdown(
                        f"""
                        <div class="anime-card">
                            <img src="{poster_url if poster_url else ''}" />
                            <div class="anime-title">{recommendation}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:
            st.warning("No recommendations found for this anime.")


# --------------------------------------------------
# PAGE: CHARMOOD (placeholder)
# --------------------------------------------------

def render_charmood():

    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">🎭 CharMood</div>
            <div class="hero-subtitle">
                Mood-based anime discovery is coming soon — pick a vibe
                (uplifting, dark, heartwarming, intense) and get anime
                that match it.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    spacer_l, mid, spacer_r = st.columns([1, 1, 1])
    with mid:
        st.info("🚧 This feature is under construction. Check back soon!")


# --------------------------------------------------
# ROUTER
# --------------------------------------------------

if st.session_state.page == "Home":
    render_home()
elif st.session_state.page == "Explore":
    render_explore()
elif st.session_state.page == "CharMood":
    render_charmood()