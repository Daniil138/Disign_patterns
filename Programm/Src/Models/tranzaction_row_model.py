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

    
    def __init__(self, _nomenclature: nomenclature_model, _stock: str, _operation: bool, _unit: unit_model, _period: datetime):
        """

        Args:
            _nomenclature (nomenclature_model): _description_
            _stock (str): _description_
            _operation (bool): _description_
            _unit (unit_model): _description_
            _period (datetime): _description_
        """
        exception_proxy.validate(_nomenclature, reference)
        exception_proxy.validate(_unit, reference)
        exception_proxy.validate(_stock, str)
        exception_proxy.validate(_operation, bool)
    
         
        self.__nomenclature = _nomenclature
        self.__operation = _operation
        self.__unit = _unit
        self.__period = _period
        self.__stock = _stock
        
        super().__init__( f"{_nomenclature.name}, {_stock}, {_operation}, {_unit.name}, {_period} ")
    
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
            Колличество

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
    
    @property    
    def operation(self):
        """
           Операция 

        Returns:
            _type_: _description_
        """
        return self.__operation   
    
    @property    
    def stock(self):
        """
           Операция 

        Returns:
            _type_: _description_
        """
        return self.__stock

    @property    
    def period(self):
        """
           Операция 

        Returns:
            _type_: _description_
        """
        return self.__period
        
        
    