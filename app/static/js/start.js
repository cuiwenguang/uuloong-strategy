var isExitJson = (typeof (JSON) !== 'undefined');
if (!Array.indexOf) {
	Array.prototype.indexOf = function (obj) {
		for (var i = 0; i < this.length; i++) {
			if (this[i] == obj) {
				return i;
			}
		}
		return -1;
	}
}
window.baseUrl = '/static/';
require.config({
	urlArgs: 'v=1.0.0',
	baseUrl: window.baseUrl + 'js/',
	paths: {
		//jquery: ['http://apps.bdimg.com/libs/jquery/1.7.1/jquery.min', 'jquery-1.7.1.min'],
		jquery: 'jquery-1.7.1.min',
		//citylist: 'lib/tool-city',
		json2: 'lib/json2',
		alertBox: 'lib/alertBox',
		flowerDialog: 'lib/flower-dialog',
		domReady: 'base/domReady',
		navActive: 'lib/navActive',
		wdate: 'lib/My97DatePicker/WdatePicker',
		extend: "lib/extend.min",
		validate : 'lib/validate',
		//absoluteShow: 'lib/absoluteShow',
		angular: "lib/angular-1.2.20/angular.min",
		ngPager: "lib/ngpage",
		directive: "lib/directive",
		jqueryform: "lib/jquery.form",
		valid: "lib/valid.new",
		'angular-route': 'lib/angular-1.2.20/angular-route.min',
		'angular-animate': 'lib/angular-1.2.20/angular-animate.min',
		'route':"lib/route"
	},
	shim: {
		'alertBox': {
			deps: ['jquery'],
			exports: '$.alertBox'
		},
		'angular': {
			exports: "angular",
			deps: [isExitJson || 'json2', 'jquery'],
			init: function () {
				//init angular module
				window.ngMoudle = function (moudlename, moudle) {
					//$http 拦截器
					function myHttpInterceptor() {
						return {
							'request': function (config) {
								if (config.dataType == "string") {
									var c = {
										'headers': {
											'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
										},
										transformRequest: function (obj) {
											var str = [];
											for (var p in obj) {
												str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
											}
											return str.join("&");
										}
									};
									angular.extend(config, c);
								}
								return config;
							}
						}
					}
					//ie 7
					if (navigator.appName == "Microsoft Internet Explorer" && navigator.appVersion.match(/7./i) == "7.") {
						return angular.module(moudlename, moudle || []).config(["$sceProvider", "$httpProvider", function ($sceProvider, $httpProvider) {
							$sceProvider.enabled(false);
							$httpProvider.interceptors.push(myHttpInterceptor);
						}]);
					} else {
						return angular.module(moudlename, moudle || []).config(["$httpProvider", function ($httpProvider) {
							$httpProvider.interceptors.push(myHttpInterceptor);
						}]);
					}
				}
			}
		},
		'extend': {
			deps: ["angular"]
		},
		'flowerDialog': {
			deps: ["angular"]
		},
		'angular-route': {
			exports: "angular-route",
			deps: ["angular"]
		}
	}


});
window.vd = {
	trim: function (s) {
		return s.replace(/(^\s*)|(\s*$)/g, "");
	},
	check: function (red, val) {
		if (vd.trim(val) && red.test(val)) {
			return 1;
		} else {
			return 0;
		}
	}
};
//工具
window.tool = {
	//去掉 "/"  绝对路径转为相对路径
	setImgUrl: function (url) {
		return url[0] == "/" ? url.substring(1) : url;
	}
}
window.selectedMenu=function(index){
	$("li.nav-item").eq(index).addClass("active");
}
window.selected=function(index){
	$("span.lg-tab").eq(index).addClass("active");
}


