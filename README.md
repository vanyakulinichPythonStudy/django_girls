#### steps to start => create virtual env => start virtual env => do 'pip install -r requirements.txt' to install django

#### admin credentials: username: admin, password: djangogirls

дз

1. добавлена страница с выводом всех комментариев
   в хедере сайта есть ссылка на нее(выводит список всех комментариев с ссылками на блоги)

2. фильтр valid_url в blog/templatetags/extras.py строчка 35
   фильтр применен в двух местах - при добавлении комментариев(post_detail.html) и при выводе комментариев(all_comments.html)

3. встраиваемый тег images в blog/templatetags/extras.py строчка 159
   под картинку создан свой шаблон images.html и ссылка в хедере сайта
