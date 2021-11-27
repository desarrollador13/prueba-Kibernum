class PatentesBusiness:

    def __init__(self):
	      pass

    def filterPatentes(self, patente):
      try:
        data = [
            {"patentes": "AAAA000", "id": 1},
            {"patentes": "AAAA001", "id": 2},
            {"patentes": "ZZZZ999", "id": 3}
        ]
        patenteList = list(filter(lambda patentes: patentes["patentes"] == patente, data))
        if(len(patenteList)==0):
          return { "msg":"no hay registros en la busqueda", "patente":patente }
        return patenteList[0]
      except Exception as error:
        print("____________  Error Businness")
        print(error)
        return { "msg":"no hay registros en la busqueda", "patente":patente }

    def filterIdPatentes(self, idPatente):
      try:
        data = [
              {"patentes": "AAAA000", "id": 1},
              {"patentes": "AAAA001", "id": 2},
              {"patentes": "ZZZZ999", "id": 3}
          ]
        patenteList = list(filter(lambda patentes: patentes["id"] == idPatente, data))
        if(len(patenteList)==0):
            return { "msg":"no hay registros en la busqueda", "id":idPatente }
        return patenteList[0]
      except Exception as error:
        print("____________  Error Businness")
        print(error)
        return { "msg":"no hay registros en la busqueda", "id":idPatente }