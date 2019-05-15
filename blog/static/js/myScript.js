
jQuery(function($){
	load=0;
	var obj={
				type:'POST',
				timeout:5000,
				error:function(){
					alert('Произошла какая-то ошибка. Ну хз, попробуйте еще раз');
					},
	}	
	
		
	///Предусматриваем что элементы будут подгружаться динамически. Так что нужно вешать события на элементы которых еще нет, по этому делегируем body
	$('body').bind('click',function(event){
		
		
		
		if(event.target.className=='responce_comm'){
			 self=$(event.target);
			 
			 elem=$("#add_comm_form");

			 $('#esc_com',elem).remove();//удаляем старую кнопку "отмена"
			 $("input[name='comm-id']",elem).attr("value",self.attr("data-com-id"));

			 elem.css({'width':'100%',"margin-left":"0%"})

			 self.parents(".comments").after(elem);

			 $("textarea[name='text_comm']",elem).text('').focus();

			 elem.animate({'width':'85%',"margin-left":"12%"},500)

			 $('button',elem).after('<button id="esc_com" >Отмена</button>')
			
				
			
		}
		if(event.target.id=='esc_com'){
			
			elem=$("#add_comm_form");
			$(event.target).remove()
			$("textarea[name='text_comm']",elem).text('');
			elem.animate({'width':'100%',"margin-left":"0%"},500);

			$('.content').append(elem);
			$("input[name='comm-id']",elem).attr("value","");
		}


		
		
		
	 
	 
	});  // кенец загрузки страницы   

	$("textarea[name='text_comm']").focus(function(event){
		$(this).parents(".add_comm").addClass("add_comm_focus");
	});
	$("textarea[name='text_comm']").blur(function(event){
		$(this).parents(".add_comm").removeClass("add_comm_focus");
	});
}); 








// экранирование
function escapeHtml(text) {
  return text
	  .replace(/&/g, "&amp;")
	  .replace(/</g, "&lt;")
	  .replace(/>/g, "&gt;")
	  .replace(/"/g, "&quot;")
	  .replace(/'/g, "&#039;");
}





/*csrf_token */   
	 
 function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	 
					
