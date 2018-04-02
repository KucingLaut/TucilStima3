from flask import *
import sys
import json
from Astar import *
app = Flask(__name__)

@app.route("/")
def launch():
    return render_template("index.html")

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.get_json()
    # cara akses data json
    # jsdata['coordinates'][idx]['lat'] nerima latitude
    # jsdata['coordinates'][idx]['lng'] nerima longitude
    arrOfCoords = []
    arrOfEdges = []
    for i in range(len(jsdata['coordinates'])):
        lat = jsdata['coordinates'][i]['lat']
        lng = jsdata['coordinates'][i]['lng']
        arrOfCoords.append([lat,lng])
    arrOfEdges = jsdata['edges']
    adjMatrix = graphGeneration(arrOfCoords,arrOfEdges)
    start = 0
    goal = 4
    sol = Astar(start,goal,arrOfCoords,adjMatrix) 
    print("solution: ")
    print(sol)
    return json.dumps(jsdata)[0];

if __name__ == "__main__":
    app.run()
