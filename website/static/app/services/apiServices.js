app.factory("Teams", function($resource){
	return $resource('teams/:id');
});