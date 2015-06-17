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

	$('.current_date').click(function(event){
			var now = new Date();
			var day = now.getDate();
			var mon = now.getMonth() + 1;
			var year = now.getFullYear();
			var hours = now.getHours()
			var current_date = year + "-" + mon + "-" + day;
			//alert(current_date);
			$('#date_of_measurement').attr("value", current_date);
		});

	//обработчики кнопки Эдобавить измерение
	$('.add_button').click(function(event){
		$('#new_measure_info').removeClass('hidden_menu');
		$('#new_measure_info').addClass('visible_menu');
	});
});