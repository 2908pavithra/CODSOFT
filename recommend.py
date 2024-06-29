import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
movies_df= pd.read_csv(r"c:\Users\pavit\Downloads\movies.csv")



# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the genres
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genres'])


# Calculate the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Convert the similarity matrix to a DataFrame for better readability
cosine_sim_df = pd.DataFrame(cosine_sim, index=movies_df['title'], columns=movies_df['title'])



def get_recommendations(title, cosine_sim_df, movies_df, num_recommendations=3):
    # Get the index of the movie that matches the title
    idx = movies_df[movies_df['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim_df.iloc[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the most similar movies
    sim_scores = sim_scores[1:num_recommendations + 1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top most similar movies
    return movies_df['title'].iloc[movie_indices]

# Take user input for the movie title
user_movie = input("Enter a movie title: ")

# Check if the movie exists in the dataset
if user_movie in movies_df['title'].values:
    # Generate recommendations for the user input movie
    recommendations = get_recommendations(user_movie, cosine_sim_df, movies_df)

    # Display the recommendations
    print(f"\nRecommendations for '{user_movie}':")
    print(recommendations)
else:
    print("The movie title you entered is not in the dataset.")
