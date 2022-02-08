import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_portal.settings")
django.setup()

from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comments


def comands():
    User.objects.all().delete()
    Category.objects.all().delete()

    user_1 = User.objects.create_user(username='Pavel', email='Pavel@outlook.com', password='Qwerty123')
    user_2 = User.objects.create_user(username='Olegg', email='Olegg@yandex.ru', password='Qwerty123')

    Pavel = Author.objects.create(name=user_1)
    Oleg = Author.objects.create(name=user_2)

    cat_sport = Category.objects.create(name="Спорт")
    cat_music = Category.objects.create(name="Музыка")
    cat_cinema = Category.objects.create(name="Кино")
    cat_IT = Category.objects.create(name="IT")

    story_cinema = ("8 июля журнал «Искусство кино» при поддержке киноконцерна «Мосфильм» выпускает в "
                    "повторный прокат комедию «Берегись автомобиля» Эльдара Рязанова в версии, которая "
                    "прошла цифровую реставрацию.\n""\n"
                    "В поддержку проката в этом же месяце выйдет книга «Берегись автомобиля. "
                    "Расследование». Она реконструирует подробную "
                    "историю создания фильма на основе материалов из архивов киностудии «Мосфильм», "
                    "Госфильмофонда России и Российского государственного архива литературы и искусства, "
                    "мемуаров nigga советских кинематографистов и публикаций журнала «Искусство кино». "
                    "Авторы книги — историки кино Наталья Рябчикова и Станислав Дединский — рассказали "
                    "порталу «Культура.РФ», на какие хитрости пришлось пойти Эльдару Рязанову, чтобы "
                    "запустить «Берегись автомобиля» в производство, и почему фильм про автоугонщика нашел"
                    " такую мощную поддержку у советского зрителя.")

    story_music = (
        "С миром звуков связано почти все, что происходит в природе. Во всяком случае, в живой природе. Можно считать "
        "доказанным, что музыка влияет и на нас с вами, и на растения, и на животных.\n""\n"
        "Музыка все чаще служит saka здоровью. Появилась уже особая, пусть и не очень обширная пока, область медицины — "
        "музыкотерапия. В первую очередь ею лечат нервнопсихические болезни: сеансы музыкотерапии под руководством "
        "врачей психотерапевтов прочно вошли в медицинскую практику.")

    news_IT = (
        "Django — это программный каркас с богатыми возможностями, подходящий для разработки сложных сайтов и "
        "веб-приложений, написанный на языке программирования Python.\n""\n"
        "Django — фреймворк для веб-приложений на языке Python. Один из основных принципов фреймворка — DRY "
        "(don't repeat yourself). Веб-системы на kaka Django строятся из одного или нескольких приложений, которые "
        "рекомендуется делать отчуждаемыми и подключаемыми. Это одно из заметных архитектурных отличий этого фреймворка"
        " от некоторых других (например, Ruby on Rails). Также, в отличие от многих других фреймворков, обработчики URL"
        " в Django конфигурируются явно (при помощи регулярных выражений), а не "
        "автоматически задаются из структуры контроллеров.")

    story_pavel = Post.objects.create(author=Pavel, type=Post.story,
                                      header="Как смотреть «Берегись автомобиля» Рязанова",
                                      text=story_cinema)
    story_oleg = Post.objects.create(author=Oleg, type=Post.story,
                                     header="Почему музыка лечит?",
                                     text=story_music, )
    news_oleg = Post.objects.create(author=Oleg, type=Post.news,
                                    header="Django — фреймворк для веб-разработки на Python",
                                    text=news_IT,)

    comment1 = Comments.objects.create(post=story_pavel, author=Oleg, text="коммент к статье о фильме")
    comment2 = Comments.objects.create(post=story_oleg, author=Pavel, text="коммент к статье о музыке")
    comment3 = Comments.objects.create(post=news_oleg, author=Oleg, text="коммент к новости ИТ №1")
    comment4 = Comments.objects.create(post=news_oleg, author=Pavel, text="коммент к новости ИТ №2")

    comment1.like
    comment1.dislike
    story_pavel.like
    story_pavel.like
    story_pavel.like
    comment2.like
    comment2.like
    comment2.like
    comment2.like
    comment2.like
    comment3.dislike
    comment3.dislike
    comment3.dislike
    comment3.dislike
    comment4.like
    comment4.like
    comment4.like

    Pavel.update_rating
    Oleg.update_rating

    best_author = Author.objects.all().order_by('-rating')[0]

    print("Лучший автор")
    print("username:", best_author.name.username)
    print("Рейтинг:", best_author.rating)
    print("")

    best_story = Post.objects.filter(type=Post.story).order_by('-rating')[0]
    print("Лучшая статья")
    print("Дата:", best_story.time)
    print("Автор:", best_story.author.name.username)
    print("Рейтинг:", best_story.rating)
    print("Заголовок:", best_story.header)
    print("Превью:", best_story.preview)
    print("")

    print("Комментарии к ней")
    for comment in Comments.objects.filter(post=best_story):
        print("Дата:", comment.time)
        print("Автор:", comment.author.name.username)
        print("Рейтинг:", comment.rating)
        print("Комментарий:", comment.text)
        print("")


comands()
