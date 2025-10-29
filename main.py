import pandas as pd
network_df = pd.read_excel("reseau_en_arbre.xlsx")
broken_network = network_df[network_df['infra_type']== "a_remplacer"]
print(broken_network["id_batiment"].values)