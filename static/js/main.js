$(document).ready(function() {
	document.getElementById('top-container-vid').addEventListener('loadedmetadata', function(){
	  this.currentTime = 10;
	}, false);


	$('#submit-bttn').click(function() {
		sendit();
		$('#sumInput').val('');
		$('#load-svg').fadeIn("slow");
	})

	$('#sumInput').keypress(function(e){
		if (e.which == 13) {
			sendit();
			$('#sumInput').val('');
			$('#load-svg').fadeIn("slow");
		}
	})

});

Vue.component('champion-info', {
	template: '#champion-template',
	delimiters: ["[[", "]]"]
})


Vue.component('app-view', {
	template: '#app-view',

})


var vm = new Vue({
	el: "#app-index",
	data: {
		hasError: false,
		isActive: true,
		message: 'test',
		currentView: 'app-view',
		summonerName: '',
		championList: ''
	},
	methods: {
		resetDisplay: function(){
			this.hasError = false;
			this.isActive = true;
		}
	},
	delimiters: ["[[", "]]"]

})


function sendit() {
	var summName = $('#sumInput').val();
	$.ajax({
		type: "POST",
		dataType: "text",
		data: summName,
		url: "http://127.0.0.1:3000/searchhandler",
		success: function(e) {
			if (e == 'no-user') {
				$('#load-svg').fadeOut();
				vm.hasError = true;
				vm.isActive = false;
				window.setTimeout(vm.resetDisplay, 5000);
			} else {
				vm.summonerName = summName;
				vm.championList = JSON.parse(e);
				vm.currentView = 'champion-info';
				
				console.log(vm.championList);
			}
		}
	})

}


// Event Handlers

