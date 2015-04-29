#!/usr/bin/env python


class User(Model):
    
    def join_activity(self, activity):
        pass
        


class Activity(Model):
    pass

    
class Handler(object):
    
    def post(self):

        user = self.current_user()
        activity = Activity.get_or_none(id=1024)

        if user.apply_activity(activity):
            pass
        


class VoteLog(Model):

    vote_by = User
    vote_to = Int
    vote_at = Datetime


class User():
    user.upvote(topic)
    user.downvote(topic)

    user.upvote(post)

    def _upvote(self, upvote_to):
        # 根据 update_to 的类型 写入日志
        # 但 如何判断有效性？也就是那些 object 是可以被
        # upvote 的那些是不可以的？只有使得全部的允许 vote 的对像
        # 都存在某种相同的接口之类的东西 也就是实现相同的方法
        upvote_to.upvote()


class Topic():
    
    def upvote(self):
        # 重新计算点赞次数
        # 记录点赞记录
        pass
        
    def downvote(self):
        pass


