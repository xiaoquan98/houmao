var app = angular.module('issueApp', ['ngSanitize','ngRoute']);
app.controller('mainController', ['$scope', '$http',  function($scope, $http) {
    $scope.Logup = function() {
      $http({
       method  : 'POST',
       url     : '/logup',// new issue always use this address.
       data    : $scope.login, 
       headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
      })
       .success(function(data) { // get return data here.
         if(data.success){
             //   $scope.issues = data.message;
            //  alert("注册成功.");
            $scope.login.checked = true;
         }else{
            $scope.login.checked = false;
            $scope.login.password = "";
         }
       });
    
    };
    
    $scope.Login = function() {
        $http({
          method  : 'POST',
          url     : '/login',// new issue always use this address.
          data    : $scope.login, 
          headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
         })
          .success(function(data) { // get return data here.
            if(data.success){
                //   $scope.issues = data.message;
                // alert("登陆成功.");
                $scope.login.checked = true;
            }else{
               $scope.login.checked = false;
               $scope.login.password = "";
            }
          });
    };
    
    $scope.Logout = function() {
        $http({
          method  : 'POST',
          url     : '/logout',// new issue always use this address.
          headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
         })
          .success(function(data) { // get return data here.
            if(data.success){
                $scope.login.checked = false;
                $scope.login.password = "";
            }else{
               $scope.login.checked = true; 
            }
          });
    };
}]);

app.config(['$routeProvider',function ($routeProvider) {
      $routeProvider
      .when('/list', {
        templateUrl: 'view/list.html',
        controller: 'RouteListCtl'
      })
      .when('/list/:id', {
        templateUrl: 'view/detail.html',
        controller: 'RouteDetailCtl'
      })
      .otherwise({
        redirectTo: '/list'
      });
}]);
    
app.controller('RouteListCtl', ['$scope', '$http',  function($scope, $http) {
    $scope.issues = [];
    $scope.page = 1;
    
    $scope.removeIssue = function(id){
    $http({
      method  : 'DELETE',
      url     : '/v2/issues/issue-'+id,
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
    
    $scope.getComments = function(is){
    $http({
      method  : 'GET',
      url     : '/v2/issues/issue-'+is.id+'/children',
      data    : $scope.input, 
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if (data.success) {
            is.comments = data.message;
            // alert("get children ok.");
        }
      });
    };
    
    $scope.lastPage = function(){
    $http({
      method  : 'GET',
      url     : '/v2/issues/page-'+($scope.page - 1),
      data    : $scope.input, 
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if (data.success) {
            $scope.issues = data.message;
            $scope.page = $scope.page - 1;
        }
      });
    };
    
    $scope.nextPage = function(){
    $http({
      method  : 'GET',
      url     : '/v2/issues/page-'+($scope.page + 1),
      data    : $scope.input, 
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if (data.success) {
            $scope.issues = data.message;
            $scope.page = $scope.page + 1;
        }
      });
    };
    
}]);

app.controller('RouteDetailCtl', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams) {
    $scope.issues = [];
    $scope.id = $routeParams.id;
    
    $scope.removeIssue = function(id){
    $http({
      method  : 'DELETE',
      url     : '/v2/issues/issue-'+id,
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

    $scope.getIssue = function(id){
    $http({
      method  : 'GET',
      url     : '/v2/issues/issue-'+id,
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if (data.success) {
            $scope.issues = data.message;
        }
      });
    };

    $scope.getComments = function(is){
    $http({
      method  : 'GET',
      url     : '/v2/issues/issue-'+is.id+'/children',
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if (data.success) {
            is.comments = data.message;
            // alert("get children ok.");
        }
      });
    };

    $scope.init = function(id){
        $scope.input.isArticle = false;
        $scope.input.parent = 0;
        $scope.input.user = 0;
        $scope.input.detail = "";
        $scope.getIssue(id);
    };
    
    $scope.input = {};
    $scope.newIssue = function() {
    $http({
      method  : 'POST',
      url     : '/v2/issues/issue-0',// new issue always use this address.
      data    : $scope.input, 
      headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
     })
      .success(function(data) { // get return data here.
        if(data.success){
            for(i=0;i<$scope.issues.length;i++){
                if ($scope.issues[i].id == $scope.input.parent){
                    $scope.issues[i].comments = data.message;
                    break;
                }
            }
        }
      });
    };

    // markdown function here
    $scope.markedinputText = "";
    $scope.markedoutputText = "";
    $scope.$watch('markedinputText', function(current, original) {
      $scope.markedoutputText = marked(current);
      $scope.input.detail = current;
    });
        
}]);

app.directive("markdown", function(){
  return function(scope, element, attr){
      var update = function(){
          element.html(marked(element.html()));
      };
      scope.$watch(attr.ngModel, function(){
          update();
      });
      attr.$set("ngTrim", "false");
  };
});


app.directive("autoGrow", function(){
  return function(scope, element, attr){
      var update = function(){
          element.css("height", "auto");
          element.css("height", element[0].scrollHeight + "px");
      };
      scope.$watch(attr.ngModel, function(){
          update();
      });
      attr.$set("ngTrim", "false");
  };
});

marked.setOptions({
    renderer: new marked.Renderer(),
    gfm: true,
    tables: true,
    breaks: false,
    pedantic: false,
    sanitize: false, // if false -> allow plain old HTML ;)
    smartLists: true,
    smartypants: false,
    highlight: function (code, lang) {
      if (lang) {
        return hljs.highlight(lang, code).value;
      } else {
        return hljs.highlightAuto(code).value;
      }
    }
});

