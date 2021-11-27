from business.patentesBusiness import PatentesBusiness
class PatentesController:

  patentesBusiness = PatentesBusiness()

  def __init__(self):
	  pass
    
  def getPatentes(self,patente):
    try:
      getPatente = self.patentesBusiness.filterPatentes(patente)
      return getPatente
    except Exception as error:
      return { 'code': 500, 'msg': 'Error servidor' }
  
  def getIdPatentes(self,idPatentes):
    try:
      getPatente = self.patentesBusiness.filterIdPatentes(idPatentes)
      return getPatente
    except Exception as error:
      print(error)
      return { 'code': 500, 'msg': 'Error servidor' }