from django.db import models
from decimal import*
import decimal
# Create your models here.

class Bin(models.Model):
	bin_id = models.IntegerField(default = 1, verbose_name = 'Номер')
	bin_adress = models.CharField(max_length = 200, verbose_name = 'Адрес')
	#Объём рабочей внутренности контейнера в литрах
	bin_volume = models.IntegerField(default = 200)
	#средний темп заполняемости контейнера, выраженный в процентах от общего объёма в день
	#bin_pace = models.DecimalField(max_digits = 4, decimal_places = 2)
	def __str__(self):
		return str(self.bin_adress)
	#возвращает самое новое измерение
	def bin_get_last_fill(self):
		if self.measurement_set.count():
			return self.measurement_set.order_by('measurement_date').last().measurement_get_percentage()
		else:
			return 0.
	#возвращает число контейнеров
	def bin_get_number(self):
		return Bin.objects.count()
	#возвращает 5 последних измерений
	def bin_get_last_five_measurements(self):
		result = self.measurement_set.all().order_by('-measurement_date')[:5]
		return result
	#считает средний темп заполняемости за всё время в процентах
	def bin_get_fill_pace_percentage(self):
		count = 0
		summa = 0.
		bin_measurement_set = self.measurement_set.all().order_by('measurement_date')
		measurement = bin_measurement_set.first()
		for next_measurement in bin_measurement_set[1:]:
			if next_measurement.measurement_cells_inside > measurement.measurement_cells_inside:
				pace_per_period = (next_measurement.measurement_cells_inside - measurement.measurement_cells_inside) / next_measurement.measurement_cells_maximum
				pace_per_day = pace_per_period / (next_measurement.measurement_date - measurement.measurement_date).days
				pace_in_percentage = pace_per_day * 100
				count = count + 1
				summa = summa + float(pace_in_percentage)
				measurement = next_measurement
		if count:
			return float("{0:.2f}".format(summa / count))
		else:
			return 0




class Measurement(models.Model):
	measurement_bin = models.ForeignKey(Bin)
	measurement_date = models.DateTimeField()
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

class Event(models.Model):
	event_bin = models.ForeignKey(Bin)
	event_date = models.DateField()
	event_description = models.CharField(max_length = 500)


#Выполняя makemigrations, вы говорите Django, что внесли 
#некоторые изменения в ваши модели и хотели бы сохранить их в миграции.


#Внесите изменения в модели (в models.py).
#Выполните python manage.py makemigrations чтобы создать миграцию для ваших изменений
#Выполните python manage.py migrate чтобы применить изменения к базе данных.

#new_bin = Bin( ... )
#new_bin.save       явно сохраняет новый элемент в БД
