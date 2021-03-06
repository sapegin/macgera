title: Отказ от комментариев Disqus.
date: 2012-09-23
type: blog
tags: [JavaScript, Django, Блог]

Так вышло что я отказался от комментариев [Disqus](http://disqus.com). Нет, не потому что он плох, отнюдь не плох. Я вообще радовался как ребенок, когда узнал что это такое. Просто в данном конкретном случае он дает какие-то не объяснимые мне сбои. И я решил поставить стандартные комментарии Django. 

Короче говоря проблема довольно странная. Тех поддержка ответила, но сделав все что они сказали, я проблему не решил. А собсвтенно она в чем, в том что почему-то дискус не подхватывает url статьи. Причем забавно вот что. 

У меня сам url генерируется следующим образом:

    def get_absolute_url(self):
        return 'http://%s/post/%s/' % (Site.objects.get_current().domain, self.slug)

То есть все просто `http://mihailyakimenko.com/post/000001/` и все, но дискус видит по другому. А именно: `http://mihailyakimenko.com/post#comment-651660753` и как тут быть? Но если бы я изменил url и поставил как было раньше, `http://mihailyakimenko.com/post-000001/` то тогда все работает. 

![Битые ссылки в Disqus.](/static/files/disqus_fail.jpg)

*Битые ссылки в Disqus.*

Я сначала думал что проблема в `/` который в конце и сделал код по другому. 

    def get_absolute_url(self):
        return 'http://%s/post/%s' % (Site.objects.get_current().domain, self.slug)

И соответственно ссылка вида `http://mihailyakimenko.com/post/000001` без слеша в конце. Но это не помогло. Помогает только `post-000001` и не важно есть слеш в конце или нет. А мне просто так не нравится, и я хочу другой url такой как сейчас. Я даже пробовал добавлять ему собственный url передавая конструкцию в шаблон, даже не в моделях. 
 
    <script type="text/javascript">
      var disqus_url = 'http://{{ site }}/post/{{ post.slig }}'; 
    </script>

Но победить багу не удалось. Мучить тех поддержку. не будучи платным подписчиком, у меня просто рука не поднялась. Да и как-то, давно хотел разобраться с Django комментариями. А там вообще все просто оказалось, единственное что вызвало трудность, это [akismet](http://akismet.com/). И кстати я пока что не уверен что сделал все правильно с ним. Если вы знаете как сделать правильно, или лучше, буду благодарен, на всякий случай код на [гитхабе](https://github.com/macgera/myblog/blob/master/blog/models.py#L70).

Зато внешний вид комментариев, хоть и не древовидный, но мне нравится. Позже возможно допилю в Ajax варианте. 

### Добавлено 24.09.2012 

Так же я попробовал дать Дискусу старый урл а блогу оба.

    urlpatterns = patterns('blog.views',
        url(r'^tag/(?P<slug>[^\.]+)/$', 'tag_view', name='tag_view'),
        url(r'^post/(?P<slug>[^\.]+)/$', 'post_view', name='post_view'),
        url(r'^post-(?P<slug>[^\.]+)/$', 'post_view', name='post_view'),
        url(r'^page/(?P<slug>[^\.]+)/$', 'page_view', name='page_view'),
    )

Но тоже не помогло. Так я окончательно убедился в том что лучше оставить свои комментарии, и со временем их допилить. 