var app = angular.module("app", []);

app.controller("AppCtrl", function($scope, $http) {

  $http.get('/api').then(function(r) {
    $scope.user = r.data;
  })

});