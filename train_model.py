import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack
import joblib



action_df = pd.read_csv('data/action.csv')
adventure_df = pd.read_csv('data/adventure.csv')
animation_df = pd.read_csv('data/animation.csv')
biography_df = pd.read_csv('data/biography.csv')
crime_df = pd.read_csv('data/crime.csv')
family_df = pd.read_csv('data/family.csv')
fantasy_df = pd.read_csv('data/fantasy.csv')
noir_df = pd.read_csv('data/film-noir.csv')
history_df = pd.read_csv('data/history.csv')
horror_df = pd.read_csv('data/horror.csv')
mystery_df = pd.read_csv('data/mystery.csv')
romance_df = pd.read_csv('data/romance.csv')
scifi_df = pd.read_csv('data/scifi.csv')
sports_df = pd.read_csv('data/sports.csv')
thriller_df = pd.read_csv('data/thriller.csv')
war_df = pd.read_csv('data/war.csv')

dfs_with_genres = [
    (action_df, 'action'),
    (adventure_df, 'adventure'),
    (biography_df, 'biography'),
    (crime_df, 'crime'),
    (family_df, 'family'),
    (fantasy_df, 'fantasy'),
    (history_df, 'history'),
    (horror_df, 'horror'),
    (mystery_df, 'mystery'),
    (romance_df, 'romance'),
    (scifi_df, 'scifi'),
    (sports_df, 'sports'),
    (thriller_df, 'thriller'),
    (war_df, 'war')
]

for df, genre_name in dfs_with_genres:
    df['genre_main'] = genre_name

combined_df = pd.concat([df for df, _ in dfs_with_genres], ignore_index=True)


combined_df = combined_df[combined_df['description'] != 'Add a Plot']
combined_df = combined_df.dropna(subset=['description'])
combined_df = combined_df.drop_duplicates(subset=['movie_name'], keep='first')
combined_df["year"] = pd.to_numeric(
    combined_df["year"],
    errors="coerce"
)

combined_df = combined_df.dropna(subset=["year"])

train_df, test_df = train_test_split(
    combined_df,
    test_size=0.2,
    random_state=42,
    stratify=combined_df["genre_main"]
)

X_train_text = train_df["description"]
X_test_text = test_df["description"]

y_train = train_df["genre_main"]
y_test = test_df["genre_main"]

vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    min_df=3,
    max_df=0.90,
    stop_words="english"
)
X_train_tfidf = vectorizer.fit_transform(X_train_text)
X_test_tfidf = vectorizer.transform(X_test_text)

model = LogisticRegression(max_iter=1000, n_jobs=-1, class_weight='balanced', random_state=42)


scaler = StandardScaler()

X_train_year = scaler.fit_transform(train_df[["year"]])
X_test_year = scaler.transform(test_df[["year"]])

X_train_final = hstack([X_train_tfidf, X_train_year])
X_test_final = hstack([X_test_tfidf, X_test_year])
model.fit(X_train_final, y_train)

joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
joblib.dump(scaler, 'models/year_scaler.pkl')
joblib.dump(model, 'models/genre_model.pkl')

y_pred = model.predict(X_test_final)
print(classification_report(y_test, y_pred, zero_division=0))

