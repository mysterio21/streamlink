import unittest

from streamlink.plugins.schoolism import Schoolism


class TestPluginSchoolism(unittest.TestCase):
    def test_can_handle_url(self):
        should_match = [
            'https://www.schoolism.com/watchLesson.php',
        ]
        for url in should_match:
            self.assertTrue(Schoolism.can_handle_url(url))

    def test_can_handle_url_negative(self):
        should_not_match = [
            'https://www.schoolism.com',
        ]
        for url in should_not_match:
            self.assertFalse(Schoolism.can_handle_url(url))

    def test_playlist_parse_subs(self):
        with_subs = """var allVideos=[
            {sources:[{type:"application/x-mpegurl",src:"https://d8u31iyce9xic.cloudfront.net/44/2/part1.m3u8?Policy=TOKEN&Signature=TOKEN&Key-Pair-Id=TOKEN",title:"Digital Painting - Lesson 2 - Part 1",playlistTitle:"Part 1",}],        subtitles: [{
                    "default": true,
                    kind: "subtitles", srclang: "en", label: "English",
                    src:  "https://s3.amazonaws.com/schoolism-encoded/44/subtitles/2/2-1.vtt",
                }],
                },
            {sources:[{type:"application/x-mpegurl",src:"https://d8u31iyce9xic.cloudfront.net/44/2/part2.m3u8?Policy=TOKEN&Signature=TOKEN&Key-Pair-Id=TOKEN",title:"Digital Painting - Lesson 2 - Part 2",playlistTitle:"Part 2",}],        subtitles: [{
                    "default": true,
                    kind: "subtitles", srclang: "en", label: "English",
                    src:  "https://s3.amazonaws.com/schoolism-encoded/44/subtitles/2/2-2.vtt",
                }]
            }];
            """

        data = Schoolism.playlist_schema.validate(with_subs)

        self.assertIsNotNone(data)
        self.assertEqual(2, len(data))


    def test_playlist_parse(self):
        without_subs = """var allVideos=[
            {sources:[{type:"application/x-mpegurl",src:"https://d8u31iyce9xic.cloudfront.net/14/1/part1.m3u8?Policy=TOKEN&Signature=TOKEN&Key-Pair-Id=TOKEN",title:"Gesture Drawing - Lesson 1 - Part 1",playlistTitle:"Part 1",}],},
            {sources:[{type:"application/x-mpegurl",src:"https://d8u31iyce9xic.cloudfront.net/14/1/part2.m3u8?Policy=TOKEN&Signature=TOKEN&Key-Pair-Id=TOKEN",title:"Gesture Drawing - Lesson 1 - Part 2",playlistTitle:"Part 2",}]}
            ];
        """

        data = Schoolism.playlist_schema.validate(without_subs)

        self.assertIsNotNone(data)
        self.assertEqual(2, len(data))
