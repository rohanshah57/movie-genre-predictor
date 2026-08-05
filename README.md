# 🎬 Movie Genre Predictor

> A real-time NLP application that predicts movie genres from plot summaries using Machine Learning.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit)](YOUR_LIVE_STREAMLIT_APP_LINK_HERE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](YOUR_GITHUB_REPO_LINK_HERE)

---

## 🌟 Overview

The **Movie Genre Predictor** leverages natural language processing (NLP) to analyze free-form movie plot descriptions and output the top matching genres alongside model confidence scores. 

Whether you're testing an original screenplay idea or analyzing plot archetypes, this app provides real-time multi-genre classification through a clean, interactive user interface.

![App Screenshot](LINK_TO_YOUR_SCREENSHOT_OR_GIF_HERE)

---

## 🚀 Key Features

* **Multi-Genre Probability Scoring:** Displays the top 3 predicted genres along with percentage confidence bars.
* **Interactive UI:** Built with Streamlit for clean, responsive real-time predictions.
* **Metadata Inputs:** Accepts release year and plot inputs to evaluate predictions against historical plot trends.

---

## 🛠️ Tech Stack & Methods

* **Frontend / Hosting:** [Streamlit Cloud](https://streamlit.io/)
* **Model & ML:** Python, `scikit-learn`, `pandas`, `numpy`
* **NLP Pipeline:** TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization
* **Classifier:** Logistic Regression (Multi-label / Multi-class framework)

---

## 🧠 Machine Learning Pipeline

1. **Preprocessing:** Cleaned raw plot text by stripping punctuation, converting to lowercase, and handling stop words.
2. **Feature Extraction:** Vectorized text sequences into sparse matrix representations using **TF-IDF**.
3. **Model Training:** Fit a **Logistic Regression** classifier to evaluate probability distributions across multiple genre tags.
4. **Inference Engine:** Transformed incoming web payload into TF-IDF features to output ordered class probabilities.

---

## 💻 Local Setup & Installation

To run this project locally on your machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/rohanshah57/movie-genre-predictor.git](https://github.com/rohanshah57/movie-genre-predictor.git)
cd movie-genre-predictor
