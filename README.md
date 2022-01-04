# **Comment ranker sur Google ? Retroengineering des facteurs de ranking à l'exemple des annonces emploi**

![image](https://user-images.githubusercontent.com/32369680/148120962-42c49cc9-c98b-4f3d-b766-eadae22642c8.png)



## **Contexte**

En octobre 202 Google détenait En France, sur le marché du search une part de marché de 91,4% sur desktop (source statscounter GlobalStats).

Les statistiques actuelles montrent que 80% des consommateurs effectuent des recherches en ligne avant et pendant leurs achats et que les recherches par mots clés produisent 3 fois plus de trafic que les réseaux sociaux à eux seuls. 


Comme le digital est clé dans le processus d’achat, pour vendre, il faut drainer du trafic qualifié, donc être bien positionné sur les mots clés stratégiques.

**Corollaire** de cette assertion : connaître les mots clés stratégiques permet de bâtir la stratégie d’acquisition. Cette mine d’or sémantique, produite en continu « par la multitude » selon les termes mêmes de Nicolas Colin, alimente nos dispositifs de collecte et d’analyse bientôt automatiques pour proposer des indicateurs actionnables et fiables.

Très pragmatiquement il s’agit dont d’exploiter ce que les clients cherchent, dans quel volume et quelle position. Nous pré-supposons que dans une économie digitale, un acteur à considérer est une firme qui exerce une autorité digitale via:
· La performance des médias intégrés qui recouvre la position du site web directement contrôlé sur un ensemble de plusieurs milliers de mots clés décrivant le produit sur un territoire géographique donné ; ci-après « organic ranking »

· La performance des medias payés qui recouvre la promotion positive acquise grâce à la publicité payante afin de générer un trafic vers le point de vente physique ou le site marchand ; ci-après « paid search ranking »

· La performance des medias gagnés qui recouvre la notoriété positive et le trafic ciblé acquis dans le cadre des efforts de promotion éditoriale voire plus prosaiquement des échanges de liens ; ci-après « referral ranking »

· Avec ce triptyque « Organic, Paid, Referral » nous disposons donc des métriques homogènes pour détecter les acteurs (y compris les nouveaux entrants) et évaluer, de manière indiscutable, leur performance. Les milliers d’expressions réellement utilisées sur Google par les clients du produit ou service permettent demesurer très rapidement les sites qui trustent le trafic, donc les ventes.


## **Ce paradigme a d’autres atouts :**
Au paradigme de ce projet figurent donc **l'universalité du scope de données, la performance de la collecte et de leur traitement ;  la solidité du modèle d’analyse.** et tout particulièrement :
· Rapidité de mise en œuvre quelle que soit la langue ou le pays puisque nous recensons les mots clés et expressions de longue traine qui génèrent le trafic et donc l’activité sur une niche précise
· Solidité du modèle de détection des acteurs fondé sur la position détenue dans le top 100 des résultats de Google sur ce set de mots clés
· Sans intermédiaire et donc affranchi des problématiques de confidentialité ou de droit d’exploitation des données de base
· Immédiatement actionnable car permet de lister les firmes pas forcément identifiées avec lesquelles mettre en place un écosystème profitable à tous avec un plan d’action concret


## **Méthodo**

· 4000 requêtes pour sélectionner les mots clés et volumes cf https://github.com/caroheymes/jedha_final_project/blob/master/keywords_selection.ipynb

· Scraping  de toutes les url => position 100 cf https://github.com/caroheymes/jedha_final_project/tree/master/scrap

· Modélisations, sélection des features : 
cf https://github.com/caroheymes/jedha_final_project/blob/master/features_calculation.ipynb 

et  

https://github.com/caroheymes/jedha_final_project/blob/master/model_with_semantic_and_tech_attributes.ipynb


· Evaluation de la contribution des features avec Shapash
https://github.com/caroheymes/jedha_final_project/blob/master/understand_model_with__shapash.ipynb


## **Meilleurs modèles**

![image](https://user-images.githubusercontent.com/32369680/148119779-f1fd19e5-903a-4682-b24c-2f9f58add98e.png)


**Matrice de confusion : **

![image](https://user-images.githubusercontent.com/32369680/148119839-b0c583eb-7a25-400d-8167-1da4c23d1dca.png)

**Features importance:**

![image](https://user-images.githubusercontent.com/32369680/148119969-0bda1602-ad81-42fe-bb71-d59f00e1c4e4.png)

**A noter**
Nous avons utilisé le package shapash pour évaluer la contribution des features au modèle

![image](https://user-images.githubusercontent.com/32369680/148120126-1d70cb6a-6136-4bfb-8846-6a8ad6757694.png)


**Pour avancer sur le sujet**
Echangeons aussi sur linkedin !

https://www.linkedin.com/in/caroline-heymes


