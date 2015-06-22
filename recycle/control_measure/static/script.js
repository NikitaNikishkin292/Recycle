$(document).ready(function() {
	//обработка нажатия на кнопку "добавить контейнер"
	$('#new_bin').click(function(event){
		$('#new_bin_info').removeClass('hidden_menu');
		$('#new_bin_info').addClass('visible_menu');
	});

	//обработчики кнопки "выгрузить"
	$('.unload_button').click(function(event){
		$('#new_unload_info').removeClass('hidden_menu');
		$('#new_unload_info').addClass('visible_menu');
	});

	
	//обработчики кнопки Эдобавить измерение
	$('.add_button').click(function(event){
		$('#new_measure_info').removeClass('hidden_menu');
		$('#new_measure_info').addClass('visible_menu');
	});

	//обработчики кнопки Эдобавить измерение в процентах
	$('.add_button_percent').click(function(event){
		$('#new_measure_info_percent').removeClass('hidden_menu');
		$('#new_measure_info_percent').addClass('visible_menu');
	});

	$('.unload_button_percent').click(function(event){
		$('#new_unload_info_percent').removeClass('hidden_menu');
		$('#new_unload_info_percent').addClass('visible_menu');
	});

	$('.add_event').click(function(event){
		$('#new_event_info').removeClass('hidden_menu');
		$('#new_event_info').addClass('visible_menu');
	});

	//обработка кнопок "сейчас"
	$('.current_date').click(function(event){
			var now = new Date();
			var day = now.getDate();
			var mon = now.getMonth() + 1;
			var year = now.getFullYear();
			var hours = now.getHours()
			var minutes = now.getMinutes();
			var current_time = hours + ":" + minutes;
			var current_date = year + "-" + mon + "-" + day;
			//alert(current_date);
			$('#date_of_measurement').attr("value", current_date);
			$('#time_of_measurement').attr("value", current_time);
			$('#date_of_measurement').attr("placeholder", "");
			$('#time_of_measurement').attr("placeholder", "");
	});

	$('#current_date_percent').click(function(event){
		var now = new Date();
		var day = now.getDate();
		var mon = now.getMonth() + 1;
		var year = now.getFullYear();
		var hours = now.getHours()
		var minutes = now.getMinutes();
		var current_time = hours + ":" + minutes;
		var current_date = year + "-" + mon + "-" + day;
		//alert(current_date);
		$('#date_of_measurement_percent').attr("value", current_date);
		$('#time_of_measurement_percent').attr("value", current_time);
		$('#date_of_measurement_percent').attr("placeholder", "");
		$('#time_of_measurement_percent').attr("placeholder", "");
	});

	$('#button_unload_current').click(function(event){
			var now = new Date();
			var day = now.getDate();
			var mon = now.getMonth() + 1;
			var year = now.getFullYear();
			var hours = now.getHours();
			var minutes = now.getMinutes();
			var current_date = year + "-" + mon + "-" + day;
			var current_time = hours + ":" + minutes;
			//alert(current_date);
			$('#date_of_upload').attr("value", current_date);
			$('#time_of_upload').attr("value", current_time);
			$('#date_of_upload').attr("placeholder", "");
			$('#time_of_upload').attr("placeholder", "");
	});

	$('#button_unload_current_percent').click(function(event){
			var now = new Date();
			var day = now.getDate();
			var mon = now.getMonth() + 1;
			var year = now.getFullYear();
			var hours = now.getHours();
			var minutes = now.getMinutes();
			var current_date = year + "-" + mon + "-" + day;
			var current_time = hours + ":" + minutes;
			//alert(current_date);
			$('#date_of_upload_percent').attr("value", current_date);
			$('#time_of_upload_percent').attr("value", current_time);
			$('#date_of_upload_percent').attr("placeholder", "");
			$('#time_of_upload_percent').attr("placeholder", "");
	});

	$('#button_event_current').click(function(event){
			var now = new Date();
			var day = now.getDate();
			var mon = now.getMonth() + 1;
			var year = now.getFullYear();
			var current_date = year + "-" + mon + "-" + day;
			//alert(current_date);
			$('#date_of_event').attr("value", current_date);
			$('#date_of_event').attr("placeholder", "");
	});

	$('span.measure_error').each(function() {
    		var val = parseFloat($(this).text());
    		console.log(val);
    		if (val > 0.0) {
    			$(this).closest('div').css('color', 'green');
    		}
    		else {
    			$(this).closest('div').css('color', 'red');
    		}
    	});
});