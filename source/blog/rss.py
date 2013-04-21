from django.contrib.syndication.views import Feed
from models import Post

class LatestPostFeed(Feed):
    title = "Latest posts from alexHappens.com"
    link = "/"
    description = "The latest thrills from alexHappens.com"

    def items(self, item):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html_content
