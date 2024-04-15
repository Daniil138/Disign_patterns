from Src.Logics.convert_factory import convert_factory
from Src.Logics.process_factory import process_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.exceptions import argument_exception, exception_proxy, operation_exception
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.receipe_model import receipe_model
from Src.Models.storage_model import storage_model
from Src.Models.receipe_row_model import receipe_row_model
from Src.Storage.storage import storage
from Src.settings_manager import settings_manager

from datetime import datetime
import json

class storage_service:
    __data = []
    options = settings_manager()
    options.open("settings.json")
    _block_period = options._settings.block_period


    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data
        
    def __processing(self, data: list) -> list:
        """
            Сформировать обороты
        Args:
            data (list): _description_

        Returns:
            list: _description_
        """
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Подобрать процессинг    
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn  )
    
        # Обороты
        turns =  processing().process( data )
        return turns
            
        
    # Набор основных методов    


    def __make_turns_by_blocked_stop_period(self, data_real_turn: list):
        """Метод для добавления оборотов из сохраненных к отсортированным 

        Args:
            data_real_turn (list): _description_

        Returns:
            _type_: _description_
        """
        exception_proxy.validate(data_real_turn, list)

        storage_data = storage()
        data_turn_blocked = storage_data.data[ storage.turn_key() ]
        data = {}


        for item in data_turn_blocked:
            key = (item.nomenclature.id, item.storage.id)
            data[key] = item
            #Снчала из созраненных оборотов добавляются все 

        #Затем если такие обороты есть в полученных, то мы складываем их значения, если нет то просто добавляем 
        for item in data_real_turn:
            key = (item.nomenclature.id, item.storage.id)
            if key in data.keys():
                data[key].value+=item.value
            else:
                data[key] = item
        
        return data.items()
    
    def __make_turns_by_blocked_stop_period_nomenclature(self, data_real_turn: list):
        """Метод для добавления оборотов из сохраненных к отсортированным по одной номенклатуре 

        Args:
            data_real_turn (list): _description_

        Returns:
            _type_: _description_
        """
        exception_proxy.validate(data_real_turn, list)

        storage_data = storage()
        data_turn_blocked = storage_data.data[ storage.turn_key() ]
        data = []
        key0 = (data_real_turn[0].nomenclature.id,  data_real_turn[0].storage.id)


        for item in data_turn_blocked:
            key = (item.nomenclature.id, item.storage.id)
            if key0 == key:
                item.value += data_real_turn[0].value
                data.append(item)

        if len(data) == 0:
            return data_real_turn


        
        return data



        
    def create_turns(self, start_period: datetime, stop_period:datetime = None ) -> list:
        """
            Получить обороты за период
        Args:
            start_period (datetime): Начало
            stop_period (datetime): Окончание

        Returns:
            list: обороты за период
        """

        if stop_period == None:
            stop_period = start_period
            start_period =  self._block_period
            
            exception_proxy.validate(start_period, datetime)
            exception_proxy.validate(stop_period, datetime)
            
            if start_period > stop_period:
                raise argument_exception("Некорректно переданы параметры!")
            
            # Фильтруем      
            prototype = storage_prototype(  self.__data )  
            filter = prototype.filter_by_period( start_period, stop_period)
            
            data = self.__processing( filter. data )
            self.create_blocked_turns(self._block_period)
            result = self.__make_turns_by_blocked_stop_period(data)
            return result

        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Фильтруем      
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter_by_period( start_period, stop_period)
        
        return self.__processing( filter. data )
            
        
    def create_turns_by_nomenclature(self, start_period: datetime, *args) -> list:
        """
            Получить обороты за период по конкретной номенклатуры
        Args:
            start_period (datetime): Начало
            stop_period (datetime): Окончание
            nomenclature (nomenclature_model): Номенклатуры

        Returns:
            list: Обороты
        """
        if len(args)==0:
            raise argument_exception("Не передана номенклатура")
        
        if len(args)==1:
            stop_period = start_period
            start_period = self._block_period
            nomenclature = args[0]

            exception_proxy.validate(start_period, datetime)
            exception_proxy.validate(stop_period, datetime)
            exception_proxy.validate(nomenclature, nomenclature_model)

            if start_period > stop_period:
                raise argument_exception("Некорректно переданы параметры!")
            

            # Фильтруем      
            prototype = storage_prototype(  self.__data )  
            filter = prototype.filter_by_period( start_period, stop_period)
            filter = filter.filter_by_nomenclature( nomenclature )

            if not filter.is_empty:
                raise operation_exception(f"Невозможно сформировать обороты по указанным данных: {filter.error}")
            
            data = self.__processing( filter. data )
            self.create_blocked_turns(self._block_period)
            result = self.__make_turns_by_blocked_stop_period_nomenclature(data)

            return result
            



        if len(args)==2:
            stop_period = args[0]
            nomenclature = args[1]

        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        exception_proxy.validate(nomenclature, nomenclature_model)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Фильтруем      
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter_by_period( start_period, stop_period)
        filter = filter.filter_by_nomenclature( nomenclature )
        if not filter.is_empty:
            raise operation_exception(f"Невозможно сформировать обороты по указанным данных: {filter.error}")
            
        return self.__processing( filter. data )    
    
    def create_turns_only_nomenclature(self, nomenclature: nomenclature_model) -> list:
        """
            Получить обороты по номенклатуре
        Args:
            nomenclature (nomenclature_model): _description_

        Returns:
            list: Обороты
        """
        exception_proxy.validate(nomenclature, nomenclature_model)
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter_by_nomenclature( nomenclature )
        if not filter.is_empty:
            raise operation_exception(f"Невозможно сформировать обороты по указанным данных: {filter.error}")
         
        return self.__processing( filter. data )   
    
    def create_turns_by_receipt(self, receipt: receipe_model) -> list:
        """
            Сформировать обороты по указанному рецепту
        Args:
            receipt (receipe_model): _description_

        Returns:
            list: _description_
        """
        exception_proxy.validate(receipt, receipe_model)
        
        if len(receipt.consist) == 0:
            raise operation_exception("Переданный рецепт некорректный. Не содержит в себе список номенклатуры!")
        
        # Отфильтровать по рецепту
        transactions = []
        filter =  storage_prototype(  self.__data )
        for item in receipt.rows():
            filter =  filter.filter_by_nomenclature( item.nomenclature )
            if filter.is_empty:
                for transaction in filter.data:
                    transactions.append( transaction )
                    
            filter.data = self.__data        
            
        return self.__processing( transactions )     
            
    
    def build_debits_by_receipt(self, receipt: receipe_model) -> list:
        """
            Сформировать проводки списания по рецепту
        Args:
            receipt (receipe_model): _description_

        Returns:
            list: _description_
        """
        exception_proxy.validate(receipt, receipe_model)
        
        if len(receipt.consist) == 0:
            raise operation_exception("Переданный рецепт некорректный. Не содержит в себе список номенклатуры!")
        
        turns = self.create_turns_by_receipt(receipt)
        if len(turns) <= 0:
            raise operation_exception("По указанному рецепту не найдеты обороты!")
        
        if len(receipt.rows()) > len(turns):
            raise operation_exception("Невозможно сформировать список транзакций для списания т.к. нет достаточно остатков!")
        
        # Формируем список проводок на списание
        processing = process_factory().create( process_factory.debit_key() )
        transactions = processing().process( receipt.rows() )
        key = storage.storage_transaction_key()
        
        data = storage().data[ key ]
        for transaction in transactions:
            data.append ( transaction )

    def create_blocked_turns(self,  block_period:datetime ):
        """
            Сделать обороты до периода блокировки 
        Args:
            start_period (datetime): Начало
            stop_period (datetime): Окончание

        Returns:
            list: обороты за период
        """
        start_period = datetime.strptime("1900-01-01", "%Y-%m-%d")
        exception_proxy.validate(block_period, datetime)
        
        if start_period > block_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Фильтруем      
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter_by_period( start_period, block_period)
        data = storage()
        process = self.__processing( filter. data )
        if len(process) < 0:
            raise operation_exception("Некорректно почситана процесс")

        
        data.data[ data.turn_key() ] = process
    
    # Набор основных методов        
    
    def data(self) -> list:
        """
            Получить отфильтрованные данные
        Returns:
            list: _description_
        """
        return self.__data    
        
    @staticmethod        
    def create_response( data: list, app):
        """"
            Сформировать данные для сервера
        """
        if app is None:
            raise argument_exception("Некорректно переданы параметры!")

        # Преоброзование
        data = convert_factory().serialize( data )
        json_text = json.dumps( data, sort_keys = True, indent = 4,  ensure_ascii = False)  
   
        # Подготовить ответ    
        result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = "application/json; charset=utf-8"
        )
        
        return result