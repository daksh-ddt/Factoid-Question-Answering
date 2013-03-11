# -*- coding: utf-8 -*-
import unicodedata


def safe_unicode(obj, *args):
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def remove_accents(s):
    s = safe_unicode(s)
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')