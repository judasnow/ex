# coding=utf-8

class CircleEventEnrolls(db.Model):
    """ 圈子活动报名信息 """

    class Meta:
        db_table = "sp_circle_event_enrolls"

    circle = ForeignKeyField(CircleEvent)
    member = ForeignKeyField(User)
    agent_by = ForeignKeyField(User)
    sum = IntegerField()
    created_by = DateTimeField(default=time.time)
    # 报名途径
    enroll_by = CharField()
    # 是否是候补报名
    is_candidate = BooleanField()
    state = IntegerField()


