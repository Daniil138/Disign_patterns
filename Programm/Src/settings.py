

class settings:
    __first_name = ""
    __INN = ""
    __coresp_schet = None
    __BIK = None
    __name_service = ""
    __type_prop = ""


    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def INN(self):
        return self.__INN
    
    @property
    def coresp_schet(self):
        return self.__coresp_schet
    
    @property
    def BIK(self):
        return self.__BIK
    
    @property
    def name_service(self):
        return self.__name_service
    
        
    @property
    def type_prop(self):
        return self.__type_prop
    
    
    
    
    @first_name.setter
    def first_name(self, value: str):
        """
        Получение значения first_name и проверка на тип 
        """
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()

    @INN.setter
    def INN(self, value: str):
        """
        Получение значения INN и проверка на тип и длинну 
        """
        if (not isinstance(value, int)) and len(str(value))==11:
            raise Exception("Некорректный аргумент!")
        
        self.__INN = value
    
    @coresp_schet.setter
    def coresp_schet(self, value: str):
        """
        Получение значение кореспонденского счета  и проверка на тип и длинну 
        """
        if (not isinstance(value, int)) and len(str(value))==11:
            raise Exception("Некорректный аргумент!")
        
        self.__coresp_schet = value


    @BIK.setter
    def BIK(self, value: str):
        """
        Получение значение BIK и проверка на тип и длинну 
        """
        if (not isinstance(value, int)) and len(str(value))==11:
            raise Exception("Некорректный аргумент!")
        
        self.__BIK = value

    @name_service.setter
    def name_service(self, value: str):
        """
        Получение вида услуги  и проверка на тип 
        """
        if (not isinstance(value, str)) :
            raise Exception("Некорректный аргумент!")
        
        self.__name_service = value.strip()

    @type_prop.setter
    def typ_prop(self, value: str):
        """
        Получение вида собственности  и проверка на тип и длинну 
        """
        if (not isinstance(value, str)) and len(value)<=5 :
            raise Exception("Некорректный аргумент!")
        
        self.__type_prop = value.strip()

    
        
        