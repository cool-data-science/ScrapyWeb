# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class City58Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = Field()
    job_salary = Field()
    job_description = Field()
    job_welfare = Field()
    job_requirement = Field()
    job_location = Field()
    job_detail = Field()
    company_name = Field()
    company_introduction = Field()
    
    publish_data = Field()
    review = Field()
    application = Field()
    resume_feedback = Field()
    recruitment_number = Field()
    when_join58 = Field()
    
