from django.db import models
from django.contrib.auth.models import User, UserManager
from decimal import*
import decimal
import pytz
from pytz import timezone
import datetime
import time
from datetime import datetime, timedelta
tz = 'Europe/Moscow'
# Create your models here.
# coding=utf8 
import logging
logger = logging.getLogger(__name__)

def my_view(request, arg1, arg):
    if bad_mojo:
        logger.error('Something went wrong!')

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
	BIN_STATUS = (
		(True, 'Включен в вывоз'),
		(False, 'Не включен в вывоз'),
	)
	bin_status = models.BooleanField(choices = BIN_STATUS, verbose_name = 'Статус контейнера', default = False)
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

	def bin_generate_volume_pace_test(self):
		measure_set_init = self.measurement_set.all().order_by('measurement_date')
		size = measure_set_init.count()
		if size > 10:
			begin = size - 10
		else:
			begin = 0
		measure_set = measure_set_init[begin:]
		logger.info(measure_set)
		if measure_set.count() > 1:
			logger.info(measure_set_init.last())
			logger.info(measure_set.first().measurement_date)
			time_summ = measure_set_init.last().measurement_date - measure_set.first().measurement_date
			logger.info(time_summ)
			time_summ = time_summ.days * 24 + time_summ.seconds / 3600
			logger.info(time_summ)
			summ = 0.
			mes_first = measure_set.first()
			for mes_second in measure_set[1:]:
				if mes_second.measurement_volume - mes_first.measurement_volume > 0:
					summ += float(mes_second.measurement_volume - mes_first.measurement_volume)
				mes_first = mes_second
			result = summ / time_summ
			logger.info("New: ")
			logger.info(summ)
			logger.info(time_summ)
			return result
		else:
			return 0

	def bin_generate_volume_pace_of_date(self, our_date):
		measure_set = self.measurement_set.all().order_by('measurement_date')
		if measure_set.count() > 1:
			summ = 0.
			last_meas = 0
			mes_first = measure_set.first()
			#logger.info(mes_first)
			if our_date > mes_first.measurement_date:
				for mes_second in measure_set[1:]:
					if mes_second.measurement_date >= our_date:
						last_meas = mes_first
						break
					if mes_second.measurement_volume - mes_first.measurement_volume > 0:
						summ += float(mes_second.measurement_volume - mes_first.measurement_volume)
					mes_first = mes_second
				if last_meas == 0:
					last_meas = self.measurement_set.all().order_by('measurement_date').last()
				time_summ = last_meas.measurement_date - measure_set.first().measurement_date
				time_summ = time_summ.days * 24 + time_summ.seconds / 3600
				if time_summ:
					result = summ / time_summ
					return result
				else:
					return 0
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
			hours_number = ((self.bin_type.type_get_volume() * 0.9 - self.bin_get_current_fill_litres())) / self.bin_generate_volume_pace()
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

	

	def bin_get_ordered_bins_list(self):
		dict_for_sort = []
		early_stage_bins = []
		for a_bin in Bin.objects.all():
			if a_bin.bin_get_upload_date():
				dict_for_sort.append([a_bin.bin_get_upload_date(), a_bin])
			else:
				early_stage_bins.append(a_bin)
		def getDate(item):
			return item[0]
		dict_for_sort.sort(key = getDate)
		result = []
		for pair in dict_for_sort:
			result.append(pair[1])
		for bins in early_stage_bins:
			result.append(bins)
		return result

	def bin_get_ordered_bins_list_filtered(value):
		dict_for_sort = []
		early_stage_bins = []
		for a_bin in Bin.objects.filter(bin_status = value):
			if a_bin.bin_get_upload_date():
				dict_for_sort.append([a_bin.bin_get_upload_date(), a_bin])
			else:
				early_stage_bins.append(a_bin)
		def getDate(item):
			return item[0]
		dict_for_sort.sort(key = getDate)
		result = []
		for pair in dict_for_sort:
			result.append(pair[1])
		for bins in early_stage_bins:
			result.append(bins)
		return result

	def bin_get_bins_not_included_into_unloadings():
		return Bin.bin_get_ordered_bins_list_filtered(False)


class Measurement(models.Model):
	measurement_bin = models.ForeignKey(Bin, verbose_name = "Контейнер")
	measurement_date = models.DateTimeField(verbose_name = "Дата замера")
	measurement_volume = models.IntegerField(verbose_name = "Объём в литрах", blank = 'True', null = 'True')
	measurement_error = models.DecimalField(max_digits = 4, decimal_places = 1, verbose_name = "Ошибка", blank = 'True', null = 'True')
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
	bag_in_bin = models.OneToOneField(Bin, verbose_name = "В контейнере", null = 'True', blank = 'True')

	def bag_get_types(self):
		return self.bag_type.all()

	def __str__ (self):
		return str(self.bag_id)

