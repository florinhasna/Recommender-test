import csv

# File details
folder = "ml-32m"
movies = "movies.csv"
ratings = "ratings.csv"

# Holds contents of movies features file
movies_array = []

# Rating data of movie
movie_ratings = []

AMOUNT_BINARY_DIGITS = 10

# Read in movie features file
def read_movie_features():
    print("Reading movies features...")
    with open(f"{folder}/{movies}", mode='r', encoding='utf-8') as file:  # Specify encoding
        reader = csv.DictReader(file)
        for row in reader:
            # Store in list for easier processing
            movies_array.append(row)
    # Read the ratings
    read_movie_ratings()

# Read in ratings
def read_movie_ratings():
    print("Reading movie ratings...")
    with open(f"{folder}/{ratings}", mode='r', encoding='utf-8') as file:  # Specify encoding
        reader = csv.DictReader(file)
        for row in reader:
            # Store ratings of user 1 in list for easier processing
            if row['userId'] == '1':
                movie_ratings.append(row)
    # Process the ratings of the user
    process_ratings()

user_preference = []

# Process the rating data of user
def process_ratings():
    print("Processing ratings by genres...")
    for rating in movie_ratings:
        # take the movieId of each film user has rated
        movie_id = int(rating['movieId'])
        given_rating = int(rating['rating'])
        
        # retrieve the genre tags of the movie
        movie_details = movies_array[movie_id - 1]  # Adjust for 0-based indexing
        user_preference.append({ 'genre': movie_details['genres'], 'givenRating': given_rating })
    
    # Generate the map
    generate_map()

# Use a dictionary to store genre-binary mappings
genre_map = {}

def generate_map():
    print("Generating ordered binary map for genres...")

    counter = 0
    processed_genres = set()

    def get_binary_string(num, length=AMOUNT_BINARY_DIGITS):
        return format(num, f'0{length}b')  # Convert number to binary string with padding
    
    for preference in user_preference:
        genre = preference['genre']
        if genre in processed_genres:
            continue  # Skip if already processed

        genre_map[genre] = get_binary_string(counter)
        counter += 1
        processed_genres.add(genre)

# Function to get binary representation of a genre
def get_genre_binary(genre):
    if genre in genre_map:
        return {"binary": genre_map[genre], "mapLabel": genre}
    return None

# Run the pipeline
read_movie_features()