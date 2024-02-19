from abstract_reference import abstract_reference
from ..argument_exception import argument_exception


#Еденица измерения 
class organization_model(abstract_reference):
    __INN: str = None
    #ИНН
    __BIK: str = None
    #БИк счет 
    __Schet: str = None
    #Счет 
    __type_of_organization: str = None
    #Вид организации
        
    


    def __init__(self, *args, INN, BIK, Schet, type_of_organization):
        super().__init__(*args)
        self.name=args
        self.INN=INN
        self.BIK=BIK
        self.Schet=Schet
        self.type_of_organization=type_of_organization


    @property
    def INN(self):
        return self.__INN
    
    @INN.setter
    def INN(self, value: str):
        """Инн

        Args:
            value (str): _description_

        Raises:
            argument_exception: _description_
        """
        
        if type(value)==str and len(value)==11:
            raise argument_exception("Не верно задан ИНН")
        self.__INN=value

    @property
    def BIK(self):
        return self.__BIK
    
    @BIK.setter
    def BIK(self, value: str):
        """Бик

        Args:
            value (str): _description_

        Raises:
            argument_exception: _description_
        """
        
        if type(value)==str and len(value)==11:
            raise argument_exception("Не верно задан БИК")
        self.__BIK=value

    @property
    def Schet(self):
        return self.__Schet
    
    @Schet.setter
    def Schet(self, value: str):
        """Счет

        Args:
            value (str): _description_

        Raises:
            argument_exception: _description_
        """
        
        if type(value)==str and len(value)==6:
            raise argument_exception("Не верно задан номер счета ")
        self.__Schet=value

    @property
    def type_of_organization(self):
        return self.__Schet
    
    @type_of_organization.setter
    def type_of_organization(self, value: str):
        """ тип организации

        Args:
            value (str): _description_

        Raises:
            argument_exception: _description_
        """
        
        if type(value)==str and len(value)<=5:
            raise argument_exception("Не верно задан тип организации ")
        self.__type_of_organization=value

