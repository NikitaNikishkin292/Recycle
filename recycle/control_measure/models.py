from django.db import models
from decimal import*
# Create your models here.

class Bin(models.Model):
	bin_id = models.IntegerField(default = 1)
	bin_adress = models.CharField(max_length = 200)
	#Объём рабочей внутренности контейнера в литрах
	bin_volume = models.IntegerField(default = 200)
	#средний темп заполняемости контейнера, выраженный в процентах от общего объёма в день
	#bin_pace = models.DecimalField(max_digits = 4, decimal_places = 2)
	def __str__(self):
		return str(self.bin_adress)
	#возвращает последнее измерениие
	def bin_get_last_fill(self):
		return self.measurement_set.last().measurement_get_percentage()
	def bin_get_number(self):
		return Bin.objects.count()


class Measurement(models.Model):
	measurement_bin = models.ForeignKey(Bin)
	measurement_date = models.DateField()
	#число клеточек, соответствующее уровню заполненности контейнера
	measurement_cells_inside = models.DecimalField(max_digits = 3, decimal_places = 1)
	#максимально возможное число клеточек
	measurement_cells_maximum = models.DecimalField(max_digits = 3, decimal_places = 1)
	def __str__ (self):
		return str(self.measurement_date)
	def measurement_get_percentage(self):
		x = (self.measurement_cells_inside / self.measurement_cells_maximum) * 100
		g =float("{0:.2f}".format(x))
		return g

#Выполняя makemigrations, вы говорите Django, что внесли 
#некоторые изменения в ваши модели и хотели бы сохранить их в миграции.


#Внесите изменения в модели (в models.py).
#Выполните python manage.py makemigrations чтобы создать миграцию для ваших изменений
#Выполните python manage.py migrate чтобы применить изменения к базе данных.

#new_bin = Bin( ... )
#new_bin.save       явно сохраняет новый элемент в БД
