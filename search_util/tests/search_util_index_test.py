import unittest
from search_util import SearchUtil


class TestSearchUtilInvertedIndex(unittest.TestCase):
    def setUp(self):
        summaries = [
            {
                "id": 0,
                "summary": "The Book in Three Sentences: Practicing meditation and mindfulness will make you at least 10 percent happier. Being mindful doesn\u2019t change the problems in your life, but mindfulness does help you respond to your problems rather than react to them. Mindfulness helps you realize that striving for success is fine as long as you accept that the outcome is outside your control."
            },
            {
                "id": 1,
                "summary": "The Book in Three Sentences: The 10X Rule says that 1) you should set targets for yourself that are 10X greater than what you believe you can achieve and 2) you should take actions that are 10X greater than what you believe are necessary to achieve your goals. The biggest mistake most people make in life is not setting goals high enough. Taking massive action is the only way to fulfill your true potential."
            },
            {
                "id": 2,
                "summary": "The Book in Three Sentences: The only thing you have that nobody else has is control of your life. The hardest thing of all is to learn to love the journey, not the destination. Get a real life rather than frantically chasing the next level of success."
            },
            {
                "id": 3,
                "summary": "The Book in Three Sentences:\u00a0An idea occurs when you develop a new combination of old elements.\u00a0The capacity to bring old elements into new combinations depends largely on your ability to see relationships. All ideas follow a five-step process of 1) gathering material, 2) intensely working over the material in your mind, 3) stepping away from the problem, 4) allowing the idea to come back to you naturally, and 5) testing your idea in the real world and adjusting it based on feedback."
            },
        ]
        self.su = SearchUtil(summaries=summaries)
        self.su.generate_inverted_indices()

    def test_indexing(self):
        self.assertEqual(self.su.inverted_index['idea'], {3})
        self.assertEqual(self.su.inverted_index['chasing'], {2})
        self.assertEqual(self.su.inverted_index['for'], {0, 1})

    def test_special_chars(self):
        self.assertEqual(self.su.inverted_index['happier'], {0})

    def test_upper_case_chars(self):
        self.assertEqual(self.su.inverted_index['practicing'], {0})
