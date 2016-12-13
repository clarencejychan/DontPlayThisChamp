$(document).ready(function() {
	document.getElementById('top-container-vid').addEventListener('loadedmetadata', function(){
	  this.currentTime = 10;
	}, false);


	$('#submit-bttn').click(function() {
		sendit();
		$('#sumInput').val('');
	})

	$('#sumInput').keypress(function(e){
		if (e.which == 13) {
			sendit();
			$('#sumInput').val('');
		}
	})

});

var vm = new Vue({
	el: "body",
	data: {
		currentView: "default"
	}
})


var error = new Vue({
	el:'#error', 
	data : {
		hasError : false,
		isActive : true
	},
	methods: {
		resetDisplay: function(){
			this.hasError = false;
			this.isActive = true;
		}
	}
})




function sendit() {
	var summName = $('#sumInput').val();
	console.log(summName);
	$.ajax({
		type: "POST",
		dataType: "text",
		data: summName,
		url: "http://127.0.0.1:3000/searchhandler",
		success: function(e) {
			if (e == 'no-user') {
				error.hasError = true;
				error.isActive = false;
				window.setTimeout(error.resetDisplay, 3000);
			}
		}
	})

}


// Event Handlers

