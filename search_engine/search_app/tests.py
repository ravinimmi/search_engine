from django.test import TestCase, Client


class SearchAPITest(TestCase):
    maxDiff = None

    def test_search(self):
        expected_response = [
            [
                {
                    "id": 0,
                    "summary": "The Book in Three Sentences: Practicing meditation and mindfulness will make you at least 10 percent happier. Being mindful doesn’t change the problems in your life, but mindfulness does help you respond to your problems rather than react to them. Mindfulness helps you realize that striving for success is fine as long as you accept that the outcome is outside your control.",
                    "query": "is your problems",
                    "author": "Dan Harris"
                },
                {
                    "id": 7,
                    "summary": "The Book in Three Sentences: Everything in life is an invention. If you choose to look at your life in a new way, then suddenly your problems fade away. One of the best ways to do this is to focus on the possibilities surrounding you in any situation rather than slipping into the default mode of measuring and comparing your life to others.",
                    "query": "is your problems",
                    "author": "Rosamund Zander and Benjamin Zander"
                },
                {
                    "id": 48,
                    "summary": "The Book in Three Sentences: Finding something important and meaningful in your life is the most productive use of your time and energy. This is true because every life has problems associated with it and finding meaning in your life will help you sustain the effort needed to overcome the particular problems you face. Thus, we can say that the key to living a good life is not giving a fuck about more things, but rather, giving a fuck only about the things that align with your personal values.",
                    "query": "is your problems",
                    "author": "Mark Manson"
                }
            ],
            [
                {
                    "id": 1,
                    "summary": "The Book in Three Sentences: The 10X Rule says that 1) you should set targets for yourself that are 10X greater than what you believe you can achieve and 2) you should take actions that are 10X greater than what you believe are necessary to achieve your goals. The biggest mistake most people make in life is not setting goals high enough. Taking massive action is the only way to fulfill your true potential.",
                    "query": "achieve take book",
                    "author": "Grant Cardone"
                },
                {
                    "id": 12,
                    "summary": "The Book in Three Sentences: The compound effect is the strategy of reaping huge rewards from small, seemingly insignificant actions. You cannot improve something until you measure it. Always take 100 percent responsibility for everything that happens to you.",
                    "query": "achieve take book",
                    "author": "Darren Hardy"
                },
                {
                    "id": 14,
                    "summary": "The Book in Three Sentences: Ultimately, profit is the only valid metric for guiding a company, and there are only three ways to influence profit: price, volume, and cost. Of these three factors, prices get the least attention, but have the greatest impact. The price a customer is willing to pay, and therefore the price a company can achieve, is always a reflection of the perceived value of the product or service in the customer’s eyes.",
                    "query": "achieve take book",
                    "author": "Hermann Simon"
                }
            ]
        ]

        client = Client()
        data = {
            'queries': ["is your problems", "achieve take book"],
            'K': 3
        }
        response = client.post('/search-app/search/', data, content_type='application/json').json()
        self.assertEqual(response, expected_response)

    def test_invalid_input(self):
        client = Client()
        data = {
            'queries': ["is your problems", "achieve take book"]
        }
        response = client.post('/search-app/search/', data, content_type='application/json')
        self.assertEquals(response.status_code, 400)
