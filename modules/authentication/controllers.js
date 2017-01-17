'use strict';
 
angular.module('Authentication')
.controller('LoginController',
    ['$scope', '$rootScope', '$location', 'AuthenticationService','$http','ModalService',
    function ($scope, $rootScope, $location, AuthenticationService,$http,ModalService) {
        // reset login status
        AuthenticationService.ClearCredentials();
        $scope.modalbutton=false
        $scope.message=''
		//$scope.openLoginModal = 
		$scope.openLoginModal = function() { 
				console.log("entered");
				ModalService.showModal({
            templateUrl: 'modules/authentication/views/signupModal.html',
            controller: "LoginController",
            scope: $scope
        }).then(function(modal) {
            modal.element.modal();
            
        });
		
		 };
		
        $scope.login = function () {
            $scope.dataLoading = true;
            AuthenticationService.Login($scope.username, $scope.password, function(response) {
                if(response.success) {
                    AuthenticationService.SetCredentials($scope.username, $scope.password);
                    $location.path('/');
                } else {
                    $scope.error = response.message;
                    $scope.dataLoading = false;
                }
            });
        };

        $scope.signup = function(){
            var url="/user/signup"
            $scope.newdataLoading = true;
            $http.post(url,{"username":$scope.newusername,"password":$scope.newpassword,"gender":$scope.gender}).success(function(data){
                    $scope.message=data;
                    ModalService.showModal({
            templateUrl: 'modules/authentication/views/modal.html',
            controller: "LoginController",
            scope: $scope
        }).then(function(modal) {
            modal.element.modal();
            
        });
                    $scope.newdataLoading = false;

            });
            $location.path('/');
        }
    }]);