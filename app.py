# app.py
import streamlit as st
import pandas as pd
import pickle
import gzip
import requests
import os

st.set_page_config(page_title="Movie Recommender", layout="wide")

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"  # keep or replace with your key


@st.cache_data(show_spinner=True)
def load_popularity_model(path="popularity_model.pkl"):
    """
    Try to load a popularity DataFrame from a pickle.
    Returns None if not available.
    """
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return pickle.load(f)


@st.cache_data(show_spinner=True)
def load_movie_list(path="movie_list.pkl", gz_path="content_model.pkl.gz"):
    """
    Load the movies DataFrame created by preprocessing.
    Tries a plain pickle first (movie_list.pkl) and then a gzipped content pickle.
    """
    # 1) try standard pickle (from your `pickle.dump(new,open('movie_list.pkl','wb'))`)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # 2) try gzipped pickle used earlier (content_model.pkl.gz)
    if os.path.exists(gz_path):
        with gzip.open(gz_path, "rb") as f:
            return pickle.load(f)

    # Not found
    return None


@st.cache_data(show_spinner=True)
def load_similarity(path="similarity.pkl"):
    """
    Load the similarity matrix (numpy array) created by preprocessing.
    """
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return pickle.load(f)


def fetch_poster(movie_id):
    """
    Query TMDB for the poster path for the provided movie id.
    Returns full image url or None on failure.
    """
    if movie_id is None:
        return None
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        resp = requests.get(url, timeout=6)
        resp.raise_for_status()
        data = resp.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except requests.RequestException:
        # don't spam UI with traceback; return None so we can display placeholder
        return None
    return None


def get_movie_id_column(df):
    """Return the column name in df that holds the numeric TMDB id if present."""
    for candidate in ("movie_id", "id", "movieId", "tmdb_id"):
        if candidate in df.columns:
            return candidate
    return None


def recommend_from_similarity(title, movies_df, similarity_matrix, top_n=5):
    """
    Given a title, movies dataframe, and similarity matrix (2D array), return top_n titles and poster URLs.
    """
    if movies_df is None or similarity_matrix is None:
        return [], []

    # find index of the movie title
    matches = movies_df[movies_df["title"] == title]
    if matches.empty:
        return [], []

    idx = matches.index[0]
    # distances is a list of (index, score)
    distances = list(enumerate(similarity_matrix[idx]))
    # sort descending by score
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    movie_id_col = get_movie_id_column(movies_df)

    recommended_titles = []
    recommended_posters = []
    # skip the first one (itself)
    count = 0
    for i, score in distances:
        if i == idx:
            continue
        # safety check
        if i >= len(movies_df):
            continue
        row = movies_df.iloc[i]
        rec_title = row.get("title", None)
        rec_id = row.get(movie_id_col) if movie_id_col else None

        recommended_titles.append(rec_title if rec_title else "Unknown Title")
        recommended_posters.append(fetch_poster(int(rec_id)) if rec_id is not None and str(rec_id).isdigit() else None)

        count += 1
        if count >= top_n:
            break

    return recommended_titles, recommended_posters


# ------------------------------
# Load models/data
# ------------------------------
popularity_df = load_popularity_model("popularity_model.pkl")
movies_df = load_movie_list("movie_list.pkl", "content_model.pkl.gz")
similarity = load_similarity("similarity.pkl")

# If movies_df loaded but similarity didn't, try content_model that may have similarity inside (legacy)
# (Some workflows saved 'tagged_movie' which might include a 'similarity' column); handle that case:
if similarity is None and movies_df is not None and "similarity" in movies_df.columns:
    similarity = movies_df["similarity"].values.tolist()  # might need conversion to 2D array

# Basic UI
st.title("🎬 Movie Recommender System")

system = st.sidebar.radio("Select Recommendation System", ["Popularity Based", "Content Based"])

if system == "Popularity Based":
    st.header("Popularity-based recommendations")

    if popularity_df is None:
        st.warning("No `popularity_model.pkl` found. Make sure you placed it in the app folder.")
    else:
        # If genres column is a list, explode to rows for genre selection
        df_pop = popularity_df.copy()
        if "genres" in df_pop.columns and isinstance(df_pop["genres"].iloc[0], list):
            # explode duplicates so each row has a single genre (non-destructive by using copy)
            df_pop = df_pop.explode("genres")

        if "genres" in df_pop.columns:
            selected_genre = st.selectbox("Select genre", sorted(df_pop["genres"].dropna().unique()))
            filtered = df_pop[df_pop["genres"] == selected_genre]
        else:
            # fallback: if no genres in popularity file, show all
            filtered = df_pop

        # ensure we have title and id/score columns
        for col in ("title", "score"):
            if col not in filtered.columns:
                st.error(f"Expected column `{col}` not found in popularity model.")
                st.stop()

        # pick top results
        filtered = filtered[["title", "score", "id" if "id" in filtered.columns else ("movie_id" if "movie_id" in filtered.columns else None)]].copy()
        # remove the extra column that is None if not present
        filtered = filtered.loc[:, filtered.columns.notnull()]

        filtered = filtered.sort_values("score", ascending=False).head(250)

        # Display grid-like list (image + title + score)
        for _, row in filtered.iterrows():
            st.markdown(f"### {row['title']}")
            # ID may be missing; try to fetch poster only if present
            movie_id = None
            if "id" in row.index and pd.notna(row["id"]):
                movie_id = row["id"]
            elif "movie_id" in row.index and pd.notna(row["movie_id"]):
                movie_id = row["movie_id"]

            poster = fetch_poster(int(movie_id)) if movie_id is not None and str(movie_id).isdigit() else None
            if poster:
                st.image(poster, caption=f"Score: {row['score']:.2f}", use_column_width=True)
            else:
                st.write(f"Score: {row['score']:.2f} — Poster not available")

elif system == "Content Based":
    st.header("Content-based recommendations (similarity)")

    if movies_df is None:
        st.warning("No movie list found (expected `movie_list.pkl` or `content_model.pkl.gz`). Place it in the app folder and restart.")
        st.stop()

    if similarity is None:
        st.warning("No similarity matrix found (expected `similarity.pkl`). Place it in the app folder and restart.")
        st.stop()

    # Prepare movie titles for selection
    titles = movies_df["title"].drop_duplicates().values
    selected_movie = st.selectbox("Select a movie", titles)

    if st.button("Recommend"):
        rec_titles, rec_posters = recommend_from_similarity(selected_movie, movies_df, similarity, top_n=5)

        if not rec_titles:
            st.info("No recommendations found for this title.")
        else:
            cols = st.columns(5)
            for i, col in enumerate(cols):
                if i < len(rec_titles):
                    with col:
                        col.write(rec_titles[i])
                        if rec_posters[i]:
                            col.image(rec_posters[i], use_column_width=True)
                        else:
                            col.write("Poster not available")
                else:
                    with col:
                        col.write("—")
