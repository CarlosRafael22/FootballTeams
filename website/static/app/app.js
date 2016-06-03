var app = angular.module('app', ['ngRoute', 'ngResource', 'ngCookies']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
	$routeProvider
	.when('/signup',{
		templateUrl: 'static/partials/signup.html',
		controller: 'MainController'
	})
	.when('/', {
		templateUrl: 'static/partials/home.html',
		controller: 'MainController'
	})
	.when('/team',{
		templateUrl: 'static/partials/team.html',
		controller: 'ManagerController'
	})
	.when('/login',{
		templateUrl: 'static/partials/login.html',
		controller: 'MainController'
	})
	.when('/userteam',{
		templateUrl: 'static/partials/user_team.html',
		controller: 'ManagerController'
	})

	// $locationProvider.htmlMode(true);
}]);

app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

 //    var $cookies;
	// angular.injector(['ngCookies']).invoke(function(_$cookies_) {
	//   $cookies = _$cookies_;
	// });    
	// console.log($cookies);

 //    $httpProvider.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];

 	//A COISA QUE FUNCIONOU FOI ISSO!!!!:

 	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
