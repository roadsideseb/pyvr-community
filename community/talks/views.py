from django.views import generic

from ..member.models import Member
from . import models


class SpeakerList(generic.ListView):
    model = Member
    context_object_name = 'speakers'
    template_name = 'talks/speaker_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_speaker=True)


class TalkList(generic.ListView):
    model = models.Talk
    context_object_name = 'talks'
    template_name = 'talks/talk_list.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-presented_on', 'title')
