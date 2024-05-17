import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommendation System')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies_list_df = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies_list_df[movies_list_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in similar_movies:
        recommended_movies.append(movies_list_df.iloc[i[0]]['title'])

    return recommended_movies

movie_selected = st.selectbox('Select a movie:', movies_list_df['title'].values)

if st.button('Recommend'):
    recommendations = recommend(movie_selected)
    for movie in recommendations:
        st.write(movie)
