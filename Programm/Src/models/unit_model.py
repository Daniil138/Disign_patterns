from abstract_reference import abstract_reference
from argument_exception import argument_exception


#Еденица измерения 
class unit(abstract_reference):
    #Коэффициент пересчета 
    __recount_index: int = 1
    #Базвоя еденица 
    __base_unit = None
        
    


    def __init__(self, *args, recount_index, base_unit):
        super().__init__(*args)
        self.name = args 
        self.recount_index= recount_index
        self.__base_unit = base_unit

        if self.__base_unit == None:
            self.__base_unit = self


    
    @property
    def recount_index(self):
        return self.__recount_index
    
    @recount_index.setter
    def recount_index(self, value: int):
        """коэффициент пресчета 

        Args:
            value (int): _description_
        """
        
        if type(value)==int:
            raise argument_exception("Не верно задан коэффициент пересчета")
        self.__recount_index=value
        
    @property
    def base_unit(self):
        return self.base_unit

        
    

      


    

    