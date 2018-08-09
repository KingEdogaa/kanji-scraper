#!/usr/bin/env python
import logging
from typing import Any
import requests
import lxml.html

logger = logging.getLogger(__name__)

def get_my_section(html:str) -> lxml.html.HtmlElement:
    "rip out the section of the etree we want"
    tree = lxml.html.fromstring(html)
    # assuming the first p is good enough?
    return tree.find_class("onkunYomi")[0]

def main() -> None:
    "Edgar's cool function"
    req = requests.get("http://www.kanjipedia.jp/kanji/0000384700")
    req.raise_for_status()
    html = req.text
    #logger.info(html[:500])
    print(get_my_section(html).text_content())    

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()