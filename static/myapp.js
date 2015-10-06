var postApp = angular.module('issueApp', []);
postApp.controller('postController', ['$scope', '$http',  function($scope, $http) {
    $scope.issues = [];
   $scope.input = {};
    $scope.newIssue = function() {
    $http({
      method  : 'POST',
      url     : '/v1/issues/0',// new issue always use this address.
      data    : $scope.input, 
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if(data.success){
          $scope.issues = data.message;
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
            $scope.issues = data.message;
        } else {
            alert("fail to delete.");
        }
      });
    };

    $scope.getIssues = function(){
    $http({
      method  : 'GET',
      url     : '/v1/issues',
      data    : $scope.input, 
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if (data.success) {
            $scope.issues = data.message;
        }
      });
    };

    $scope.init = function(ijson){
        $scope.issues = ijson;
        $scope.input.isArticle = false;
        $scope.input.parent = 0;
        $scope.input.user = 0;
        $scope.input.detail = "";
    };
        
        
    }    
]);
