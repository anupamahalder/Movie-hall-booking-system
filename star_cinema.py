class Star_Cinema:
    __hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)
    
    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list
