from django.shortcuts import render

from webapp.cat import Cat


def articles_list_view(request):
    return render(request, "index.html")


def article_create_view(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    else:
        action = request.POST.get('action')
        if action == 'play':
            Cat.play_pet()
        elif action == 'feed':
            Cat.feed_pet()
        elif action == 'sleep':
            Cat.sleep_pet()

        if Cat.happiness < 0:
            Cat.happiness = 0

        if Cat.satiety < 0:
            Cat.satiety = 0

        new_cat = {"name": request.POST.get("name"), "happiness": Cat.happiness, "satiety": Cat.satiety, "sleep": Cat.sleep}
        return render(request, "article.html", new_cat)
