from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = "Amirrezano's blog"
    link = reverse_lazy('blog_app:post_list')
    description = "New posts of Amirrezano's blog."

    def items(self):
        return Post.published.all()[:2]  # last 2 posts

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)
