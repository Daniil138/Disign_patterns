import unittest

from service_nomenclatures import service_nomenclatures
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage
from Src.settings_manager import settings_manager


class service_nomenclatures_test(unittest.TestCase):


    #
    #Проверить нахождение номенклатуры 
    #
    def test_find_nomenclatura(self):
        #Подготовка

        options = settings_manager() 
        start = start_factory(options.settings)
        start.create()
        service = service_nomenclatures(start.storage.data)
        nomenclatura_id = start.storage.data[storage.nomenclature_key()][1].id


        #Действие 
        result = service.get_nomenclatura(nomenclatura_id)

        #Проверка 
        assert result!= None
    

    def test_get_nomenclatures(self):
        #Подготовка
        options = settings_manager() 
        start = start_factory(options.settings)
        start.create()
        service = service_nomenclatures(start.storage.data)

        #Действие
        data = service.get_nomenclatures()

        #Проверка
        assert len(data)!=0

    def test_path_nomeclatures(self):
        #Подготовка
        options = settings_manager() 
        start = start_factory(options.settings)
        start.create()
        service = service_nomenclatures(start.storage.data)
        nomenclatura = start.storage.data[storage.nomenclature_key()][1]


        #Действие
        result = service.path_nomenclatures(nomenclatura)

        #Провеерка 
        assert result
    
    def test_put_nomeclatures(self):
        #Подготовка
        options = settings_manager() 
        start = start_factory(options.settings)
        start.create()
        service = service_nomenclatures(start.storage.data)
        nomenclatura = start.storage.data[storage.nomenclature_key()][1]
        lens = len(start.storage.data[storage.nomenclature_key()])


        #Действие
        service.put_nomenclatures(nomenclatura)

        #Провеерка 
        assert len(service.ger_nomenclatures())>lens
           
    def test_put_nomeclatures(self):
        #Подготовка
        options = settings_manager() 
        start = start_factory(options.settings)
        start.create()
        service = service_nomenclatures(start.storage.data)
        nomenclatura = start.storage.data[storage.nomenclature_key()][1]
        lens = len(start.storage.data[storage.nomenclature_key()])


        #Действие
        result = service.delete_nomenclatures(nomenclatura)

        #Провеерка 
        assert len(service.ger_nomenclatures())<lens
        assert result




