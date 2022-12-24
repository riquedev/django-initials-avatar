import unittest, pathlib
from django_initials_avatar.utils.svg_avatar import SVGAvatar
from django_initials_avatar.templatetags.initials_avatar import render_initials_avatar


_ROOT = pathlib.Path(__file__).parent.absolute()
class TestUtils(unittest.TestCase):

    def test_name_to_letters(self):
        self.assertEqual(SVGAvatar.name_to_letters('Henrique da Silva Santos', 1), 'H')
        self.assertEqual(SVGAvatar.name_to_letters('Henrique da Silva Santos', 2), 'HS')
        self.assertEqual(SVGAvatar.name_to_letters('Henrique da Silva Santos', 3), 'HdS')
        self.assertEqual(SVGAvatar.name_to_letters('Henrique da Silva Santos', 4), 'HdSS')
        self.assertEqual(SVGAvatar.name_to_letters('Henrique', 4), 'H')

    def test_issue_1(self):
        """
        This test is for resolve the issue mentioned in
        https://github.com/riquedev/django-initials-avatar/issues/1
        """

        with open(_ROOT / 'data' / 'issue_1.txt','r') as handler:

            for word in handler.readlines():
                self.assertTrue(SVGAvatar.name_to_letters(word, 1) == word[0])

                with self.assertRaises(TypeError):
                    render_initials_avatar(name=word, old_method=True)

                self.assertIsInstance(render_initials_avatar(name=word), str)



    def test_render(self):
        expected_svg = """<svg style="font-weight:700;" width="500px" height="500px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><style type="text/css">@font-face {font-family: "montserratbold";src: url("https://cdn.oxro.io/fonts/montserrat-bold-webfont.woff2") format("woff2"),url("https://cdn.oxro.io/fonts/montserrat-bold-webfont.woff") format("woff");font-weight: normal;font-style: normal;}</style></defs><rect x="0" y="0" width="500" height="500" rx="50" ry="50" style="fill:#fff"/><text x="50%" y="50%" dy=".1em" fill="#252525" text-anchor="middle" dominant-baseline="middle" style="font-family: &quot;Montserrat&quot;, sans-serif; font-size: 250px; line-height: 1">hs</text></svg>"""
        svg = SVGAvatar.render(
            name="Henrique da Silva Santos",
            background="#fff",
            color="#252525",
            text_length=2,
            avatar_width=500,
            avatar_height=500,
            font_size=250,
            avatar_rounded=True,
            text_capitalize=False,
            text_lowercase=True,
            text_bold=True
        )
        self.assertEqual(svg, expected_svg)


if __name__ == '__main__':
    unittest.main()
