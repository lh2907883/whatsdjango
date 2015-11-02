/**
 * ImageUpload
 * 依赖jQuery  
 */
(function($){
    // 因为django把script引用到了head里面，所以要在domready以后执行逻辑 
    $(function(){
        var fileChange = function(){
            var _this = this;
            var file = this.files[0];
            //这里我们判断下类型如果不是图片就返回 去掉就可以上传任意文件 
            if(!/image\/\w+/.test(file.type)){
                alert("请确保文件为图像类型"); 
                return false; 
            }
            var reader = new FileReader(); 
            reader.readAsDataURL(file); 
            reader.onload = function(e){ 
                $(_this).prev('img').attr('src', this.result);
                $(_this).next('input[type="hidden"]').val(this.result);
            }
        }

        $('.jq-imgup').each(function(){
            var $this = $(this);
            $('input[type="file"]', $this).change(fileChange);
        });
    });
//django对juqery重命名了。。
})(django.jQuery) 