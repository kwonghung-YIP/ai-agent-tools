import asyncio
import aiohttp
from bs4 import BeautifulSoup
from lxml import etree

async def parse(url:str,xpath:str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            page = await resp.text()
            soup = BeautifulSoup(page,"html.parser")
            dom = etree.HTML(str(soup))
            value = dom.xpath(xpath)[0]
            print(value)
            return value

async def main():
    url = f'https://www.xe.com/en-gb/currencyconverter/convert/?Amount=1&From=USD&To=GBP'
    xpath = "//text()[contains(., 'USD =') and contains(., 'GBP')]"
    result = await parse(url,xpath)
    print(result)
    

if __name__=="__main__":
    asyncio.run(main())