class Unload(models.Model):
	unload_id = models.IntegerField(primary_key = True, verbose_name = 'id выгрузки')
	unload_date = models.DateTimeField(verbose_name = 'Дата выгрузки')
	unload_bins_list = models.ManyToManyField(Bin, verbose_name = 'Выгружаемые контейнеры', blank = 'True', null = 'True')
	#unload_bags_list = models.ManyToManyField(Bag, verbose_name = 'Необходимые мешки', blank = 'True')
	UNLOAD_STATUS = (
		(0, 'Осуществленный'),
		(1, 'Запланированный'),
	)
	unload_status = models.IntegerField(verbose_name = 'Статус выгрузки', choices = UNLOAD_STATUS, default = 1)
	unload_time_spent = models.IntegerField(verbose_name = 'Минут потрачено', blank = 'True', null = 'True')
	unload_money_spent = models.IntegerField(verbose_name = 'израсходовано денег', blank = 'True', null = 'True')

	def __str__(self):
		return str(self.unload_date)

	def unload_get_bins(self):
		return self.unload_bins_list.all()


class City_Pace(models.Model):
	city_pace_date = models.DateField(verbose_name = 'Дата')
	city_pace_value = models.DecimalField (max_digits = 6, decimal_places = 3, verbose_name = 'Темп м3/сутки')

	def __str__(self):
		return str(self.city_pace_date)

	def city_pace_count_rest():
		current_server_time = datetime.utcnow()
		#current_client_date = timezone(tz).fromutc(current_server_time)
		if City_Pace.objects.all().order_by('city_pace_date').last():
			last_date_counted = City_Pace.objects.all().order_by('city_pace_date').last().city_pace_date
			mytime = datetime.strptime('2130','%H%M').time()
			last_date_counted = datetime.combine(last_date_counted, mytime)
		else:
			#aware - абсолютное время, так как берётся из БД
			last_date_counted = Measurement.objects.all().order_by('measurement_date').first().measurement_date
			current_server_time = timezone(tz).fromutc(current_server_time)
		#logger.info(last_date_counted)
		#logger.info(current_client_date)
		if current_server_time.date() != last_date_counted.date():
			for a_date in range((current_server_time - last_date_counted).days):
				new_pace = 0.
				logger.info(last_date_counted + timedelta(days = a_date + 1))
				for a_bin in Bin.objects.all():
					new_date = last_date_counted + timedelta(days = a_date + 1)
					new_date = timezone('UTC').fromutc(new_date)
					logger.info(new_date)
					new_pace += a_bin.bin_generate_volume_pace_of_date(new_date)
					#logger.info(a_bin.bin_adress)
					#logger.info(a_bin.bin_generate_volume_pace_of_date(last_date_counted + timedelta(days = a_date + 1)))
				logger.info(float("{0:.2f}".format(new_pace * 24 / 1000)))
				new_city_pace = City_Pace(city_pace_date = last_date_counted + timedelta(days = a_date + 1), city_pace_value = new_pace * 24 / 1000)
				new_city_pace.save()

class Demos_Measurement(models.Model):
	demos_measurement_user = models.ForeignKey(User)
	demos_measurement_date = models.DateField(verbose_name = "Дата замера")
	demos_measurement_percentage = models.DecimalField(max_digits = 4, decimal_places = 1, default = 50, verbose_name = "Процент")
	demos_measurement_comment = models.CharField(max_length = 1000)
	demos_measurement_bin = models.ForeignKey(Bin, verbose_name = "Измеренный контейнер", blank = 'True', null = 'True')

	def __str__(self):
		return str(self.demos_measurement_date)

class Demos(User):
	demos_sochnik_count = models.IntegerField(verbose_name = 'Сочников накполено', default = 0)
	demos_avatar = models.ImageField(upload_to="avatars")
	demos_bins = models.ManyToManyField(Bin, verbose_name = 'Выгружаемые контейнеры', blank = 'True', null = 'True')
	objects = UserManager()

	def demos_get_messages(self):
		inbox = self.demos_message_set.all().order_by('-demos_message_date')
		return inbox

	

	#def delete(self, *args, **kwargs):
	#	for a_bin in self.unload_get_bins():
	#		a_bin.bin_status = 'False'
	#		a_bin.save()
	#	super(Unload, self).delete()

class Demos_Message(models.Model):
	demos_message_user = models.ForeignKey(Demos, verbose_name = "Пользователь")
	demos_message_date = models.DateField(verbose_name = "Дата сообщения")
	demos_message_content = models.CharField(verbose_name = "Сообщение", max_length = 500)
	MESSAGE_STATUS = (
		(0, 'Измерение'),
		(1, 'Поздравление'),
		(2, 'Вывоз'),
	)
	demos_message_status = models.IntegerField(verbose_name = "Тип сообщения", choices = MESSAGE_STATUS)

	def demos_get_message_icon_class(self):
		if self.demos_message_status == 0:
			return "glyphicon glyphicon-pencil aligned"
		else:
			if self.demos_message_status == 1:
				return "glyphicon glyphicon-thumbs-up aligned"
			else:
				return "glyphicon glyphicon-transfer aligned"

	def __str__(self):
		return str(self.demos_message_content)

#Выполняя makemigrations, вы говорите Django, что внесли 
#некоторые изменения в ваши модели и хотели бы сохранить их в миграции.


#Внесите изменения в модели (в models.py).
#Выполните python manage.py makemigrations чтобы создать миграцию для ваших изменений
#Выполните python manage.py migrate чтобы применить изменения к базе данных.

#new_bin = Bin( ... )
#new_bin.save       явно сохраняет новый элемент в БД
