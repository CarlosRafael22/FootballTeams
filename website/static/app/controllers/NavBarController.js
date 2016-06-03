app.controller('NavBarController', ['$scope', '$http', '$location', 'userService', '$cookies', function($scope, $http, $location, userService, $cookies) {

	$scope.userLogedIn = $cookies.get('userLogedIn');
	console.log($scope.userLogedIn);
	if($scope.userLogedIn != null){
		$scope.userLogedIn = JSON.stringify($scope.userLogedIn);
		console.log($scope.userLogedIn);
	}

	// $scope.userBackEnd = userService.getUserBackEnd();
	// console.log($scope.userBackEnd);
	// console.log($scope.userBackEnd.username);

	if($cookies.get('logged') == 'true'){
		console.log("Oi");
		$http.get("/getUser").success(function(response){
			$scope.userBackEnd = response;
			console.log($scope.userBackEnd);
		});
	}else{
		console.log("Deu merda");
	}
	
	
	// SE TIVER NULL EH PQ NINGUEM LOGOU AINDA AI O COOKIE TB VAI SER NULL
	// SE NAO FIZER ISSO DA Unknown provider: $cookieProvider <- $cookie PQ VAI FAZER $cookie.get() SEM COOKIE SETADO
	// if($scope.userLogedIn == null){
	// 	$scope.userCookie = null;
	// }else{
	// 	$scope.userCookie = $cookies.get('userLogedIn');
	// 	console.log($scope.userCookie);
	// }
	//console.log($scope.userLogedIn.username);

	$scope.teste = "Oi nessa";

	$scope.$on('userUpdated', function(){
		$scope.userLogedIn = userService.userLogedIn;
		console.log($scope.userLogedIn);
		console.log($cookies.get('logged'));

		if($cookies.get('logged') == 'true'){
			console.log("Oi");
			$http.get("/getUser").success(function(response){
				$scope.userBackEnd = response;
				console.log($scope.userBackEnd);
			});
		}else{
			console.log("Deu merda");
		}
	});

	$scope.logOut = function(){
    	$http.post('/logout')
    		.success(function(out_data){
    			$cookies.remove('userLogedIn');
    			$cookies.put('logged', 'false');
    			$scope.userBackEnd = null;
    			userService.logoutUser();
				console.log($cookies.get('logged'));
    		});
    	$location.path("/");
    }

}]);