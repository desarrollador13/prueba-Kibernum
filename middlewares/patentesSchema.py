from marshmallow import Schema, fields

class PatentesSchema(Schema):
    patentes = fields.Str(required=True)
