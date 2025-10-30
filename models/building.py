class  Building:
    def __init__(self, id_building, list_infras):
        self.id_building = id_building
        self.list_infras = list_infras

    def get_building_difficulty(self):
         return sum(self.list_infras)
    
    def __lt__(self,other_objet):
        return self.get_building_difficulty() < other_objet.get_building_difficulty()

    def __repr__(self):
        return self.id_building

    def __str__(self):
        return self.id_building

if __name__ == "__main__":
    pass