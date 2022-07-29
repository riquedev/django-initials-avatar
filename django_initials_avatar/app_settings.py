from django.conf import settings

BG_COLORS = getattr(settings, 'INITIALS_AVATAR_BG_COLORS', [
    "#E284B3", "#FFED8B", "#681313", "#F3C1C6", "#735372", "#009975", "#FFBD39", "#B1E8ED", "#52437B", "#F76262",
    "#216583", "#293462", "#DD9D52", "#936B93", "#6DD38D", "#888888", "#6F8190", "#BCA0F0", "#AAF4DD", "#96C2ED",
    "#3593CE", "#5EE2CD", "#96366E", "#E38080"
])
TEXT_COLOR = getattr(settings, 'INITIALS_AVATAR_TEXT_COLOR', '#fff')
TEXT_LENGTH = getattr(settings, 'INITIALS_AVATAR_TEXT_LENGTH', 2)
WIDTH = getattr(settings, 'INITIALS_AVATAR_WIDTH', 500)
HEIGHT = getattr(settings, 'INITIALS_AVATAR_HEIGHT', 500)
FONT_SIZE = getattr(settings, 'INITIALS_AVATAR_FONT_SIZE', 250)
ROUNDED = getattr(settings, 'INITIALS_AVATAR_ROUNDED', False)
CAPITALIZE = getattr(settings, 'INITIALS_AVATAR_CAPITALIZE', False)
LOWERCASE = getattr(settings, 'INITIALS_AVATAR_LOWERCASE', False)
BOLD = getattr(settings, 'INITIALS_AVATAR_BOLD', True)
CACHE_TIMEOUT = getattr(settings, 'INITIALS_AVATAR_CACHE_TIMEOUT', 60 * 60)