#  Projet de Planification du Raccordement Électrique des Bâtiments

##  Description du projet
À la suite d’une tempête ayant endommagé une partie du réseau électrique, plusieurs bâtiments ont été isolés.  
La mairie souhaite rétablir le réseau en **priorisant les zones où l’investissement permet de reconnecter le plus de bâtiments possible au coût minimal**.  

Ce projet propose une **méthode de planification algorithmique et géospatiale** permettant d’optimiser les travaux de réparation selon le coût, le temps et le nombre de bâtiments concernés.

🔗 **Lien du projet GitHub :** [https://github.com/TekoEvans/Projet_optimisation_operationelle](https://github.com/TekoEvans/Projet_optimisation_operationelle)

---

##  Membres du groupe
- **DEGBE TEKO EVANS**
- **BOUDJEKA ANIK**
- **NJANKOUO ABDEL AKIM**
- **NYALEU HERMINE**

---

##  Données et sources

Les données ont été fournies par la mairie et complétées à partir de nos propres demandes.

### Fichiers principaux :
- **`batiments.shp`** → positions et identifiants des bâtiments (`id_bat`, `nb_maison`).
- **`infrastructures.shp`** → tronçons d’infrastructures à réparer (`id_infra`, `longueur`, `état`).
- **`reseau_en_arbre.csv / xlsx`** → arborescence du réseau (relations, longueurs, coûts).
- **`infra.csv`** → type des infrastructures (aérien, semi-aérien, fourreau).
- **`batiments.csv`** → type de bâtiment et nombre réel de maisons.

### Nettoyage et préparation :
- Correction des incohérences dans le nombre de maisons.
- Jointure entre les shapefiles et les fichiers CSV.
- Filtrage des infrastructures à remplacer (577 tronçons).
- Identification de **85 bâtiments à raccorder**.

---

##  Métrique de priorisation

L’évaluation de la difficulté ne s’effectue **pas par infrastructure**, mais **par bâtiment**.  
Chaque bâtiment peut dépendre de plusieurs tronçons, et réparer un seul d’entre eux peut suffire à le reconnecter.

La métrique de difficulté globale d’un bâtiment est définie par :

**M_global = Σ ((C_i × T_i) / N_i)**

### Définition des variables
- **C_i** : coût de réparation d’une infrastructure.  
- **T_i** : temps estimé de réparation selon le type d’infrastructure.  
- **N_i** : nombre de maisons raccordées par l’infrastructure.  
- **M_global** : score total de difficulté du plan de raccordement.  

Un bâtiment est d’autant plus prioritaire que sa valeur **M_global** est faible., plus le bâtiment est **simple et prioritaire** à raccorder.

---

##  Algorithme proposé

### Étapes principales :
1. Catégoriser en **phase 0** les bâtiments déjà alimentés (aucune réparation nécessaire).  
2. Créer une **liste initiale** contenant les bâtiments à raccorder et une **liste vide** pour ceux réparés.  
3. Tant que la liste n’est pas vide :
   - Sélectionner le bâtiment avec la plus faible métrique \( M_i \).  
   - Réparer les infrastructures nécessaires à son raccordement.  
   - Ajouter le bâtiment réparé à la nouvelle liste.  
   - Mettre à jour les métriques des autres bâtiments (mutualisation des lignes).  
   - Retirer le bâtiment de la liste initiale.  

### Avantage :
Ce processus **itératif et adaptatif** permet de prioriser dynamiquement les bâtiments en tenant compte des réparations déjà effectuées.

---

##  Plan de raccordement proposé

L’analyse de la liste des bâtiments a révélé la présence d’infrastructures **critiques** telles qu’un **hôpital** et une **école**.  
Ces structures ont été **priorisées manuellement** en réduisant leur valeur de métrique **M_global = Σ ((C_i × T_i) / N_i)** afin d’assurer leur **raccordement en premier**.

Cette pondération manuelle du critère de criticité permet de garantir la **continuité des services vitaux** (santé, éducation, secours) tout en conservant une logique globale d’optimisation des ressources.

---

##  Résultats et visualisation

Une carte a été produite sous **QGIS** afin de représenter la **priorisation spatiale des bâtiments**.

| Couleur | Intervalle de la métrique | Niveau de priorité |
|----------|----------------------------|--------------------|
| 🔵 Bleu | 0 – 20 | Très prioritaire |
| 🟣 Violet | 20 – 40 | Prioritaire |
| 🟤 Pourpre | 40 – 60 | Moyenne priorité |
| 🔴 Rouge | 60 – 80 | Faible priorité |
| 🟥 Rouge foncé | 80 – 100 | Très faible priorité |

Les bâtiments bleus sont raccordés en premier, tandis que les rouges le sont en dernier.  
Cette classification par tranches de 20 unités offre une **lecture claire et hiérarchisée du territoire**, facilitant la planification opérationnelle des équipes sur le terrain.

---

##  Difficultés et solutions

### Principales difficultés :
- Données initiales incomplètes ou incohérentes.  
- Besoins du client évolutifs au cours du projet.  
- Manque d’uniformité des identifiants et des colonnes dans les fichiers sources.

### Solutions apportées :
- Multiplication des échanges avec la mairie pour clarifier les attentes.  
- Nettoyage et normalisation des fichiers (renommage des colonnes, correction des incohérences).  
- Recalcul complet des métriques après chaque ajustement.

---

##  Conclusion

Ce projet a permis d’élaborer un **plan de raccordement électrique optimisé**, fondé sur une métrique alliant **coût, temps et nombre de prises raccordées**.  
L’approche en graphe et l’algorithme itératif ont facilité une planification **dynamique et réaliste**, adaptable aux contraintes du terrain.  
La **mutualisation des infrastructures** a permis de réduire les coûts globaux, tandis que la **priorisation des bâtiments critiques**, comme l’hôpital, a renforcé l’impact social du plan.  
Ce modèle, à la fois **mathématiquement rigoureux et flexible**, constitue une base solide pour une **gestion intelligente et durable des réseaux électriques**.

---

##  Outils utilisés
- **Python** (Pandas)
- **QGIS** (visualisation et cartographie)
- **Excel / CSV**
- **VS Code**

---


 GitHub : [@TekoEvans](https://github.com/TekoEvans)

