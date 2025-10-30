class Infra:
    def __init__(self,id_infra, length, infra_type, nb_houses,type_infra="aerien"):
        self.id_inra = id_infra
        self.length = length
        self.infra_type = infra_type
        self.nb_houses = nb_houses
        self.type_infra = type_infra

    def repair_infra(self):
        self.infra_type == "infra_intacte"
        return None
        
    def get_infra_difficuty(self):
        if self.infra_type == "infra_intacte":
            return 0
        else:
            if self.type_infra == "aerien":
                return ((self.length*500)*2)/self.nb_houses
            if self.type_infra == "semi-aerien":
                return ((self.length*750)*4)/self.nb_houses
            if self.type_infra == "fourreau":
                return ((self.length*900)*5)/self.nb_houses
    ## (cout * temps )/ nb
    
    def __radd__(self,other_objet):
        return self.get_infra_difficuty() + other_objet

    def __repr__(self):
        return self.id_inra  

    
if __name__ == "__main__":
    
    pass












































