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
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Sleek Aesthetics
st.markdown("""
<style>
/* Remove padding around main container */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}
/* Make metric cards pop slightly */
[data-testid="stMetricSimpleValue"] {
    font-family: 'Courier New', monospace;
    font-weight: bold;
}
/* Smooth button transitions */
.stButton>button {
    border-radius: 20px;
    padding: 0.5rem 2rem;
    transition: all 0.3s ease;
}
/* Subtitle styling */
.hero-subtitle {
    font-size: 1.2rem;
    color: #888888;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True) # <-- Fixed parameter here


# 4. Hero Section
st.title("🎬 Movie Genre Predictor")
st.markdown("<p class='hero-subtitle'>A machine learning model designed to predict movie genres based on their plot summaries.</p>", unsafe_allow_html=True)
st.divider()


# 5. Core Layout: Grid Matrix
col_input, col_output = st.columns([1.1, 1.0], gap="large")

with col_input:
    st.markdown("### 📝 ENTER MOVIE PLOT")
    
    # Pre-filled default text matching the prompt image description
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
        "Predict Genres ✨",
        use_container_width=True
    )

with col_output:
    st.markdown("### 📊 TOP PREDICTED GENRES")
    st.markdown("<p style='color: #8A8D9F; font-size: 12px; margin-top: -10px;'>Probabilities indicate how well each genre matches the plot.</p>", unsafe_allow_html=True)
    
    # Define visualization blocks matching UI cards
    if predict_btn:

        if user_plot.strip() == "":
            st.warning("Please enter a movie description.")
            st.stop()

        with st.spinner("Analyzing plot..."):
            time.sleep(0.5)

            # TF-IDF
            clean_plot = user_plot.lower()
            clean_plot = re.sub(r"[^a-zA-Z\s]", "", clean_plot)

            text_features = vectorizer.transform([clean_plot])

            # Scale the release year
            year_feature = scaler.transform([[release_year]])

            # Combine features
            features = hstack([text_features, year_feature])

            # Get probabilities
            probabilities = model.predict_proba(features)[0]

            # Sort highest probabilities
            top3 = np.argsort(probabilities)[-3:][::-1]

            best_idx = top3[0]

            st.success(
                f"### 🎯 Predicted Genre: {model.classes_[best_idx].title()}"
            )

            labels = ["🥇", "🥈", "🥉"]

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

# 4. Bottom Value Proposition Grid
# Render four distinct visual columns to mirror the dashboard value banners
v_col1, v_col2, v_col3 = st.columns(3, gap="medium")

with v_col1:
    st.markdown("🤖 **Machine Learning**")
    st.caption("Trained on thousands of movies using advanced NLP techniques.")

with v_col2:
    st.markdown("🎯 **Accurate**")
    st.caption("High-performance model with robust predictions.")

with v_col3:
    st.markdown("📦 **Multi-Genre**")
    st.caption("Get the top 3 genres that best match your plot structure.")




