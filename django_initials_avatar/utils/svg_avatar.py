class SVGAvatar:

    @classmethod
    def name_to_letters(cls, name: str, length: int) -> str:
        name_parts = list(map(lambda part: str(part)[0], name.split(' ')))

        if length > 1 and len(name_parts) > 1:
            new_length = length - 2

            if new_length > 0:
                first_letter = name_parts[0]
                last_letter = name_parts[-1]
                middle_letters = name_parts[1:new_length + 1]
                letters = ''.join([first_letter] + middle_letters + [last_letter])
            else:
                letters = ''.join([name_parts[0], name_parts[-1]])

            return letters
        else:
            return name_parts[0]

    @classmethod
    def render(cls, name: str, background: str, color: str, text_length: int, avatar_width: int, avatar_height: int,
               font_size: int,
               avatar_rounded: bool, text_capitalize: bool, text_lowercase: bool, text_bold: bool) -> str:
        letter_name = cls.name_to_letters(name, length=text_length)
        if text_capitalize:
            letter_name = letter_name.upper()
        elif text_lowercase:
            letter_name = letter_name.lower()

        style = "font-weight:700;" if text_bold else ""
        return f'<svg style="{style}" width="{avatar_width}px" height="{avatar_height}px" ' \
               f'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs>' \
               f'<style type="text/css">' \
               '@font-face {font-family: "montserratbold";src: url("https://cdn.oxro.io/fonts/montserrat-bold-webfont.woff2") format("woff2"),' \
               'url("https://cdn.oxro.io/fonts/montserrat-bold-webfont.woff") format("woff");' \
               'font-weight: normal;font-style: normal;}</style></defs>' \
               f'<rect x="0" y="0" width="500" height="500" rx="{50 if avatar_rounded else 0}" ry="{50 if avatar_rounded else 0}" ' \
               f'style="fill:{background}"/>' \
               f'<text x="50%" y="50%" dy=".1em" fill="{color}" ' \
               f'text-anchor="middle" dominant-baseline="middle" ' \
               f'style="font-family: &quot;Montserrat&quot;, sans-serif; font-size: {font_size}px; line-height: 1">' \
               f'{letter_name}</text>' \
               f'</svg>'