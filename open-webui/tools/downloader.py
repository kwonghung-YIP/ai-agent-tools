"""
title: Resource Downloader
author: Hung Yip
description: This simple tool aim to download file from the Internet
"""

import aiohttp
import asyncio

class Tools:
    def __init__(self):
        pass

    async def download_html(self,url:str) -> str:
        """
        Download the HTML file source code from the URL parameter
        :params 
        - url: URL to download the html page
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.status)
                page = await resp.text()
                return page

    async def extract_from_html(self,url:str,xpath:str) -> str:
        """
        Download the html file and extract the element by xpath
        - url: URL to download the html page
        - xpath: XPATH to extract the element from the html page
        """
        return "damn it!"
