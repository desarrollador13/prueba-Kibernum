from flask_restful import Resource, Api
from flask import Flask, jsonify, request, Response, make_response
from controller.patentesController import PatentesController
from cerberus import Validator

class PatentesRouter(Resource):

    def __init__(self):
        pass
    
    def post(self):
        try:
            schema = {'patentes': {'required': True, 'type': 'string'}}
            isValid = Validator(schema)
            #if(isValid.validate(request.get_json()))
            patentes = request.get_json()
            if(patentes["patentes"]==""):
                return make_response(jsonify({"msg":"Todos los datos son obligatorios"}),400)
            patentesController = PatentesController()
            patenteData = patentesController.getPatentes(patentes["patentes"])
            return make_response(jsonify(patenteData),200)
        except Exception as error:
            return make_response(jsonify({"msg":"Error al ingresar los datos"}),409)