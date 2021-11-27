from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api
from routes.patentesRouter import PatentesRouter
from routes.patentesIdRouter import PatentesIdRouter
from functools import wraps
from flask_cors import CORS

#pip install Flask
#pip install flask_restful
#pip install flask_cors
#app.secret_key = 'myawesomesecretkey'
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.before_request
def before_request():
  print('-------*endpoint: %s, url: %s, path: %s' % (
  request.endpoint,
  request.url,
  request.path),'*------')

api.add_resource(PatentesRouter, '/api/v1/patentes/name')
api.add_resource(PatentesIdRouter, '/api/v1/patentes/id')

if __name__ == '__main__':
	app.run(debug=True)