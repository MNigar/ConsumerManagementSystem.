class User:
    def __init__(self, _consumername, _consumersurname,_consumerusername,_consumerpassword):
     self.consumername=_consumername
     self.consumersurname=_consumersurname
     self.consumerusername=_consumerusername
     self.consumerpassword=_consumerpassword
    def showData(self):
      print(f"{self.consumername} / {self.consumersurname} / {self.consumerusername} / {self.consumerpassword}")
