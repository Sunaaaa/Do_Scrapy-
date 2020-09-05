import scrapy
import json


class IdmetaSpider(scrapy.Spider):
    name = 'idmeta'
    allowed_domains = ['https://static.api.nexon.co.kr/fifaonline4/latest/spid.json']
    start_urls = ['https://static.api.nexon.co.kr/fifaonline4/latest/spid.json']
    headers={"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTQyNjcxOTIxMyIsImF1dGhfaWQiOiIyIiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIiwic2VydmljZV9pZCI6IjQzMDAxMTQ4MSIsIlgtQXBwLVJhdGUtTGltaXQiOiI1MDA6MTAiLCJuYmYiOjE1OTg5MzY0NTUsImV4cCI6MTYxNDQ4ODQ1NSwiaWF0IjoxNTk4OTM2NDU1fQ.YaqrOe58Ma89bArXA77QDb0QfcwZwYenrJhftId1ktU"}

    def parse(self, response):
        items = []
        jsonresponse = json.loads(response)

        print(jsonresponse)
