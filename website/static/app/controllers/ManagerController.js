app.controller('ManagerController', ['$scope', '$http', 'Teams','$location', function($scope, $http, Teams, $location){


	$scope.submitTeam = function(){
	    	var in_data = { name: $scope.name };

	    	$http.post('/createTeam', in_data)
	    		.success(function(out_data){

	    		});
	    	$location.path("/team");
	 };


   $scope.addPlayer = function(){
        var in_data = {name: $scope.name,
                       position: $scope.position,
                       country: $scope.country,
                       realLifeTeam: $scope.realLifeTeam};

        // //EU ACHO QUE FICA MELHOR SALVANDO OS DADOS EM OUTRA VARIAVEL DP QUE TER QUE PEGAR COM HTTP.POST
        // //E IR PRA VIEWS.PY DE NOVO, MAS NAO SEI SE EH O MAIS EFICIENTE MESMO
        // $scope.nametoEdit = $scope.name;
        // $scope.positiontoEdit = $scope.position;
        // $scope.countrytoEdit = $scope.country;
        // $scope.realLifeTeamtoEdit = $scope.realLifeTeam;

        console.log($scope.nametoEdit);

        // LIMPANDO OS INPUTS DO FORM
        $scope.name = "";
        $scope.position = "";
        $scope.country = "";
        $scope.realLifeTeam = "";

        $http.post("/createPlayer", in_data)
          .success(function(response){
            console.log("Added player");
            $http.get("/getPlayers")
              .success(function(response){
                $scope.players = response;
                console.log($scope.players);
              });
          });
   };


   $scope.editPlayer = function($index){
      console.log($index);
      $scope.currentIndex = $index;
      console.log($scope.currentIndex);
      console.log($scope.players[$index]);
      $scope.playertoEdit = $scope.players[$index];
      console.log($scope.playertoEdit['id']);
        $http.get("players/"+$scope.playertoEdit['id'])
          .success(function(response){
              console.log(response);

              $scope.nametoEdit = response.name;
              $scope.positiontoEdit = response.position;
              $scope.countrytoEdit = response.country;
              $scope.realLifeTeamtoEdit = response.realLife_team;
              console.log("Terminou dentro");
          });
      console.log("Terminou fora");
   };


   $scope.saveEditedPlayer = function(){
      var player_id = $scope.playertoEdit.id;
      console.log(player_id);
      console.log($scope.currentIndex);

      var in_data = {
        nameUpdated: $scope.nametoEdit,
        positionUpdated: $scope.positiontoEdit,
        countryUpdated: $scope.countrytoEdit,
        realLifeTeamUpdated: $scope.realLifeTeamtoEdit,
        player_id: player_id
      };

      $http.post("/updatePlayer", in_data)
        .success(function(response){
            console.log($scope.currentIndex);
            $scope.players[$scope.currentIndex] = response;
            console.log($scope.players);
        });
   };
   
    $http.get("/getPlayers")
          .success(function(response){
            $scope.players = response;
            console.log($scope.players);
          });



    Teams.query(function(data){
    	$scope.allTeams = data;
    });


    Teams.get({id: 1}, function(data){
    	$scope.teamOne = data;
    });

    $http.get("/teams", {params: { onlyOneTeam: true } }).success(function(response) {
    		$scope.team = response;
    		$scope.teamName = $scope.team['name'];
    	});

    // $http({
    //     method: 'GET',
    //     url: "/teams",
    //     params: { teamList: false}
    //  }).success(function(data){
    //     // With the data succesfully returned, call our callback
    //     $scope.team = response;
    // });

    //Chama pra pegar os times que o user tem assim que chegar na pagina
	// $scope.team = $scope.getTeam();

}]);