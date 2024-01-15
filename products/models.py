import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

#-> Todos los que hereden de models son una tabla en la base de datos
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) #12345678.00
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Esto es una forma de guardar las url automaticamente
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Produc, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

def set_slug(sender, instance, *args, **kwargs): #Generar las url automaticamente

    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:5])
            )
        instance.slug = slug 

pre_save.connect(set_slug, sender=Product) #-> Guardar automaticamente las url de los productos con el nombre del producto