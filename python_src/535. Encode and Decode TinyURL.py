#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2017/8/27'
__time__ = '14:54'

import base64


class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        bytesString = longUrl.encode(encoding="utf-8")
        encodestr = base64.b64encode(bytesString)
        return 'http://tinyurl.com/' + encodestr

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        decodestr = base64.b64decode(shortUrl.split('http://tinyurl.com/')[1])
        return decodestr