var app = angular.module('issueApp', ['ngSanitize']);
app.controller('postController', ['$scope', '$http',  function($scope, $http) {
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
    
    // markdown function here
    $scope.markedinputText = "";
    $scope.markedoutputText = "";
    $scope.$watch('markedinputText', function(current, original) {
      $scope.markedoutputText = marked(current);
      $scope.input.detail = $scope.markedoutputText;
    });
        
    }    
]);


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

