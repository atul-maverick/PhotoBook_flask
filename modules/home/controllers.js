'use strict';
 
angular.module('Home',['ngFileUpload'])
 
.controller('HomeController',
    ['$scope','$rootScope','Upload','$timeout','$http','$location','$route',
    function ($scope,$rootScope,Upload,$timeout,$http,$location,$route) {
        $scope.fileupload=false
        $scope.imageloading=false
        $scope.uid=false
        $scope.pcomment=false
        $scope.image=''
        $scope.show_images=false
        $scope.upButton=false
        $scope.username=$rootScope.globals.currentUser.username
        $scope.$watch('files', function () {
            $scope.upload($scope.files);
        });
        $scope.dataLoading=false
        $scope.myimages= false
        $scope.show_allimages= false
        $scope.log = '';
        $scope.uuid='';
        $scope.upuname='';
        $scope.upload = function (files) {
            $scope.fileupload=true
            if (files && files.length) {
                for (var i = 0; i < files.length; i++) {
                    var file = files[i];
                    Upload.upload({
                        url: '/uploadpics',
                        fields: {
                            'username': $rootScope.globals.currentUser.username
                        },
                        file: file
                    }).progress(function (evt) {
                        var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                        $scope.log = 'progress: ' + progressPercentage + '% ' +
                        evt.config.file.name + '\n' + $scope.log;
                    }).success(function (data, status, headers, config) {
                        $scope.upButton=true
                        $timeout(function() {

                            $scope.log = 'file: ' + config.file.name + ', Response: ' + JSON.stringify(data["message"]) + '\n' + $scope.log;
                            $scope.uuid=data["img"]["uuid"]
                            $scope.upuname=data["img"]["username"]

                        });
                    });
                }
            }
        };

        $scope.getUpimage = function(){
            $scope.fileupload=false
            var url ="/getupimage"
            $http.post(url,{"uuid":$scope.uuid,"username":$scope.upuname}).success(function(data) {
                $scope.show_images=true

                $scope.image=data

            });

        };

        $scope.getAllMyimage = function(){
            $scope.fileupload=false
            $scope.imageloading=true
            var url ="/getAllMyImage"
            $http.post(url,{"username":$rootScope.globals.currentUser.username}).success(function(data) {
                $scope.show_allimages=false
                $scope.show_myimages=true
                $scope.imageloading=false
                // console.log(data)

                $scope.myimages=data

            });
        };

        $scope.getAllimages = function(){
            $scope.fileupload=false
            $scope.imageloading=true
            var url ="/getAllImages"
            $http.post(url).success(function(data) {

                $scope.show_myimages=false
                $scope.show_allimages=true
                // console.log(data)
                $scope.imageloading=false
                $scope.allimages=data

            });
        };

        $scope.postcomment = function(pimage,uuid_data){
           //var uuid_data=document.getElementById("uniid").value
            //var uuid_data=document.getElementById("uniid").innerHTML;
            console.log(uuid_data)
            console.log(pimage.inputcomment)
            var url ="/postcomment"
            var post_params={"username":$rootScope.globals.currentUser.username,"uuid_data":uuid_data,"comment":pimage.inputcomment};
            $http.post(url,post_params).success(function(data) {

                $scope.show_myimages=true
                // console.log(data)
                $scope.pcomment=true


            });
            url="/getComments"
            $http.post(url,post_params).success(function(data) {

                // console.log(data)
                $scope.cphotoComments=data


            });

        };

        $scope.getComments = function(uuid_data){
            $scope.pcomment=true
            var url="/getComments"
            var post_params={"username":$rootScope.globals.currentUser.username,"uuid_data":uuid_data};
            $http.post(url,post_params).success(function(data) {

                // console.log(data)
                $scope.cphotoComments=data


            });

        };

        $scope.deleteImg=function(uuid_data){
            $scope.pcomment=true
            var url="/deleteImg"
            var post_params={"username":$rootScope.globals.currentUser.username,"uuid_data":uuid_data};
            $http.post(url,post_params).success(function(data) {

                // console.log(data)
                $location.path('/')
                $route.reload();

            });
            $scope.Message="The image has been deleted"
        };


    }]);