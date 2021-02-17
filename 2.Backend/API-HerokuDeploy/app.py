
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import pickle
import torch
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#Movie names list:
file = open('data/movies.pkl','rb')
movies = pickle.load(file)
file.close()  

#Embeddings as a tensor for the movies:
file = open('data/movie_factors_tensor.pkl','rb')
movie_factors = pickle.load(file)
file.close()   



class Search(Resource):
    @cross_origin()
    def post(self):
        #Get posted data
        postedData = request.get_json()
        #Get the data
        target = str(postedData["target"])
        numMaxReturn = postedData["max"]
        #Get elements:
        res = [s for s in movies if target in s.lower()]
        if len(res)>numMaxReturn:
            res = res[:numMaxReturn]
        #Return the response (message will be a string array)
        retJson = {
            "message": res,
            "status": 200,
        }
        return jsonify(retJson)

class Mix(Resource):
    @cross_origin()
    def post(self):
        #Get posted data
        postedData = request.get_json()
        #Get the data
        selectedMovies = postedData["selectedMovies"]
        ratios = postedData["ratios"]
        numRec = int(postedData["numRec"])

        #Get ids of selectedMovies:
        idxs = [movies.index(m) for m in selectedMovies]

        #Create the cocktail embedding:
        cocktailEmbd = torch.zeros([1,100])
        for i,idx in enumerate(idxs):
            rawEmbd = movie_factors[idx][None]
            embd = ratios[i]*rawEmbd
            cocktailEmbd = torch.add(cocktailEmbd,embd)
        
        #Find the distance of each movie to the cocktail:
        dists = torch.cdist(movie_factors,cocktailEmbd) # [60k,1]
        #Transform this tensor to a list:
        distsList = dists.tolist()
        distsList = [j for sub in distsList for j in sub]

        #Add ids to the distsList and sort it:
        indexedDistsList = [(idx,dist) for idx,dist in enumerate(distsList)]
        sortedDistances = sorted(indexedDistsList, key=lambda tup: tup[1])
        
        #Avg dist from cocktail to other movies:
        avgDistFromCocktail = round(torch.mean(torch.cdist(movie_factors,cocktailEmbd)).item(),2)

        recMovies = []
        avgDistsOfRecMovies2Cocktail = []
        avgDistsOfRecMovies2Others = []
        #Find the closest movies to the cocktail:
        for i in range(numRec):
            recMovies.append(movies[sortedDistances[i][0]])
            avgDistsOfRecMovies2Cocktail.append(round(sortedDistances[i][1],2))
            avgDistsOfRecMovies2Others.append(round(torch.mean(torch.cdist(movie_factors,movie_factors[sortedDistances[i][0]][None])).item(),2))

        #Return the response (message will be a string array)
        retJson = {
            "avgDistFromCocktail": avgDistFromCocktail,
            "recMovies": recMovies,
            "avgDistsOfRecMovies2Cocktail": avgDistsOfRecMovies2Cocktail,
            "avgDistsOfRecMovies2Others": avgDistsOfRecMovies2Others,
            "status": 200
        }
        return jsonify(retJson)


api.add_resource(Search,"/search")
api.add_resource(Mix,"/mix")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

