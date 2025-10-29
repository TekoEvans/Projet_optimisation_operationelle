class Infra:
    def __init__(self,id_infra, length, infra_type, nb_houses):
        self.id_inra = id_infra,
        self.length = length,
        self.infra_type = infra_type,
        self.nb_houses = nb_houses

    def repair_infra(self):
        self.infra_type == "infra_intacte"
        return None
        
    def get_infra_difficuty(self):
        if self.infra_type == "infra_intacte":
            return 0
        else:
            return self.length/self.nb_houses
    ## (cout * temps )/ nb
    
    def __radd__(self,other_objet):
        self.get_infra_difficuty + other_objet

    def __repr__(self):
        print(self.id_inra)    

    
if __name__ == "__main__":
    
    pass












































