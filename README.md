# Movie-Cocktail
A machine learning based movie recommendation app.

# Movie Cocktail
* Movie Cocktail suggests new movies based on the selected combination of movies.
* Not sure which movie to watch? Want to watch something similar to movies you've watched before?
* Search and select movies you've already watch, mix them as you wish and get the closest movies to the cocktail.
* Here is the link of the app: [moviecocktail](https://www.moviecocktail.netlify.app)

## How it Works?
* Let's say you want to watch something 30% like 'the Matrix (1999)' and 70% like 'Titanic (1997)' then you can search for the movies **the Matrix (1999)** and **Titanic (1997)**,combine them as you wish and find the top ten closest movies to this combination.
* Note that, the program will work for a single movie as well, so you don't always have to mix the movies.

## Distances?
* These values are basically L2 distances between vectors. There are three different distance measures specified.
* First distance on the top represents the average distance of the cocktail to any movie.
* The second one represents the distance between the cocktail to the specified movie.
* Extra distance info button shows the average distance of the specified movie to any other movie.

## Under the Hood
* Movie Cocktail uses movie embeddings obtained by a collaborative filtering model trained on 25m movie ratings.
* By using the embedding vectors of selected movies, a new combined embedding vector is generated. After that, it is all about finding the closest L2 distances to the generated new embedding vector.

## Tips
* You don't have to mix the movies, you can just select a single movie, and find the closest movies to the specified movie. In this case slider value won't matter as long as it is greater than zero.
* Search bar only allows searches of three or more characters. So if you are looking for a movie '21' you should search as '21 (' or if you're looking for the movie 'V' then you should search as 'V ('
* This project is done for educational purposes only, there might be some bugs on the GUI.
