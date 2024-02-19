import unittest
from Src.models.unit_model import unit
from Src.models.organization_model import organization_model


class test_model(unittest.TestCase):
    def test_check_unit_model(self):
        #Подготовка
        u = unit()

        #действие
        u1 = u("gramm",1)
        u2 = u("kilo",1000,u1)

        #Проверка 
        assert u1 

    def test_check_organization_model(self):
        #Подготовка
        organiz = organization_model()

        #Действие 
        organiz1 = organiz("name", "12121212121", "12121212121", "123456", "OOO" )





