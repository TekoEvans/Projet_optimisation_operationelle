import pandas as pd
from models.building import Building
from models.infra import Infra


network_df = pd.read_excel("reseau_en_arbre.xlsx")
# Reseau des batiments a remplacer
broken_network = network_df[network_df['infra_type']== "a_remplacer"]

# Notre reseau actuels contiens des erreur sur le nombre de maison 
# supprimons la colones nb_maisons

broken_network = broken_network.drop(columns=["nb_maisons"])

# faisons une jointure avec la nouvelle données fournie par le clients sur les batiments
new_data_building = pd.read_csv("batiments.csv")
new_broken_network = broken_network.merge(new_data_building, on="id_batiment", how="left")


# faisons une nouvelle jointure avec la nouvelle données fournie par le clients sur les type d'infrastructure

new_data_infra = pd.read_csv("infra.csv")

# renomons d'abord le nom de la colone infra_id pour corespondre et permettre la jointure
new_broken_network =  new_broken_network.rename(columns={"infra_id":"id_infra"})
new_broken_network = new_broken_network.merge(new_data_infra, on="id_infra", how="left")




if __name__=="__main__":
    # print(new_data_infra)
    # print(new_broken_network)
   
    list_object_of_building_broken = []

# On regroupe par id_batiment
for id_building, group in new_broken_network.groupby("id_batiment"):
    list_infras = []
    for _, row in group.iterrows():
        infra = Infra(
            id_infra=row["id_infra"],
            length=row["longueur"],
            infra_type=row["infra_type"],
            nb_houses=row["nb_maisons"],
            type_infra=row["type_infra"],
           
        )
        list_infras.append(infra)
    building = Building(id_building, list_infras,row["type_batiment"])
   
    list_object_of_building_broken.append(building)

 #le nombre de tout les batiments a reparer 
print(len(list_object_of_building_broken))  

buildings = list_object_of_building_broken[:]
building_by_priority = []
while buildings :
    low_difficulty_building = min(buildings)
    for infra in low_difficulty_building.list_infras:
        infra.repair_infra()
    building_by_priority.append(low_difficulty_building)
    buildings.remove(low_difficulty_building)
# voici la liste des batiment par odre de prioritée
print(building_by_priority)  

# creeeons un colone prioritée
building_by_priority_df = pd.DataFrame({"batiments":building_by_priority, "priority":range(len(building_by_priority))})
building_by_priority_df.to_excel('final_building_by_priority.xlsx', index=False, columns=["batiments", "priority"])



     

