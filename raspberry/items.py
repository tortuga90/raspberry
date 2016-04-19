# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RaspberryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    key = scrapy.Field()
    head_forum = scrapy.Field()
    head_forum_link = scrapy.Field()
    forum_name = scrapy.Field()
    forum_link = scrapy.Field()
    forum_topics = scrapy.Field()
    forum_posts = scrapy.Field()
    forum_lp_user = scrapy.Field()
    forum_lp_user_link = scrapy.Field()
    pass

class ProjectsItem(scrapy.Item):
    topic_name = scrapy.Field()
    topic_link = scrapy.Field()
    topic_replies = scrapy.Field()
    topic_views = scrapy.Field()
    topic_author = scrapy.Field()
    topic_author_link = scrapy.Field()
    pass
