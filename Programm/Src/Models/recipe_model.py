from Src.reference import reference
from Src.Models.receipe_row_model import receipe_model
from Src.exceptions import exception_proxy


#
#Модель для описания рецепта 
#
class recipts_model(reference):
    __recipt = []


    def __init__(self, name):
        super.__init__(name)


    @property
    def recipt(self):
        """вывод для рецепта 

        Returns:
            _type_: _description_
        """
        return self.__recipt
    
    @recipt.setter
    def recipt(self, value: receipe_model):
        """Ввод строки рецепта 

        Args:
            value (receipe_model): _description_
        """
        exception_proxy.validate(value, receipe_model)
        self.__recipt.append(value)



        
        
