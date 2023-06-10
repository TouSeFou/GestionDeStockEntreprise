from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import *
admin.site.register(Commande)
admin.site.register(DetailCommande)
admin.site.register(DetailDevis)
admin.site.register(Devis)
admin.site.register(Facture)
admin.site.register(Fournisseur)
admin.site.register(Livraison)
admin.site.register(Produit)

admin.site.unregister(User)
admin.site.unregister(Group)

