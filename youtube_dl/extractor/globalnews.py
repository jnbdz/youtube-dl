# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor


class GlobalNewsPlayerFeedIE(InfoExtractor):
    _VALID_URL = r'http://feed.theplatform.com/f/dtjsEC/FCT_FJTDVpVT?form=json&byId='
    _TEST = {
        'url': 'http://feed.theplatform.com/f/dtjsEC/FCT_FJTDVpVT?form=json&byId=833310275627',
        'info_dict': {
            'id': '833310275627',
            'ext': 'mp4',
            'title': 'L’industrie du taxi dénonce l’entente entre Québec et Uber: explications',
            'description': 'md5:479653b7c8cf115747bf5118066bd8b3',
            'uploader_id': '1741764581',
            'timestamp': 1473352030,
            'upload_date': '20160908',
        },
    }

    @staticmethod
    def _extract_url(webpage):
        a_m = re.search(
            r'"(?P<url>https?:\\/\\/feed\.theplatform\.com[^"]+)"', webpage)
        if a_m:
            return a_m.group('url')

    @staticmethod
    def _extract_id(webpage):
        svp_m = re.search(
            r'svp\[\'gncaRid\'\] = \'(?P<id>\d+)\'\;', webpage)
        platform_account_m = re.search(
            r'svp\.platformAccount = \"(?P<id>\w+\/?)\"\;', webpage)
        feed_id_m = re.search(
            r'svp\.feedId = \"(?P<id>\w+)\"\;', webpage)

        #'http://feed.theplatform.com/f/dtjsEC/FCT_FJTDVpVT?form=json&byId=' + svp_m.group('id')

        if platform_account_m:
            if feed_id_m:
                if svp_m:
                    return svp_m.group('id')

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        self._download_json(url, video_id, None, err, None, True, 'UTF-8', None)
        exit()

class GlobalNewsPlayerIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?globalnews\.ca/video/embed/(?P<id>\d+)/'
    _TEST = {
        'url': 'http://globalnews.ca/video/embed/3140129/#autoplay',
        'info_dict': {
            'id': '3140129',
            'ext': 'mp4',
            'title': 'L’industrie du taxi dénonce l’entente entre Québec et Uber: explications',
            'description': 'md5:479653b7c8cf115747bf5118066bd8b3',
            'uploader_id': '1741764581',
            'timestamp': 1473352030,
            'upload_date': '20160908',
        },
    }

    @staticmethod
    def _extract_url(webpage):
        a_m = re.search(
            r'<a[^>]+data-displayinline="(?P<url>https?://globalnews\.ca/[^"]+)"', webpage)
        if a_m:
            return a_m.group('url')

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        exit()


class GlobalNewsIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?globalnews\.ca/news/(?P<id>\d+)/'
    _TEST = {
        'url': 'http://globalnews.ca/news/3141130/mother-of-boys-killed-in-spruce-grove-stresses-she-had-primary-care-in-online-post/',
        'info_dict': {
            'id': '',
            'ext': 'mp4',
            'title': 'L’industrie du taxi dénonce l’entente entre Québec et Uber: explications',
            'description': 'md5:479653b7c8cf115747bf5118066bd8b3',
            'uploader_id': '1741764581',
            'timestamp': 1473352030,
            'upload_date': '20160908',
        },
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        return self.url_result(
            GlobalNewsPlayerIE._extract_url(webpage), 'GlobalNewsPlayer')

