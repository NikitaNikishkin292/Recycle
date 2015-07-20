from django.db import models
from decimal import*
import decimal
import pytz
from pytz import timezone
import datetime
from datetime import datetime, timedelta
tz = 'Europe/Moscow'
# Create your models here.
# coding=utf8 

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

	#возвращает измерения
	def bin_get_last_five_measurements(self):
		result = self.measurement_set.all().order_by('-measurement_date')
		return result

	#объём контейнера
	def bin_get_volume(self):
		return self.bin_type.type_get_volume()

	#генерирует скорость заполнения в литрах/час для счёта
	def bin_generate_volume_pace(self):
		measure_set = self.measurement_set.all().order_by('measurement_date')
		if measure_set.count() > 1:
			time_summ = measure_set.last().measurement_date - measure_set.first().measurement_date
			time_summ = time_summ.days * 24 + time_summ.seconds / 3600
			summ = 0.
			mes_first = measure_set.first()
			for mes_second in measure_set[1:]:
				if mes_second.measurement_volume - mes_first.measurement_volume > 0:
					summ += float(mes_second.measurement_volume - mes_first.measurement_volume)
				mes_first = mes_second
			result = summ / time_summ
			return result
		else:
			return 0

	def bin_generate_volume_pace_of_date(self, our_date):
		measure_set = self.measurement_set.all().order_by('measurement_date')
		if measure_set.count() > 1:
			summ = 0.
			last_meas = 0
			mes_first = measure_set.first()
			for mes_second in measure_set[1:]:
				if mes_second.measurement_date == our_date:
					last_meas = mes_first
					break
				if mes_second.measurement_volume - mes_first.measurement_volume > 0:
					summ += float(mes_second.measurement_volume - mes_first.measurement_volume)
				mes_first = mes_second
			time_summ = last_meas.measurement_date - measure_set.first().measurement_date
			time_summ = time_summ.days * 24 + time_summ.seconds / 3600
			if time_summ:
				result = summ / time_summ
				return result
			else:
				return 0
		else:
			return 0


	#Средний темп заполняемости в %/час за всё время для вывода
	def bin_get_average_pace_per_hour_output(self):
		result = float("{0:.1f}".format( ( self.bin_generate_volume_pace() / self.bin_type.type_get_volume() ) * 100) )
		return result

	#средний темп заполняемости в %/день за всё время для вывода
	def bin_get_average_pace_per_day_output(self):
		result = float("{0:.1f}".format( (self.bin_generate_volume_pace() / self.bin_type.type_get_volume() * 2400 )))
		return result
		
	#Текущая заполненность в литрах для счёта
	def bin_get_current_fill_litres (self):
		last_measure = self.measurement_set.all().order_by('measurement_date').last()
		if last_measure:
			pace_per_hour_litres = self.bin_generate_volume_pace()
			current_server_time = datetime.utcnow()
			current_client_time = timezone(tz).fromutc(current_server_time)
			#date_of_last_measure = pytz.utc.localize(last_measure.measurement_date) - timedelta(hours = 3)
			time_delta = current_client_time - last_measure.measurement_date
			time_delta = time_delta.days * 24 + time_delta.seconds / 3600
			fill_now = float(last_measure.measurement_volume) + time_delta * pace_per_hour_litres
			return fill_now
		else:
			return 0

	#Текущая заполненность в процентах для вывода
	def bin_get_current_fill_percentage (self):
		result = (self.bin_get_current_fill_litres() / self.bin_type.type_get_volume()) * 100
		return float("{0:.1f}".format(result))


	def bin_get_upload_date (self):
		current_server_time = datetime.utcnow()
		current_client_time = timezone(tz).fromutc(current_server_time)
		if self.bin_generate_volume_pace():
			hours_number = (self.bin_type.type_get_volume() - self.bin_get_current_fill_litres()) / self.bin_generate_volume_pace()
			term = timedelta(hours = hours_number)
			upload_date = current_client_time + term
			return upload_date.date()

	def bin_predict_fill_of_date(self, dt):
		measure_set = self.measurement_set.all().order_by('measurement_date')
		if measure_set:
			delta = pytz.utc.localize(dt) - measure_set.last().measurement_date
			if delta > timedelta(0):
				delta = delta.days * 24 + delta.seconds / 3600
				volume_inside =  self.bin_generate_volume_pace_of_date(dt) * delta + measure_set.last().measurement_volume
				return volume_inside

	def bin_get_events(self):
		return self.event_set.all().order_by('-event_date')





class Measurement(models.Model):
	measurement_bin = models.ForeignKey(Bin, verbose_name = "Контейнер")
	measurement_date = models.DateTimeField(verbose_name = "Дата замера")
	measurement_volume = models.IntegerField(verbose_name = "Объём в литрах", blank = 'True', null = 'True')
	measurement_error = models.DecimalField(max_digits = 3, decimal_places = 1, verbose_name = "Ошибка", blank = 'True', null = 'True')
	#заполненность контейнера в процентах
	measurement_percentage = models.DecimalField(max_digits = 4, decimal_places = 1, default = 50, verbose_name = "Процент")
	measurement_mass = models.DecimalField(max_digits = 3, decimal_places = 1, verbose_name = 'Масса PET', blank = 'True', null = 'True')
	measurement_bag = models.IntegerField(verbose_name = 'Номер мешка', blank = 'True', null = 'True')
	#число клеточек, соответствующее уровню заполненности контейнера
	#measurement_cells_inside = models.DecimalField(max_digits = 3, decimal_places = 1, null = 'True', blank = 'True')
	#максимально возможное число клеточек
	#measurement_cells_maximum = models.DecimalField(max_digits = 3, decimal_places = 1, null = 'True', blank = 'True')
	def __str__ (self):
		return str(self.measurement_date)
	def measurement_get_percentage(self):
		x = (self.measurement_volume / self.measurement_bin.bin_get_volume()) * 100
		g =float("{0:.1f}".format(x))
		return g

class Event(models.Model):
	event_bin = models.ForeignKey(Bin)
	event_date = models.DateField()
	event_description = models.CharField(max_length = 500)


class Bag(models.Model):
	bag_id = models.IntegerField(primary_key = True, verbose_name = 'Номер мешка')
	bag_type = models.ManyToManyField(Type, verbose_name = 'Тип контейнера')
	BAG_STATUS = (
			(1, "В контейнере"),
			(2, "На складе полный"),			
			(3, "На складе пустой"),
		)
	bag_status = models.IntegerField(verbose_name = 'Статус мешка', choices = BAG_STATUS, default = 2)

	def __str__ (self):
		return str(self.bag_id)

#Выполняя makemigrations, вы говорите Django, что внесли 
#некоторые изменения в ваши модели и хотели бы сохранить их в миграции.


#Внесите изменения в модели (в models.py).
#Выполните python manage.py makemigrations чтобы создать миграцию для ваших изменений
#Выполните python manage.py migrate чтобы применить изменения к базе данных.

#new_bin = Bin( ... )
#new_bin.save       явно сохраняет новый элемент в БД
