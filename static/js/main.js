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

Vue.component('champion-info', {
	template: '#champion-template'
})


Vue.component('app-view', {
	template: '#app-view',
})


var vm = new Vue({
	el: "#app-index",
	data: {
		hasError: false,
		isActive: true,
		currentView: 'app-view',
		championList: [["Teemo", "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_0.jpg", 0.33, 6, 0, 1], ["Caitlyn", "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Caitlyn_0.jpg", 0.67, 6, 2, 1], ["Miss Fortune", "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Miss Fortune_0.jpg", 0.88, 8, 2, 1]]
	},
	methods: {
		resetDisplay: function(){
			this.hasError = false;
			this.isActive = true;
		}
	},
	delimiter: ["[[" , "]]"]

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
				vm.hasError = true;
				vm.isActive = false;

				window.setTimeout(vm.resetDisplay, 3000);
			} else {

				vm.championList = JSON.parse(e);
				vm.currentView = 'champion-info';
				
				console.log(vm.championList);
			}
		}
	})

}


// Event Handlers

