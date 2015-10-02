

    var postApp = angular.module('issueApp', []);
    postApp.controller('postController', ['$scope', '$http',  function($scope, $http) {
       $scope.input = {};
         $scope.submitForm = function() {
        $http({
          method  : 'POST',
          url     : '/',
          data    : $scope.input, 
          headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
         })
          .success(function(data) {
            if (data.errors) {
             $scope.errorName = data.errors.name;
              $scope.errorUserName = data.errors.username;
              $scope.errorEmail = data.errors.email;
            } else {
              $scope.message = data.message;
            }
          });
        };
    }]);
