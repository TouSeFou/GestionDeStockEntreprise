from django.db import models

# Model Fournisseur
class Fournisseur(models.Model):
    nFr = models.IntegerField()
    societe = models.CharField(max_length=150)
    tele = models.IntegerField()
    email = models.CharField(max_length=150)
    adresse = models.CharField(max_length=500)

    def __str__(self):
        return self.societe + " " + str(self.tele)

# Model Produit
class Produit(models.Model):
    refProd = models.IntegerField()
    description = models.TextField()
    marque = models.CharField(max_length=500)

    def __str__(self):
        return str(self.refProd) + " " + self.description + " " + self.marque

# Model Devis
class Devis(models.Model):
    nFr = models.IntegerField()
    nDevis = models.IntegerField()
    dateDevis = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.nDevis) + " " + str(self.dateDevis) + " " + str(self.montant)

# Model DetailDevis
class DetailDevis(models.Model):
    refProd = models.IntegerField()
    nDevis = models.IntegerField()
    prixProd = models.DecimalField(max_digits=10, decimal_places=2)
    qteProd = models.IntegerField()

    def __str__(self):
        return str(self.nDevis) + " " + str(self.refProd) + " " + str(self.qteProd) + " " + str(self.prixProd)

# Model Commande
class Commande(models.Model):
    nDevis = models.IntegerField()
    nFr = models.IntegerField()
    nCom = models.IntegerField()
    dateCom = models.DateField()
    montantCde = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.nCom) + " " + str(self.dateCom) + " " + str(self.montantCde)

# Model DetailCommande
class DetailCommande(models.Model):
    refProd = models.IntegerField()
    nCom = models.IntegerField()
    prixProd = models.DecimalField(max_digits=10, decimal_places=2)
    qteCmd = models.IntegerField()

# Model Facture
class Facture(models.Model):
    nFact = models.IntegerField()
    nCom = models.IntegerField()
    montantFact = models.DecimalField(max_digits=10, decimal_places=2)
    dateFacr = models.DateField()

# Model Livraison
class Livraison(models.Model):
    nFact = models.IntegerField()
    refProd = models.IntegerField()
    nBon = models.IntegerField()
    prixLiv = models.DecimalField(max_digits=10, decimal_places=2)
    qteLiv = models.IntegerField()
