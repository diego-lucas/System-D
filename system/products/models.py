from django.db import models

class Distributor(models.Model):

	name = models.CharField('Nome', max_length=100)
	logo = models.ImageField(upload_to='distributor/images', verbose_name="Imagem", null=True, blank=True)
	created_at = models.DateTimeField("Criado em", auto_now_add=True)
	updated_at = models.DateTimeField("Atualizado em", auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Distribuidora'
		verbose_name_plural = 'Distribuidoras'
		ordering = ['name']

class Products(models.Model):

	categories = [
		('Sem categoria', 'Sem Categoria'),
		('Bebidas', 'Bebidas'),
		('Alimentos', 'Alimentos'),
		('Higiene', 'Higiene'),
		('Roupas', 'Roupas'),
		('Eletrodomésticos', 'Eletrodomestico')
	]

	name = models.CharField('Nome', max_length=100, blank=True)
	slug = models.SlugField('Atalho', primary_key=True)
	image = models.ImageField(upload_to='products/images', verbose_name="Imagem", null=True, blank=True)
	category = models.CharField('Categorias', max_length=100, choices=categories, default='sem categoria')
	price = models.DecimalField('Preço', max_digits=6, decimal_places=2, blank=True)
	distributor = models.ForeignKey(Distributor, verbose_name='Distribuidora', related_name='distributor', on_delete=models.CASCADE, null=True)

	created_at = models.DateTimeField("Criado em", auto_now_add=True)
	updated_at = models.DateTimeField("Atualizado em", auto_now=True)

	def get_absolute_url(self):
		return '/produtos/' + self.slug

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['name']