from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy, argument_exception
from Src.reference import reference
from Src.Models.receipe_row_model import receipe_model
from Src.Models.recipe_model import recipts_model

#
# Класс для обработки данных. Начало работы приложения
#
class start_factory:
    __oprions: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings,
                 _storage: storage = None) -> None:
        
        exception_proxy.validate(_options, settings)
        self.__oprions = _options
        self.__storage = _storage
        
      
    
    def __save(self, key:str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """
       
        exception_proxy.validate(key, str)
        
        if self.__storage == None:
            self.__storage = storage()
            
        self.__storage.data[ key ] = items
        
        
                
    @property            
    def storage(self):
        """
             Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage
    
    @staticmethod
    def create_nomenclature():
        """
          Фабричный метод Создать список номенклатуры
        """
        
        result = []
        
        
        item1 = nomenclature_model("Мука пшеничная")
        item1.group = group_model.create_group()
        item1.unit = unit_model.create_killogram()

        item2 = nomenclature_model("Сахар")
        item2.group = group_model.create_group()
        item2.unit = unit_model.create_killogram()

        item3 = nomenclature_model("Сливочное масло")
        item3.group = group_model.create_group()
        item3.unit = unit_model.create_killogram()

        item4 = nomenclature_model("Яйца")
        item4.group = group_model.create_group()
        item4.unit = unit_model.create_killogram()

        item5 = nomenclature_model("Ванилин")
        item5.group = group_model.create_group()
        item5.unit = unit_model.create_gram()

        item6 = nomenclature_model("Куриное филе")
        item6.group = group_model.create_group()
        item6.unit = unit_model.create_killogram()

        item7 = nomenclature_model("Салат Романо")
        item7.group = group_model.create_group()
        item7.unit = unit_model.create_gram()

        item8 = nomenclature_model("Сыр пармезан")
        item8.group = group_model.create_group()
        item8.unit = unit_model.create_gram()

        item9 = nomenclature_model("Чеснок")
        item9.group = group_model.create_group()
        item9.unit = unit_model.create_gram()

        item10 = nomenclature_model("Белый хлеб")
        item10.group = group_model.create_group()
        item10.unit = unit_model.create_gram()

        item11 = nomenclature_model("Соль")
        item11.group = group_model.create_group()
        item11.unit = unit_model.create_gram()

        item12 = nomenclature_model("Перец")
        item12.group = group_model.create_group()
        item12.unit = unit_model.create_gram()

        item13 = nomenclature_model("Оливковое масло")
        item13.group = group_model.create_group()
        item13.unit = unit_model.create_mililitr()

        item14 = nomenclature_model("Лимонный сок")
        item14.group = group_model.create_group()
        item14.unit = unit_model.create_mililitr()

        item15 = nomenclature_model("Горчица дижонская")
        item15.group = group_model.create_group()
        item15.unit = unit_model.create_gram()

        item16 = nomenclature_model("Сахаоная пудра")
        item16.group = group_model.create_group()
        item16.unit = unit_model.create_gram()

        item17 = nomenclature_model("Корица")
        item17.group = group_model.create_group()
        item15.unit = unit_model.create_gram()

        item18 = nomenclature_model("Какао")
        item18.group = group_model.create_group()
        item18.unit = unit_model.create_gram()

        
        
        result.extend([item1, item2, item3, item4, item5, item6, item7, item8])
        result.extend([item9, item10, item11, item12, item13, item14, item15, item16, item17, item18])
        
        return result
    
    @staticmethod
    def create_recipts():
        num = start_factory.create_nomenclature()
        result = recipts_model("Рецепт")

        item1 = receipe_model(num[0], 100, unit_model.create_gram)
        item2 = receipe_model(num[1], 80, unit_model.create_gram)
        item3 = receipe_model(num[2], 70, unit_model.create_gram)
        item4 = receipe_model(num[3], 1, unit_model.create_shtuka)
        item5 = receipe_model(num[4], 5, unit_model.create_gram)

        result = recipts_model.recipt(item1)
        result = recipts_model.recipt(item2)
        result = recipts_model.recipt(item3)
        result = recipts_model.recipt(item4)
        result = recipts_model.recipt(item5)

        return result



    def create(self):
        """
           В зависимости от настроек, сформировать начальную номенклатуру

        Returns:
            _type_: _description_
        """
        
        result = []
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            
            # Формируем и зпоминаем номеклатуру
            result = start_factory.create_nomenclature()
            self.__save( storage.nomenclature_key(), result )

            #Запоминаем группы и еденицы измерения 
            group = list(set([i.group for i in result]))
            units = list (set([i.unit for i in result]))
            self.__save(storage.group_key(), group )
            self.__save(storage.unit_key(), units)

            #Запоминаем рецепт
            recipe = start_factory.create_recipts()
            self.__save(storage.recipe_key(), recipe)
      


        return result

        
    
    
        
        
        
        
    
    
    
    