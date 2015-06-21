from django.db import models
from decimal import*
import decimal
import datetime
# Create your models here.

class Type(models.Model):
	type_short_name = models.CharField(max_length = 20, null='True')
	type_name = models.CharField(max_length = 20, verbose_name = "Тип контейнера")
	type_description = models.CharField(max_length = 100, default = "bla bla bla", verbose_name = "Описание")
	type_length = models.IntegerField(default = 145, verbose_name = "Длина")
	type_width = models.IntegerField(default = 105, verbose_name = "Ширина")
	type_heigth = models.IntegerField(default = 165, verbose_name = "Высота")
	def __str__(self):
		return str(self.type_name)
	def type_get_volume(self):
		return (self.type_heigth * self.type_width * self.type_length) / 1000

class Bin(models.Model):
	bin_id = models.IntegerField(default = 1, verbose_name = 'Номер')
	bin_adress = models.CharField(max_length = 200, verbose_name = 'Адрес')
	#Объём рабочей внутренности контейнера в литрах
	#bin_volume = models.IntegerField(default = 200)
	#тип контейнера
	bin_type = models.ForeignKey(Type, null = 'True')
	#средний темп заполняемости контейнера, выраженный в процентах от общего объёма в день
	#bin_pace = models.DecimalField(max_digits = 4, decimal_places = 2)
	def __str__(self):
		return str(self.bin_adress)

	#возвращает самое новое измерение
	def bin_get_last_fill(self):
		if self.measurement_set.count():
			return self.measurement_set.order_by('measurement_date').last().measurement_percentage
		else:
			return 0.
			return 0.

	#возвращает измерения
	def bin_get_last_five_measurements(self):
		result = self.measurement_set.all().order_by('-measurement_date')
		return result

	def bin_get_average_pace_per_hour(self):
		measure_set = self.measurement_set.all().order_by('measurement_date')
		if measure_set.count() > 1:
			time_summ = measure_set.last().measurement_date - measure_set.first().measurement_date
			time_summ = time_summ.days * 24 + time_summ.seconds / 3600
			summ = 0.
			mes_first = measure_set.first()
			for mes_second in measure_set[1:]:
				if mes_second.measurement_percentage - mes_first.measurement_percentage > 0:
					summ += float(mes_second.measurement_percentage - mes_first.measurement_percentage)
				mes_first = mes_second
			result = float("{0:.2f}".format(summ / time_summ))
			return result
		else:
			return 0

	def bin_get_average_pace_per_day(self):
		measure_set = self.measurement_set.all().order_by('measurement_date')
		if measure_set.count() > 1:
			time_summ = measure_set.last().measurement_date - measure_set.first().measurement_date
			time_summ = time_summ.days * 24 + time_summ.seconds / 3600
			summ = 0.
			mes_first = measure_set.first()
			for mes_second in measure_set[1:]:
				if mes_second.measurement_percentage - mes_first.measurement_percentage > 0:
					summ += float(mes_second.measurement_percentage - mes_first.measurement_percentage)
				mes_first = mes_second
			result = float("{0:.2f}".format((summ * 24) / time_summ))
			return result
		else:
			return 0

	






class Measurement(models.Model):
	measurement_bin = models.ForeignKey(Bin, verbose_name = "Контейнер")
	measurement_date = models.DateTimeField(verbose_name = "Дата замера")
	#заполненность контейнера в процентах
	measurement_percentage = models.DecimalField(max_digits = 3, decimal_places = 1, default = 50, verbose_name = "Процент")
	#число клеточек, соответствующее уровню заполненности контейнера
	measurement_cells_inside = models.DecimalField(max_digits = 3, decimal_places = 1, null = 'True', blank = 'True')
	#максимально возможное число клеточек
	measurement_cells_maximum = models.DecimalField(max_digits = 3, decimal_places = 1, null = 'True', blank = 'True')
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
