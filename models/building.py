class  Building:
    def __init__(self, id_building, list_infras,type_batiment):
        self.id_building = id_building
        self.list_infras = list_infras
        self.type_batiment = type_batiment

    def get_building_difficulty(self):
         if self.type_batiment == "hôpital":
             return -float('inf')
         elif self.type_batiment == "école":
             return -float('inf')+1
         else:
            return sum(self.list_infras)
    
    def __lt__(self,other_objet):
        return self.get_building_difficulty() < other_objet.get_building_difficulty()

    def __repr__(self):
        return self.id_building

    def __str__(self):
        return self.id_building

if __name__ == "__main__":
    pass