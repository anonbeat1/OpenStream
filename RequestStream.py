from mitmproxy import http
from mitmproxy import ctx
import os
import threading


def response(flow: http.HTTPFlow):

   if "api.opensea.io/graphql" in flow.request.url and flow.response.status_code == 200:
        ctx.log.info("we have seen opensea api ")
        file = open("data.txt", "a")
        file.write(str(flow.response.content.decode('utf-8')) + "\n")
