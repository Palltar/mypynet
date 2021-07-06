from django.conf import settings
from src.wall.models import Post


class Feed:
    """ сервис общих новсотей """
    def  get_post_list(self, user: settings.AUTH_USER_MODEL):
        return Post.objects.filter(user__owner__subscriber=user).order_by('-create_date')\
            .select_related('user').prefetch_related('comments')

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').prefetch_related('comments').get(id=pk)


feed_service = Feed()

#def feed(user):
#    subscribe =Follower.object.filter(subscriber=user)
#    for sub in subscribe
#        new = Post.object.Filter(user=sub)