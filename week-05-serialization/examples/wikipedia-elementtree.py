#!/usr/bin/env python

import bz2
import xml.etree.ElementTree as ET

from logging_config import logger


if __name__ == "__main__":
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    tree = ET.parse(f)
    root = tree.getroot()

    # for title in root.findall('{http://www.mediawiki.org/xml/export-0.8/}page/{http://www.mediawiki.org/xml/export-0.8/}title'):
    # or,
    namespaces = {'xmlns': 'http://www.mediawiki.org/xml/export-0.8/'}
    for title in root.findall('xmlns:page/xmlns:title', namespaces=namespaces):
        logger.info(title.text)
