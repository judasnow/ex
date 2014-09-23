# coding=utf-8

class CirclePost(db.Model):
    """ 圈子中的帖子(主题) """

    class Meta:
        db_table = "sp_circle_post"

    posted_by = ForeignKeyField(User, related_name="post", index=True)

    text = TextField(null=False, verbose_name="原始内容")
    state = IntegerField(null=False, default=0)
    posted_at = DateTimeField(default=time.time, null=False)

    lat = DoubleField(default=0)
    lng = DoubleField(default=0)
    geohash = CharField(default="", max_length=16, index=True)

    likes_count = IntegerField(default=0, verbose_name="被赞次数")
    views_count = IntegerField(default=0, verbose_name="被阅读次数")

    @classmethod
    def hot_post(cls):
        """ 热贴 """
        pass

    # @TODO 精华帖子 精华帖子数量


