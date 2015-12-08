# -*- coding: utf-8 -*-
import re
import requests

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from community.member.models import MeetupUser, SocialLink


class Command(BaseCommand):
    help = 'Find social links for a meetup user'

    def add_arguments(self, parser):
        parser.add_argument('--override', default=False, action='store_true')

    def handle(self, *args, **options):
        override = options['override']

        for meetup_user in MeetupUser.objects.all():
            if not meetup_user.groups:
                continue

            url = meetup_user.get_meetup_page(meetup_user.groups[0])
            print('Requesting {}'.format(url))

            response = requests.get(url)

            if not response.ok or not response.content:
                print('something went wrong: {}'.format(response.reason))
                continue

            member_page = BeautifulSoup(response.content, 'html.parser')

            link_elements = member_page.select('div.D_memberProfileSocial a')

            if not link_elements:
                continue

            for elem in link_elements:
                link = elem.get('href')
                if not link:
                    continue

                site = SocialLink.get_site_from_url(link)

                if not site:
                    continue

                link, __ = meetup_user.social_links.get_or_create(
                    site=site, url=link)

                member = meetup_user.member

                if site == SocialLink.TWITTER:
                    if not member.twitter or override:
                        REGEX = re.compile(r'^https?:\/\/.+\/(?P<handle>[\w]+)\/?$')
                        res = REGEX.match(link.url).group('handle')

                        if res:
                            print('TWITTER {}'.format(res))
                            member.twitter = res

                if site == SocialLink.LINKEDIN:
                    if not member.linkedin or override:
                        print('LinkedIn {}'.format(link.url))
                        member.linkedin = link.url

                member.save()
