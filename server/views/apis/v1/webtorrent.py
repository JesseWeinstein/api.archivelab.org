#!/usr/bin/env python
#-*-coding: utf-8 -*-

"""
    webtorrent.py
    ~~~~~~~~~~~~~

    Support for webtorrents of IA items.

    :copyright: (c) 2016 by Internet Archive
    :license: see LICENSE for more details.
"""

import bencode
from flask import Response
from flask.views import MethodView
from api import mimetype, download
from .items import File, Files


class Torrent(MethodView):
    def get(self, iid):
        """ Return a torrent with the webseed set correctly for webtorrents
        """
        fs = ''.join(list(download(iid, iid + '_archive.torrent')))
        t = bencode.bdecode(fs)
        t['url-list'] = ['https://api.archive.org/v2/webtorrents/files/']
        return Response(
            bencode.bencode(t),
            mimetype=mimetype(iid + '_archive.torrent')
        )


urls = (
    '/files/<iid>/<filename>', File,
    '/files/<iid>/', Files,
    '/torrents/<iid>', Torrent
  )
