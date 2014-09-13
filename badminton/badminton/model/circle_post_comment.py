# coding=utf-8

class CirclePostComment(db.Model):
    """ 圈子中的回复, 或回复的回复 """

    class Meta:
        db_table = "sp_circle_post_comment"

    post = ForeignKeyField(CirclePost, related_name="comment",
                           verbose_name="回复的帖子")
    created_by = ForeignKeyField(User, related_name="post_comment")

    created_at = DateTimeField(null=False, default=time.time)
    text = TextField(null=False, verbose_name="原始内容")
    state = IntegerField(null=False, default=0)

    parent = ForeignKeyField("self", null=True, related_name="children",
                             verbose_name="回复的回复")
    replies_count = IntegerField(default=0, verbose_name="被回复次数")


