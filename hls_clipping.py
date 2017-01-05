#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import os
import re
import sys
import platform
import clipping_utils

reload(sys)
sys.setdefaultencoding('utf8')

sysstr = platform.system()

# clips之间分隔符
BOUNDARY = u"=========="

# 行分隔符
LINE_SEP = u'\n'

if sysstr == "Windows":
    FILE_PATH = os.path.join(os.getcwd(), "My Clippings.txt")
    OUTPUT_DIR = os.path.join(os.getcwd(), "kindle_hls")
elif sysstr == "Darwin":
    FILE_PATH = clipping_utils.get_config("source", "FILE_PATH")
    OUTPUT_DIR = clipping_utils.get_config("target", "OUTPUT_DIR")

def get_sections(filename):
    """
    以BOUNDARY分隔，切分文档
    """
    with open(filename, 'r') as f:
        content = f.read()
    content = content.replace(u'\r', u'')

    return content.split(BOUNDARY)

def get_clip(section):
    """
    获取clip
    """
    clip = {}

    lines = [l for l in section.split(LINE_SEP) if l]

    if len(lines) != 3:
        return

    clip['book'] = lines[0]
    match = re.search(r'(\d+)-(\d+)', lines[1])
    if not match:
        return
    position = match.group(1)

    clip['position'] = int(position)
    clip['content'] = lines[2]

    return clip

def export_txt(clips):
    """
    生成文件
    每本书一个文件
    """
    print "into export_txt..."
    for book in clips:
        lines = []
        for pos in sorted(clips[book]):
            lines.append(clips[book][pos])
        if sysstr == "Windows" and ":" in book:
            book = book.split(":")[0]
        filename = os.path.join(OUTPUT_DIR, u"%s.txt" % book)
        with open(filename, 'w') as f:
            f.write("\n\n--\n\n".join(lines))

def checkdirectory():
    """
    检查输出目录是否存在，若不存在则生成
    """
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    return

def main():
    checkdirectory()

    clips = collections.defaultdict(dict)

    sections = get_sections(FILE_PATH)

    for section in sections:
        clip = get_clip(section)
        if clip:
            clips[clip['book']][clip['position']] = clip['content']
    clips = {k: v for k, v in clips.items() if v}

    export_txt(clips)

if __name__ == "__main__":
    main()
