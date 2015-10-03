

    var postApp = angular.module('issueApp', []);
    postApp.controller('postController', ['$scope', '$http',  function($scope, $http) {
       $scope.input = {};
         $scope.submitForm = function() {
        $http({
          method  : 'POST',
          url     : '/json/issue/0',// new issue always use this address.
          data    : $scope.input, 
          headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
         })
          .success(function(data) { // get return data here.
            if (data.errors) {
              $scope.errorName = data.errors.name;
              $scope.errorUserName = data.errors.username;
              $scope.errorEmail = data.errors.email;
              // alert("error happens.");
            } else {
              $scope.message = data.message;
              // alert(data.message[0].detail);
            }
          });
        };
    }]);
