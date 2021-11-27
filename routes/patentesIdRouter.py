from flask_restful import Resource, Api
from flask import Flask, jsonify, request, Response, make_response
from controller.patentesController import PatentesController

class PatentesIdRouter(Resource):

    def __init__(self):
        pass
    
    def post(self):
        try:
            patentes = request.get_json()
            if(patentes["id"]==""):
                return make_response(jsonify({"msg":"Todos los datos son obligatorios"}),400)
            patentesController = PatentesController()
            patenteData = patentesController.getIdPatentes(patentes["id"])
            return make_response(jsonify(patenteData),200)
        except Exception as error:
            print("_______ error routes")
            print(error)
            return make_response(jsonify({"msg":"Error al ingresar los datos"}),409)