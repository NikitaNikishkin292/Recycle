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



	var menuList = ["#bin_module", "#measurements_module", "#speed_module", "#history_module"];
    	var bufferList = [$("#bin_module").detach(), $('#measurements_module'), $('#speed_module').detach(), $('#history_module').detach()];
    	function setActiveDivId (id_string) {
    		if (!($('div').is(id_string))) {
    			var this_index = 0;
    			for (var j = 0; j < menuList.length; j++) {
    				if (id_string == menuList[j])
    					this_index = j;
    			}
	    		for (var i = 0; i < menuList.length; ++i) {
	    			if ($('div').is(menuList[i])) {
	    				bufferList[i] = $(menuList[i]).detach();
	    				bufferList[this_index].appendTo('body');
	    			}
	    		}
	    	}
    	};
    	//var measurements_module_buffer = ;
    	//var	bin_buffer = $("#bin_module");
    	$('#bin_link').click(function(e){
	    		//measurements_module_buffer = $('div#measurements_module').detach();
	    		//bin_module_buffer.appendTo('#short_bin_info');
	    		setActiveDivId("#bin_module");	    	
    	});

    	$('#measurements_link').click(function(e){
    		//bin_module_buffer = $('div#bin_module').detach();
    		//measurements_module_buffer.appendTo('#short_bin_info');
    		setActiveDivId("#measurements_module");	
    	});

    	$('#history_link').click(function(e){
    		//bin_module_buffer = $('div#bin_module').detach();
    		//measurements_module_buffer.appendTo('#short_bin_info');
    		setActiveDivId("#history_module");	
    	});

    	$('#speed_link').click(function(e){
    		//bin_module_buffer = $('div#bin_module').detach();
    		//measurements_module_buffer.appendTo('#short_bin_info');
    		var chartLabels = []
    		var chartData = []
    		setActiveDivId("#speed_module");
    		$.getJSON('{% url "control_measure:data_for_chart" a_bin.bin_id %}', function(data){
    			for (var i in data) {
    				chartLabels.push(data[i].month + "/" + data[i].day);
    				chartData.push(parseInt(data[i].pace));
    			}
    			console.log(chartData);
    			console.log(chartLabels);
    			addChart(chartLabels, chartData);
    		});
    		
    			
    	});


    	function addChart (chartLabels, chartData) {
				var lineChartData = {
					labels : chartLabels,
					datasets : [
						
						{
							label: "My Second dataset",
							fillColor : "rgba(151,187,205,0.2)",
							strokeColor : "rgba(151,187,205,1)",
							pointColor : "rgba(151,187,205,1)",
							pointStrokeColor : "#fff",
							pointHighlightFill : "#fff",
							pointHighlightStroke : "rgba(151,187,205,1)",
							data : chartData
						}
					]
				}
					var ctx = document.getElementById("myChart").getContext("2d");
					myLine = new Chart(ctx).Line(lineChartData, {
						 //scaleShowGridLines : true,
					});
			}
});