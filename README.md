# Movie-Cocktail
A machine learning based movie recommendation app.

* Movie Cocktail suggests new movies based on the selected combination of movies.
* Not sure which movie to watch? Want to watch something similar to movies you've watched before?
* Search and select movies you've already watch, mix them as you wish and get the closest movies to the cocktail.
* Here is the link of the app: [moviecocktail](https://moviecocktail.netlify.app/){:target="_blank"}

## How it Works?
* Let's say you want to watch something 30% like 'the Matrix (1999)' and 70% like 'Titanic (1997)' then you can search for the movies **the Matrix (1999)** and **Titanic (1997)**, combine them with the ratios of 30% and 70%  and find the top ten closest movies to this combination.
* The combination/mix represents the "cocktail". The movie cocktail app suggests top 10 closest movies to the cocktail.
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

