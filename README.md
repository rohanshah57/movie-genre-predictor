# 🎬 Movie Genre Predictor

> This is a small project that uses natural language processing and machine learning to predict genres using plot descriptions.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit)]([https://movie-genre-predictor-bhqmrr97dofs5tezac9jmr.streamlit.app/])
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)]([https://github.com/rohanshah57/movie-genre-predictor])

---

## Overview

The **Movie Genre Predictor** uses natural language processing to take in a movie plot description and output the best matching genre. 

The site works with an original or unoriginal plot, and displays a multi-genre classification accompanied with confidence scores.

![App Screenshot](<img width="1257" height="805" alt="genre_predictor" src="https://github.com/user-attachments/assets/44045253-0d13-41d4-8668-85cab2d3ff34" />)

---

## Key Features

* **Multi-Genre Probability Scoring:** Displays the top 3 predicted genres along with percentage confidence.
* **UI:** Built with Streamlit.
* **Inputs:** Accepts release year and plot inputs to check predictions against historical plot trends.

---

## Methods & Pipeline

1. **Preprocessing:** Use Regex to clean the text by removing any punctuation, numbers, and changing upper-case characters to lower-case.
2. **Feature Extraction:** Vectorize text sequences into sparse matrix representations using **TF-IDF**.
3. **Model Training:** Fit a **Logistic Regression** classifier to check probability distributions across multiple genre tags.
4. **Prediction:** Output the top three genres.
5. **Year:** I added a year input because I detected a correlation between some genres like film-noir and war to the release year. Thus I thought that adding a year input would help the model accuracy for more of the underrepresented genres.
