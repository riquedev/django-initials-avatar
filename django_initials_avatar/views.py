import random
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View
from django.http import HttpResponse
from django_initials_avatar.app_settings import (CACHE_TIMEOUT, BG_COLORS,
                                                 TEXT_COLOR, TEXT_LENGTH, WIDTH, HEIGHT, FONT_SIZE, ROUNDED,
                                                 CAPITALIZE, LOWERCASE, BOLD)
from django_initials_avatar.utils.svg_avatar import SVGAvatar


class BaseAvatarView(View):

    @property
    def name(self) -> str:
        return str(self.request.GET.get('name'))

    @property
    def background(self) -> str:
        return str(self.request.GET.get('background', random.choice(BG_COLORS)))

    @property
    def color(self) -> str:
        return str(self.request.GET.get('color', TEXT_COLOR))

    @property
    def text_length(self) -> int:
        return int(self.request.GET.get('length', TEXT_LENGTH))

    @property
    def avatar_width(self) -> int:
        return int(self.request.GET.get('width', WIDTH))

    @property
    def avatar_height(self) -> int:
        return int(self.request.GET.get('height', HEIGHT))

    @property
    def font_size(self) -> int:
        return int(self.request.GET.get('size', FONT_SIZE))

    @property
    def avatar_rounded(self) -> bool:
        return bool(self.request.GET.get('rounded', ROUNDED))

    @property
    def text_capitalize(self) -> bool:
        return bool(self.request.GET.get('capitalize', CAPITALIZE))

    @property
    def text_lowercase(self) -> bool:
        return bool(self.request.GET.get('lowercase', LOWERCASE))

    @property
    def text_bold(self) -> bool:
        return bool(self.request.GET.get('bold', BOLD))


@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class SVGInitialsAvatarView(BaseAvatarView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(
            SVGAvatar.render(
                name=self.name,
                background=self.background,
                color=self.color,
                text_length=self.text_length,
                avatar_width=self.avatar_width,
                avatar_height=self.avatar_height,
                font_size=self.font_size,
                avatar_rounded=self.avatar_rounded,
                text_capitalize=self.text_capitalize,
                text_lowercase=self.text_lowercase,
                text_bold=self.text_bold
            ),
            content_type='image/svg+xml'
        )