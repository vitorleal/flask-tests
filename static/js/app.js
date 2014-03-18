'use static';

var app = angular.module('flaskApp', ['ngRoute']);

//Config
app.config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        controller: 'mainController',
        templateUrl: '/static/js/views/index.html'
      })
      .when('/my-ads', {
        controller: 'myAds',
        templateUrl: '/static/js/views/myAds.html'
      })
      .when('/new-ad', {
        controller: 'newAd',
        templateUrl: '/static/js/views/newAd.html'
      })
      .when('/profile', {
        controller: 'profile',
        templateUrl: '/static/js/views/profile.html'
      })
      .otherwise({ redirectTo : '/' });
    });

//Run
app.run(function($rootScope, $location) {
  $rootScope.location = $location.path();
});

//Active menu
app.directive('activeMenu', function($location) {
  return function(scope, element, attrs) {
    var li, link, links, currentListItem, i, href,
    listItems = element.find('li'),
    urlMap = {};

    for (i = 0; i < listItems.length; i++) {
      li    = angular.element(listItems[i]);
      links = li.find('a')

      link  = angular.element(links[0])
      href  = link.attr('ng-href').replace(/^#/,'')
      urlMap[href] = li;
    }

    scope.$on('$routeChangeStart', function() {
      var pathListItem = urlMap[$location.path()];
      if (pathListItem) {
        if (currentListItem) {
          currentListItem.removeClass('active');
        }
        currentListItem = pathListItem;
        currentListItem.addClass('active');
      } else {
        listItems.removeClass('active');
      }
    });
  };
});

//Main controller
app.controller('mainController', function ($scope) {
});


//My ads
app.controller('myAds', function ($scope, $rootScope) {
});


//New ad
app.controller('newAd', function ($scope) {
});


//Profile
app.controller('profile', function ($scope) {
});
