var postApp = angular.module('issueApp', []);
postApp.controller('postController', ['$scope', '$http',  function($scope, $http) {
   $scope.input = {};
   $scope.newIssue = function() {
    $http({
      method  : 'POST',
      url     : '/v1/issues/0',// new issue always use this address.
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
    
    $scope.removeIssue = function(id){
        $http({
          method  : 'DELETE',
          url     : '/v1/issues/'+id,
          data    : $scope.input, 
          headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
         })
          .success(function(data) { // get return data here.
            if (data.success) {
            //   alert("success to delete.");
            } else {
              alert("fail to delete.");
            }
          });
        };
        
        
    }    
]);