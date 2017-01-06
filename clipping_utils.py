#!/usr/bin/env python

from __future__ import with_statement
import ConfigParser

CONF_FILE = 'clipping.conf'


def get_config(block, key):

    # get parser
    config = ConfigParser.ConfigParser()

    # open config file
    with open(CONF_FILE, 'r') as conf_file:
        config.readfp(conf_file)

    # get result
    result = config.get(block, key)

    return result
