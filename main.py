import pandas as pd
from models.building import Building
from models.infra import Infra






network_df = pd.read_excel("reseau_en_arbre.xlsx")
broken_network = network_df[network_df['infra_type']== "a_remplacer"]
broken_building_id =  set(broken_network["id_batiment"].values)





if __name__=="__main__":
   
    list_object_of_building = []

# On regroupe par id_batiment
for id_batiment, group in broken_network.groupby("id_batiment"):
    infras = []
    for _, row in group.iterrows():
        infra = Infra(
            id_infra=row["infra_id"],
            length=row["longueur"],
            infra_type=row["infra_type"],
            nb_houses=row["nb_maisons"],
            # type_infra=row["infra_type"]  # ou autre si tu as un champ spécifique
        )
        infras.append(infra)
    building = Building(id_building=id_batiment, list_infras=infras)
    list_object_of_building.append(building)
for b in list_object_of_building:
    print(b.get_building_difficulty())
#     for i in b.list_infras:
#         print("  ",i) 


     

