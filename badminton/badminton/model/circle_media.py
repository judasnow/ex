#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CircleMedia(db.Model):
    """ 帖子中的多媒体资源 """

    class Meta:
        db_table = "sp_circle_post_media"

    name = CharField(null=True)
    target = IntegerField(null=False)
    # POST, COMMENT
    target_type = CharField(null=False)
    meta = CharField(null=False)
    # IMAGE, VIDEO, AUIDO
    type = CharField(null=False)
    created_at = DateTimeField(null=False, default=time.time)


