#Les variables représentant un produit(Beurre 250g)
nom=("Beurre")
prix_unitaire_euro= 3
quantite_en_stock=("120pieces")

#Affichege en console les informations du beurre de manière formatée.
print(nom,prix_unitaire_euro,quantite_en_stock)

#Ajout des produits

nom_Lait=("Lait")
prix_unitaire_euro_litre_= 1.5
quantite_en_stock_bouteilles=("100 bouteilles")

nom_kiwi=("kiwi")
prix_unitaire_euro_kilo_= 8.5
quantite_en_stock_kilo=("20 kilo")
print(nom_Lait,prix_unitaire_euro_litre_,quantite_en_stock_bouteilles)
print(nom_kiwi,prix_unitaire_euro_kilo_,quantite_en_stock_bouteilles)

#saisir la quantité de produits qu'il utilisateur souhaite acheter et mettre le stock à jour.
input("Saisiez les types et la quantite de produit qu'il vous vous desire " )

#Mettre a jour le prix de beurre qui a subi l’inflation de 10%
inflation= 1.1
prix_unitaire_apres_inflation = float(prix_unitaire_euro*inflation)
print("correction du prix du produit")
print(nom,prix_unitaire_apres_inflation,quantite_en_stock)




