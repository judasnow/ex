# coding=utf-8

import time

import tornado
from tornado.options import define, options

#from d.logging import logger


define("cmd", metavar="start_web|test_worker", default="")
define("debug", default=False)

def main():

    tornado.options.parse_command_line()

    if options.cmd == "start_web":
        from d.web.urls import urls

        #logger.info("web start")

        application = tornado.web.Application(urls,
                                              debug=options.debug,
                                              template_path="d/web/tpl")
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

    elif options.cmd == "start_worker":
        from d.worker.worker import DBGroupWorker

        group_list = ["Xsz", "haixiuzu", "meituikong", "miniskirtlegs", "515085", "516876", "103485", "510760"]

        while 1:
            time.sleep(2)
            for group_name in group_list:
                #logger.info("%s: work start" % group_name)
                w = DBGroupWorker(group_name)
                w.start_flow()

    elif options.cmd == "init_db":
        from d.models.image import Image
        from d.models.topic import Topic

        Topic.create_table()
        Image.create_table()

        print "create_table ok"

    elif option.cmd == "migre_db":
        pass

if __name__ == "__main__":
    main()


