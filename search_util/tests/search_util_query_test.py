import unittest
from search_util import SearchUtil


class TestSearchUtilQuery(unittest.TestCase):
    def setUp(self):
        self.su = SearchUtil()
        self.su.load_data('data.json')
        self.su.generate_inverted_indices()

    def test_query_upper_case(self):
        query = 'Is youR Problems'
        k = 3
        results = [
            {
                'id': 0,
                'summary': 'The Book in Three Sentences: Practicing meditation and mindfulness will make you at least 10 percent happier. Being mindful doesn’t change the problems in your life, but mindfulness does help you respond to your problems rather than react to them. Mindfulness helps you realize that striving for success is fine as long as you accept that the outcome is outside your control.'
            },
            {
                'id': 7,
                'summary': 'The Book in Three Sentences: Everything in life is an invention. If you choose to look at your life in a new way, then suddenly your problems fade away. One of the best ways to do this is to focus on the possibilities surrounding you in any situation rather than slipping into the default mode of measuring and comparing your life to others.'
            },
            {
                'id': 48,
                'summary': 'The Book in Three Sentences:\xa0Finding something important and meaningful in your life is the most productive use of your time and energy. This is true because every life has problems associated with it and finding meaning in your life will help you sustain the effort needed to overcome the particular problems you face. Thus, we can say that the key to living a good life is not giving a fuck about more things, but rather, giving a fuck only about the things that align with your personal values.'
            }
        ]
        self.assertEqual(self.su.search(query, k), results)

    def test_query_special_chars(self):
        query = 'is your. problems)'
        k = 3
        results = [
            {
                'id': 0,
                'summary': 'The Book in Three Sentences: Practicing meditation and mindfulness will make you at least 10 percent happier. Being mindful doesn’t change the problems in your life, but mindfulness does help you respond to your problems rather than react to them. Mindfulness helps you realize that striving for success is fine as long as you accept that the outcome is outside your control.'
            },
            {
                'id': 7,
                'summary': 'The Book in Three Sentences: Everything in life is an invention. If you choose to look at your life in a new way, then suddenly your problems fade away. One of the best ways to do this is to focus on the possibilities surrounding you in any situation rather than slipping into the default mode of measuring and comparing your life to others.'
            },
            {
                'id': 48,
                'summary': 'The Book in Three Sentences:\xa0Finding something important and meaningful in your life is the most productive use of your time and energy. This is true because every life has problems associated with it and finding meaning in your life will help you sustain the effort needed to overcome the particular problems you face. Thus, we can say that the key to living a good life is not giving a fuck about more things, but rather, giving a fuck only about the things that align with your personal values.'
            }
        ]
        self.assertEqual(self.su.search(query, k), results)
