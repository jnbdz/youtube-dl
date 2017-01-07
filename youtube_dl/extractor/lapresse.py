# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor


class LaPresseIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?lapresse\.ca/videos/(?:[^/]+/)+(?P<id>\w+)'
    _TEST = {
        'url': 'http://www.lapresse.ca/videos/vivre/201611/18/46-1-pas-incontournable-mais.php/6597c012a8204a26a29108e43144e2bc',
        'info_dict': {
            'id': '6597c012a8204a26a29108e43144e2bc',
            'ext': 'flv',
            'title': 'Pas incontournable, mais... | Vidéos LaPresse.ca',
            'description': 'Vidéo de LaPresse.ca',
            'uploader_id': '',
            'timestamp': '',
            'upload_date': '',
        },
        'add_ie': ['BrightcoveNew'],
    }

    def _real_extract(self, url):
        brightcove_id = self._match_id(url)
        return ""