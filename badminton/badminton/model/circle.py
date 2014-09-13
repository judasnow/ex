# coding=utf-8

import time
import datetime

from sporting.database import db


class Circle(db.Model):
    """ 圈子(俱乐部) """

    class Meta:
        db_table = "sp_circle"

    STATE = [-20, -10, 0, 10, 20]

    STATE_DESCRPTION = {-2: "管理员删除",
                        -1: "用户删除",
                        0: "正常",
                        10: "置顶",
                        20: "精华"}

    name = CharField(index=True, max_length=255, verbose_name=u"名称")
    abbr_name = CharField(index=True, max_length=255, verbose_name=u"简称")
    description = TextField(null=True, default="", verbose_name=u"描述")
    enroll_by_agent = BooleanField(default=False, null=False,
                                   verbose_name=u"活动中是否允许成员之间的代报名")
    utmost_enroll_by_agent_limit = IntegerField(default=0,
                                                verbose_name=u"没个成员最大代报人数")
    # @TODO 这个属性方发哦这里还是放到活动信息里面有待考虑
    #       放到活动 model 中只要设置一个默认的值 就 ok 了
    event_automatic_close = BooleanField(default=False,
                                         verbose_name=u"活动是否自动关闭")
    created_at = DateTimeField(null=False, default=(datetime.datetime.utcnow),
                               verbose_name=u"创建时间")
    created_by = ForeignKeyField(User, related_name="circles",
                                 verbose_name=u"圈子创始人")
    state = IntegerField(null=False, default=0, index=True)
    logo = CharField(null=True, default="", verbose_name=u"圈子 Logo 图标")
    cover = CharField(null=True, default="", verbose_name=u"主页顶部背景")

    # 财务信息
    member_charge_sum_min = IntegerField(default=1, verbose_name=u"用户在线充值的最小金额")
    member_charge_sum_max = IntegerField(default=1, verbose_name=u"用户在线充值的最大金额")

    # 支付平台 管理员体现用 可以不填写 如果填写必须填写完整
    payment_platform_name = CharField(null=True, default="",
                                      verbose_name=u"支付平台名称")
    payment_platform_account = CharField(null=True,
                                         verbose_name=u"支付平台帐号")
    payment_platform_username = CharField(null=False,
                                          verbose_name=u"支付平台帐号对应用户名")
    payment_platform_tel = CharField(null=False,
                                     verbose_name=u"支付平台帐号对应手机号码")
    payment_platform_modified_by = CharField(null=True)
    payment_platform_modified_at = DateTimeField(null=True)

    members_count = IntegerField(default=0, index=True)

    @property
    def last_reply_time():
        """ 最近活动时间 最近发布帖子的日期 """
        pass

    @property
    def post_count():
        """ 圈子中帖子的个数 """
        pass

    # @TODO 用户附近的成员 这个属性应该挂到 user model 上还是这里？？？


