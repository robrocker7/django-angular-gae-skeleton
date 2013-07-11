var djangoApp = angular.module('djangoApp', []);


djangoApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'template/home.html',
        controller: 'HomeController'
    });
    $routeProvider.when('/about/', {
        templateUrl: 'template/about.html',
        controller: 'AboutController'
    });
}]);

djangoApp.controller('HomeController', function($scope){
    $scope.resources = [{
        'name': 'Dan Wahlin\'s Angular 60ish Minute Overview',
        'url': 'http://www.youtube.com/watch?v=i9MHigUZKEM',
    },{
        'name': 'Angular Website',
        'url': 'http://angularjs.org'
    }]
});
djangoApp.controller('AboutController', function($scope){

});
