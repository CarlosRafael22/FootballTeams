app.controller('MainController', ['$scope','$http', '$location', 'userService', '$cookies', function($scope,$http, $location, userService, $cookies){
	$scope.teams = [
	{'name': 'Chelsea', 'country': 'England'},
	{'name': 'West Ham United', 'country': 'England'},
	{'name': 'Monaco', 'country': 'France'},
	{'name': 'PSG', 'country': 'France'},
	{'name': 'Lyon', 'country': 'France'},
	{'name': 'Marseille', 'country': 'France'},
	{'name': 'Manchester United', 'country': 'England'},
	{'name': 'Manchester City', 'country': 'England'},
	{'name': 'Arsenal', 'country': 'England'},
	{'name': 'AC Milan', 'country': 'Italy'},
	{'name': 'Juventus', 'country': 'Italy'},
	{'name': 'Inter Milan', 'country': 'Italy'},
	];

	$scope.order = 'country';

	$scope.message = "Usando o angular aqui";

	$scope.submit = function() {
        var in_data = { username: $scope.username,
        				email: $scope.email,
        				password: $scope.password };
        $http.post('/signup', in_data)
            .success(function(out_data) {
                $scope.user = response;
    			console.log($scope.user);

    			// Agora vai salvar o usuario no userService pq ai a gnt pode usar em outros controles
    			// no case vai usar no NavBarController pra atualizar a navbar de acordo se o user ta logado ou nao
    			userService.setUser(response);

                // ARMAZENAR O USER NO $COOKIE PRA NAO PERDER QD DER O REFRESH
                $cookies.put('userLogedIn', $scope.user);
                $cookies.put('logged', 'true');
            });
        $location.path("/team");
    };

    

    $scope.logIn = function(){
    	var in_data = {username: $scope.username, password: $scope.password};

    	$http.post('/login', in_data)
    		.success(function(response){
    			$scope.user = response;
    			console.log($scope.user);
                $cookies.put('logged', 'true');
                console.log($cookies.get('logged'));
    			// Agora vai salvar o usuario no userService pq ai a gnt pode usar em outros controles
    			// no case vai usar no NavBarController pra atualizar a navbar de acordo se o user ta logado ou nao
    			userService.setUser(response);

                $cookies.put('userLogedIn', $scope.user);
                

    		});
    	$location.path("/");
    }

    $scope.logOut = function(){
    	$http.post('/logout')
    		.success(function(out_data){
    			userService.logoutUser();
                $cookies.remove('userLogedIn');
                $cookies.put('logged', 'false');
                console.log($cookies.get('logged'));
    		});
    	$location.path("/");
    }

    

}]);