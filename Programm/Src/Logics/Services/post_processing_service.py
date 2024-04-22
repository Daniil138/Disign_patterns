from Src.Logics.Services.service import service
from Src.Models.nomenclature_model import nomenclature_model
from Src.Storage.storage import storage
from Src.exceptions import error_proxy, exception_proxy, argument_exception




#
#Класс обработки номенклатуры 
#
class post_processing_service(service):
    _nomenclature: nomenclature_model
    _data: list


    def __init__(self, nomenclature: nomenclature_model ) -> None:
                  
        exception_proxy.validate(nomenclature, nomenclature_model)
        self._nomenclature = nomenclature
   
    
    def clean_recipt(self):
        storager = storage
        flag = False
        for recipt in storager.data[ storage.receipt_key() ]:
            flag += recipt.delete_nomenclatura(self._nomenclature)

        return flag

                
        

        



  






        
    
    def handle_event( self, event_type: str ):
        """ Обработать события"""

        super().handle_event(event_type)
    