from django.contrib import admin

from .models import *
admin.site.register(Commande)
admin.site.register(DetailCommande)
admin.site.register(DetailDevis)
admin.site.register(Devis)
admin.site.register(Facture)
admin.site.register(Fournisseur)
admin.site.register(Livraison)
admin.site.register(Produit)

