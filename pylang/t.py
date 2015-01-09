#!/usr/bin/env python

from dateutil import tz
from datetime import datetime

from datetime import *
from dateutil.tz import *



def local_to_utc(utc_dt, format_="%Y-%m-%d %H:%M:%S"):

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Shanghai')

    utc_dt = datetime.strptime(utc_dt, format_)    
    utc_dt = utc_dt.replace(tzinfo=from_zone)

    local_dt = utc_dt.astimezone(to_zone)

    print datetime.strftime(local_dt, "%Y-%m-%d %H:%M:%S")

local_to_utc("2015-1-7 10:00:00")


# order

#
# 支付平台订单记录
#
# user_id
# user_mobile 
# platform_name 支付平台名称
# platform_account 支付平台帐号
# pay_money 金额
# state 状态
# trade_no 订单编号
# created_at 订单时间
#


#
# team_admin_ops_log 管理员操作记录
#
# user_id 管理员 user_id
# to_user_id 操作针对的 user_id
# desc 操作描述
# created_at 操作时间
#


#
# member_money_change_log
#
# user_id
# user_mobile 
# money_delta 圈子成员会费变化 (增减)
# 变更前
# 变更后
# 操作人
# 时间
# 变更原因类型 (活动,管理员手动，平台充值)
# 相应 id 类型为活动消费的时候就 填写相应的 activity_id
#


# 流程描述
#
# 用户点击参加活动 -> 付费
#               -> 免费
# 
# 是否需要验证 -> 正式成员
#
# 生成 activity_member 记录状态为未支付
#  
# 等待用户支付 (活动用户列表需要可以选择已经支付的记录) 
# 用户可以选择 余额支付 或者 直接在线支付
# 
# 1 选择余额支付 -> 检查用户的余额（可选，因为允许余额为负数） -> 成功 -> 生成用户资金变化记录
# 2 直接在线支付 -> 产生一条平台支付记录 -> 等待回调 -> 成功 -> 生成用户资金变化记录 -> 
#
#
# -> 支付成功之后 需要修改 活动成员的支付状态 为 pay_state = 1（支付成功）
# 
# 根据活动的进行状态
# 
# 1 成功 -> 结算（自动结算/手动结算）-> 修改活动成员的状态
# 2 取消 -> 修改活动成员的状态 -> 将资金退还到用户余额上
#           活动进行 结算的时候 管理员也可以删除某个用户 被删除的用户支付的报名费用 会自动转移到 其在圈子上的余额中。活动成员中的支付状态修改为 结算
# 
# 管理员直接在 圈子成员记录上修改 成员的余额 -> 增/减 -> 生成管理员操作记录 -> 生成用户资金变动记录 
# 

# @TODO
# 
# 用户积分 全局
# 



