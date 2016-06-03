app.service('userService', ['$rootScope', '$http', function($rootScope, $http){

	this.userLogedIn = null;
	console.log(this.userLogedIn);

	this.setUser = function(user){
		this.userLogedIn = user;
		console.log(this.userLogedIn);
		$rootScope.$broadcast("userUpdated");
	};

	this.logoutUser = function(){
		this.userLogedIn = null;
		$rootScope.$broadcast("userUpdated");
		console.log("Logging out")
	};

	this.getUser = function(){
		return this.userLogedIn;
	};

	this.getUserBackEnd = function(){
		this.userBackEnd = null;
		$http.get("/getUser").success(function(response){
			this.userBackEnd = response;
			console.log(this.userBackEnd);
			return this.userBackEnd;
		});
		// console.log(this.userBackEnd);
		// return this.userBackEnd;
	};
}]);


// app.factory('userService', function($rootScope){

// 	function userService(){
// 		var userLogedIn;

// 		this.setUser = function(user){
// 			userLogedIn = user;
// 			$rootScope.$broadcast('updateUser');
// 			console.log(userLogedIn);
// 		};

// 		this.logoutUser = function(){
// 			userLogedIn = null;
// 		};

// 		this.getUser = function(){
// 			return userLogedIn;
// 		};


// 	}
	
// 	return new userService();

// });