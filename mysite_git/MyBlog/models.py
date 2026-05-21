from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User # Pour lier un stick à son découvreur
from geopy.geocoders import Nominatim

class Stick(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Brouillon (Dans la poche)'),
        ('Published', 'Découverte partagée'),
    ]
    
    # --- Identité du Stick ---
    title = models.CharField(max_length=200, verbose_name="Nom du spécimen")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found_sticks', verbose_name="Découvreur")
    likes = models.IntegerField(default=0, verbose_name="Nombre de Likes")
    
    # --- L'Image (Section 1.3 du devoir) ---
    # Nécessite d'installer Pillow (voir étape suivante)
    image = models.ImageField(upload_to='sticks/%Y/%m/%d/', blank=False, verbose_name="Preuve photographique")
    
    # --- Description ---
    body = models.TextField(verbose_name="Rapport d'observation")
    
    # --- La Stickmap (Section 2 du devoir) ---
    # On stocke les coordonnées pour la carte Leaflet/Folium plus tard
    location_name = models.CharField(max_length=100, blank=True, verbose_name="Lieu de découverte (Ville/Forêt)")
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    # --- Critères de Review (Concept Sticknation) ---
    handling_score = models.IntegerField(default=5, verbose_name="Prise en main (/10)")
    aesthetics_score = models.IntegerField(default=5, verbose_name="Esthétique (/10)")
    is_weaponizable = models.BooleanField(default=False, verbose_name="Potentiel offensif (Épée ?)")

    # --- Méta ---
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Draft")

    class Meta:
        ordering = ['-publish']
        verbose_name = "Stick"
        verbose_name_plural = "Sticks"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('MyBlog:post_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        # Si on a un nom de lieu mais pas de coordonnées
        if self.location_name and (not self.latitude or not self.longitude):
            try:
                # On initialise l'outil de géocodage (OpenStreetMap)
                geolocator = Nominatim(user_agent="sticknation_app")
                location = geolocator.geocode(self.location_name)
                
                if location:
                    self.latitude = location.latitude
                    self.longitude = location.longitude
                    print(f"📍 Succès : {self.location_name} trouvé à {self.latitude}, {self.longitude}")
                else:
                    print("⚠️ Lieu introuvable")
            except Exception as e:
                print(f"Erreur de géocodage : {e}")

        super().save(*args, **kwargs) # On laisse Django faire le reste de la sauvegarde


class Comment(models.Model):
    # J'ai changé 'post' en 'stick' pour la cohérence
    stick = models.ForeignKey(Stick, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Review by {self.name} on {self.stick}'
    

class MapLayer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la zone (ex: Forêt de Fontainebleau)")
    geojson_file = models.FileField(upload_to='maps/', verbose_name="Fichier GeoJSON")
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name