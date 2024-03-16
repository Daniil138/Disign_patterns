from Src.reference import reference


#
#Модель склада 
#
class stock_model(reference):

    def create_default_stock():

        """Фбричный метод. Создать склад по умолчанию

        Returns:
            _type_: _description_
        """
        item = stock_model("г.Иркутск, ул.Карла Маркса, д.100")
        return item
                                