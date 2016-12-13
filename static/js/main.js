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

function sendit() {
	var summName = $('#sumInput').val();
	console.log(summName);
	$.ajax({
		type: "POST",
		dataType: "text",
		data: summName	,
		url: "http://127.0.0.1:3000/searchhandler",
		success: function(e) {
			console.log(e + 'success');
		}
	})

}