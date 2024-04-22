from Src.Logics.Services.post_processing_service import post_processing_service
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage


import unittest

class postprocessingservice_test(unittest.TestCase):

    def test_check_delete_nomenclature_in_recipt(self):
        #Подготовка
        options = settings_manager() 
        start = start_factory(options.settings)
        start.create()
        storages = storage()
        nomenclature = storages.data[ storage.nomenclature_key() ][0]
        prosess = post_processing_service(nomenclature)
        prosess.clean_recipt

        #Действие 
        prosess = post_processing_service(nomenclature)


        #проверка
        assert prosess.clean_recipt

        

