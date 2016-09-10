/**
 * @author guopy  
 * @date 2016年1月13日 下午11:17
 * @version V1.0  
 */
define(['angular'],function(angular){
	return {
		listCtrl:function($scope,$http){
			//$scope.list = list;
		},
		imgdir:function(){
			return {
				restrict : "A",
				scope:"=",
				link:function(scope, ele, attrs, ctrl){
                    var productid = $(ele).attr("data-id");
					angular.element(ele).bind("click",function(){
						$.alertBox.custom({title:"产品图片",content:$("#js_box_img").html(),width:400,height:400,init:function(){
							//操作动态显示
							$(".alertbox #productId").val(productid);
							$(".alertbox #photoimg").change(function(){
								var reader = new FileReader();
								reader.onload = function (evt) {
									var str=" src='"+evt.target.result+"'";
									$(".alertbox .up-img-list").empty().prepend("<a><img "+str+"/></a>");
								};
							    reader.readAsDataURL(this.files[0]);
							});
						},submit:function(){
							$.alertBox.success({content: "上传成功！"});
						}});
					});
				}
			}
        },
	}
	
});