from Src.reference import reference


#
# Типы событий
#
class event_type(reference):
 
    @staticmethod
    def changed_block_period() -> str:
        """
            Событие изменения даты блокировки
        Returns:
            str: _description_
        """
        return "changed_block_period"

    @staticmethod
    def deleted_nomenclature() -> str:
        """
            Событие о удалении номенклатуры
        Returns:
            str: _description_
        """
        return "deleted_nomenclature"
    
    @staticmethod
    def change_item() -> str:
        """
            Событие о изменении item
        Returns:
            str: _description_
        """
        return "change_item"
    
    @staticmethod
    def add_item() -> str:
        """
            Событие о добавление item
        Returns:
            str: _description_
        """
        return "add_item"
    
    @staticmethod
    def create_turns_by_receipt() -> str:
        """
            Событие о формировании обороты по указанному рецепту
        Returns:
            str: _description_
        """
        return "create_turns_by_receipt"
    
    @staticmethod
    def build_debits_by_receipt() -> str:
        """
            Событие о формировании проводки списания по рецепту
        Returns:
            str: _description_
        """
        return "build_debits_by_receipt"
    
    