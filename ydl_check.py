#!/usr/bin/env python
# coding: utf-8

import os
import logging
import youtube_dl

logger = logging.getLogger(__name__)

SAVE_TO = os.path.join(os.getcwd(), "data")
YDL_OPTIONS = {
    "outtmpl": "{save_to}/%(title)s.mp4".format(save_to=SAVE_TO)
}


def download(url):
    logger.info(f"start download {url}")
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=True)
        logger.info(f"finish download {url}")

    return info


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    url = input(">> ")
    download(url)
