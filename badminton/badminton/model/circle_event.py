# coding=utf-8

class CircleEvent(db.Model):
    """ 圈子中的活动 """

    class Meta:
        db_name = "sp_circle_event"

    name = CharField()
    sport = ForeignKeyField(Sport)
    launched_by = ForeignKeyField(User)
    is_cycle_event = BooleanField(default=False)

    # 周期单位 应该是枚举
    cycle = IntegerField()
    location = CharField()
    address = CharField()
    geohash = CharField()

    # 开始时间和结束时间 如果是同一天
    # 就省略结束时间中的日期 报名时间也是同理
    start_at = DateTimeField()
    end_at = DateTimeField()

    enroll_start_at = DateTimeField()
    enroll_end_at = DateTimeField()

    # 是否可以取消报名
    can_cancel_enroll = BooleanField()
    can_cancel_enroll_before = BooleanField()

    # 发布时间 没有发布之前列表中不显示相应记录
    # 这里使用状态的话 就和 状态字段重复了
    publish_at = DateTimeField()

    # 人数限制
    max_enroll_count = IntegerField()
    min_enroll_count = IntegerField()

    # 预计消费
    except_fare_male = IntegerField()
    except_fare_female = IntegerField()
    air_drop_fare_ament = IntegerField()

    # 详情
    detail = TextField()


