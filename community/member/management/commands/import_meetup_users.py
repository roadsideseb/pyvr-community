# -*- coding: utf-8 -*-
from dateutil import parser

from django.core.management.base import BaseCommand

from community.member.models import MeetupUser, Member


class Command(BaseCommand):
    help = 'Import meetup data from member list'

    def add_arguments(self, parser):
        parser.add_argument('group_name', nargs=1)
        parser.add_argument('filename', nargs='+')

    def handle(self, *args, **options):
        group_name = options['group_name']

        for filename in options['filename']:
            self.read_meetup_export(group_name, filename)

    def read_meetup_export(self, group_name, filename):
        """
        The Meetup exports are named XLS but are actually just TSV files.
        """
        with open(filename) as infile:
            header = [h.strip() for h in infile.readline().split('\t')]
            header_keys = [h.replace(' ', '_').lower() for h in header]

            for line in infile:
                record = [d.strip() for d in line.split('\t')]

                if len(record) != len(header):
                    continue

                data = dict(zip(header_keys, record))
                meetup_id = data.get('member_id')

                try:
                    meetup_user = MeetupUser.objects.get(meetup_id=meetup_id)
                except MeetupUser.DoesNotExist:
                    meetup_user = MeetupUser(meetup_id=meetup_id)
                else:
                    print('User already exists, skipping them')

                    if not hasattr(meetup_user, 'member'):
                        Member.objects.create(meetup_user=meetup_user,
                                              name=meetup_user.name)
                    continue

                meetup_user.raw_data = data
                meetup_user.name = data.get('name')
                meetup_user.location = data.get('location')
                meetup_user.groups = [group_name]

                if data.get('last_attended'):
                    meetup_user.last_attended_at = parser.parse(data.get('last_attended')).date()

                meetup_user.save()
                Member.objects.create(meetup_user=meetup_user,
                                      name=meetup_user.name)
