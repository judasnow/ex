# coding=utf-8

from .base import Base


class CircleMember(db.Model):
    """ 圈子的成员 """

    class Meta:
        db_table = "sp_circle_member"

    user = ForeignKeyField(User, related_name="circle")
    circle = ForeignKeyField(Circle, related_name="member")
    state = IntegerField(null=False, default=0)
    role = IntegerField(null=False, default=0)
    blance = IntegerField(null=False, default=0)
    free_times = IntegerField(null=False, default=0)
    title = CharField(null=True, default="")
    points = IntegerField(null=True, default=0, verbose_name=u"积分")

    joined_at = DateTimeField(null=False, default=(time.time),
                              verbose_name="用户加入该圈子的时间")


