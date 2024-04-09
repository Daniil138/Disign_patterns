from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.Logics.report_factory import report_factory
from Src.Logics.start_factory import start_factory
from datetime import datetime
from Src.Logics.storage_service import storage_service
from Src.Models.nomenclature_model import nomenclature_model
from Src.Logics.convert_factory import convert_factory
from Src.exceptions import error_proxy, argument_exception
import uuid




class service_nomenclatures():

    __data=[]
    

    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data

    
    def get_nomenclatura(self, nomenclatura_id: uuid ):
        """ПОиск номенклатуры по айди

        Args:
            nomenclatura_id (uuid): _description_

        Returns:
            _type_: _description_
        """
        if nomenclatura_id == None:
            return error_proxy.create_error_response("Необходимо передать параметр номенклатуры")

        nomenclatures = self.__data[  storage.nomenclature_key()  ]
        
        for item in nomenclatures:
            if item.id == nomenclatura_id:

                return item   

        return False
    
    def ger_nomenclatures(self):
        """Получение списка ноиенклатур
        Returns:
            _type_: _description_
        """

        return self.__data[  storage.nomenclature_key()  ]   

        
    

    def path_nomenclatures(self,  nomenclatura: nomenclature_model):
        if nomenclatura == None:
            return error_proxy.create_error_response("Необходимо передать  номенклатуру")

        
        for  index, item  in enumerate( self.__data[  storage.nomenclature_key()  ]):
            if item.id == nomenclatura.id:
                self.__data[  storage.nomenclature_key()  ][index] = nomenclatura
                return True
        return False     

    def put_nomenclatures(self,  nomenclatura: nomenclature_model):
        if nomenclatura == None:
            return error_proxy.create_error_response("Необходимо передать  номенклатуру")
        
        self.__data[  storage.nomenclature_key()  ].append(nomenclatura)

    def delete_nomenclatures(self,  nomenclatura: nomenclature_model):
        if nomenclatura == None:
            return error_proxy.create_error_response("Необходимо передать  номенклатуру")

        
        for index, item  in enumerate( self.__data[  storage.nomenclature_key()  ]):
            if item.id == nomenclatura.id:
                self.__data[  storage.nomenclature_key()  ].pop(index)
                return True
        return False
        
        
         
    


