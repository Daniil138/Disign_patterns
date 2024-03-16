from Src.reference import reference
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.exceptions import exception_proxy
from Src.Models.stock_model import stock_model
import datetime 

#
# Класс описание одной строки рецепта
#
class tranzaction_row_model(reference):
    __stock: stock_model
    __nomenclature: nomenclature_model = None
    __operation: bool = 0
    __unit: unit_model = None
    __quantity: int = 0
    __period: datetime

    
    def __init__(self, _nomenclature: nomenclature_model, _operation: bool, _unit: unit_model, _period: datetime):
        """

        Args:
            _nomenclature (nomenclature_model): Объект номенклатура
            _size (int): Размер части
            _unit (unit_model): Объект единица измерения
        """
        exception_proxy.validate(_nomenclature, reference)
        exception_proxy.validate(_unit, reference)
         
        self.__nomenclature = _nomenclature
        self.__operation = _operation
        self.__unit = _unit
        
        super().__init__( f"{_nomenclature.name} , {_unit.name} ")
    
    @property  
    def nomenclature(self):
        """
            Номенклатура
        Returns:
            _type_: _description_
        """
        return self.__nomenclature
    
    
    @property
    def quantity(self):
        """
            Размер

        Returns:
            _type_: _description_
        """
        return self.__quantity
    
    
    @quantity.setter
    def qauntity(self, value: int):
        self.__quantity = value
    

    @property    
    def unit(self):
        """
           Единица измерения

        Returns:
            _type_: _description_
        """
        return self.__unit    
        
    