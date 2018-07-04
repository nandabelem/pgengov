from django.db import models


class Categoria(models.Model):
	categoria_id = models.AutoField(primary_key=True)
	categoria_nome = models.CharField(max_length=200)
	
	def __str__(self):
		return self.categoria_nome

class Instituicao(models.Model):
	instituicao_id = models.AutoField(primary_key=True)
	instituicao_nome = models.CharField(max_length=200)
	instituicao_categoria = models.ForeginKey(Categoria,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.instituicao_nome

class Estado(models.Model):
	estado_id = models.AutoField(primary_key=True)
	estado_nome = models.CharField(max_length=200)
	estado_sigla = models.CharField(max_length=2)
	
	def __str__(self):
		return self.estado_nome

class Cidade(models.Model):
	cidade_id = models.AutoField(primary_key=True)
	cidade_nome = models.CharField(max_length=200)
	cidade_estado = models.ForeginKey(Estado,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.cidade_nome

class Sede(models.Model):
	sede_id = models.AutoField(primary_key=True)
	sede_nome = models.CharField(max_length=200)
	sede_latitude = models.BigIntegerField()
	sede_longitude = models.BigIntegerField()
	sede_instituicao = models.ForeginKey(Instituicao,on_delete=models.CASCADE)
	sede_cidade = models.ForeginKey(Cidade,on_delete=models.CASCADE)
	sede_estado = models.ForeginKey(Estado,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.sede_nome