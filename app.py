import time
import streamlit as st
import joblib
import numpy as np
from scipy.sparse import hstack
import re

model = joblib.load("models/genre_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
scaler = joblib.load("models/year_scaler.pkl")

st.set_page_config(
    page_title="Movie Genre Predictor",
    page_icon="(o_o)",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""

<style>
    /* 1. Remove padding around main container (Your Selector) */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* Set overall dark background */
    .stApp {
        background-color: #0c0d10;
        color: #ffffff;
    }

    /* 2. Make metric cards pop slightly (Your Selector) */
    [data-testid="stMetricSimpleValue"] {
        font-family: 'Playfair Display', monospace;
        font-weight: bold;
        color: #E50914 !important;
        font-size: 2.2rem !important;
    }

    /* Style the label inside metric cards to match dark theme */
    [data-testid="stMetricLabel"] {
        color: #a0a5b1 !important;
    }

    /* 3. Smooth button transitions (Your Selector) */
    .stButton>button {
        border-radius: 20px;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
        background-color: #E50914 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
    }

    /* Hover effect for your button */
    .stButton>button:hover {
        background-color: #ff1e27 !important;
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.6) !important;
        transform: translateY(-2px);
    }

    /* 4. Subtitle styling (Your Selector) */
    .hero-subtitle {
        font-size: 1.2rem;
        color: #888888;
        margin-bottom: 2rem;
    }

    /* Input text area styling to match dark theme */
    div[data-baseweb="textarea"] > div {
        background-color: #14161d !important;
        border: 1px solid #232733 !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    /* Custom CSS Card wrapper for predictions */
    .prediction-card {
        background-color: #14161d;
        border: 1px solid #232733;
        border-radius: 16px;
        padding: 20px;
    }

    /* Progress bar layout styling */
    .genre-row {
        margin-bottom: 14px;
    }
    .genre-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 6px;
        font-weight: 600;
        font-size: 1rem;
    }
    .progress-bg {
        background-color: #232733;
        border-radius: 10px;
        height: 8px;
        width: 100%;
        overflow: hidden;
    }
    .progress-fill {
        background-color: #E50914;
        height: 100%;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Movie Genre Predictor")
st.markdown("<p class='hero-subtitle'>A machine learning model designed to predict movie genres based on their plot summaries.</p>", unsafe_allow_html=True)
st.divider()


col_input, col_output = st.columns([1.1, 1.0], gap="large")

with col_input:
    st.markdown("### ENTER MOVIE PLOT")
    
    default_plot = "A disillusioned war veteran embarks on a cross-country journey, forming an unlikely bond with a free-spirited companion. Together, they encounter various people and life-changing experiences that challenge their perspectives on life and freedom."

    
    user_plot = st.text_area(
        label="Input description window",
        value=default_plot,
        height=180,
        max_chars=2000,
        label_visibility="collapsed"
    )
    

    release_year = st.number_input(
        "Release Year",
        min_value=1900,
        max_value=2035,
        value=2020
    )

    predict_btn = st.button(
        "Predict Genres",
        use_container_width=True
    )

with col_output:
    st.markdown("### TOP PREDICTED GENRES")
    st.markdown("<p style='color: #8A8D9F; font-size: 12px; margin-top: -10px;'>Probabilities indicate how well each genre matches the plot.</p>", unsafe_allow_html=True)
    
    if predict_btn:

        if user_plot.strip() == "":
            st.warning("Please enter a movie description.")
            st.stop()

        with st.spinner("Analyzing plot..."):
            time.sleep(0.5)

            clean_plot = user_plot.lower()
            clean_plot = re.sub(r"[^a-zA-Z\s]", "", clean_plot)

            text_features = vectorizer.transform([clean_plot])

            year_feature = scaler.transform([[release_year]])

            features = hstack([text_features, year_feature])

            probabilities = model.predict_proba(features)[0]

            top3 = np.argsort(probabilities)[-3:][::-1]

            best_idx = top3[0]

            st.success(
                f"### Predicted Genre: {model.classes_[best_idx].title()}"
            )

            labels = ["1.", "2.", "3."]

            for rank, idx in enumerate(top3):

                genre = model.classes_[idx]
                confidence = probabilities[idx]

                metric_col, progress_col = st.columns([2,3])

                with metric_col:
                    st.markdown(
                        f"### {labels[rank]} {genre.title()}"
                    )

                with progress_col:
                    st.progress(float(confidence))
                    st.caption(f"{confidence*100:.1f}% confidence")
    
    

st.markdown("<br><hr><br>", unsafe_allow_html=True)


v_col1, v_col2, v_col3 = st.columns(3, gap="medium")

with v_col1:
    st.markdown("**Machine Learning**")
    st.caption("Trained on thousands of movies using advanced NLP techniques.")

with v_col2:
    st.markdown("**Accurate**")
    st.caption("High-performance model with robust predictions.")

with v_col3:
    st.markdown("**Multi-Genre**")
    st.caption("Get the top 3 genres that best match your plot structure.")
