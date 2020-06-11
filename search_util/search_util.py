import json
import string
from collections import defaultdict
from collections import Counter


class SearchUtil:

    def __init__(self, summaries=[]):
        self.summaries = summaries
        self.inverted_index = defaultdict(set)

    def load_data(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.summaries = data['summaries']

    def _clean_keyword(self, keyword):
        return keyword.lower().strip(string.punctuation)

    def generate_inverted_indices(self):
        '''
        Generates inverted index for each summary. index is a dictionary
        mapping keyword to summary objects which contain the keyword.

        e.g.
        If self.inverted_index['human'] gives {34, 37, 50, 24, 29}
        keyword 'human' is present in summary objects at index 34, 37, 50, 24
        and 29
        '''
        for idx, summary in enumerate(self.summaries):
            for keyword in summary['summary'].split():
                clean_keyword = self._clean_keyword(keyword)
                if clean_keyword != '':
                    self.inverted_index[clean_keyword].add(idx)

    def search(self, query, k):
        '''
        Input: The input is a user query of type string and number of
        items to return
        query (string): eg. 'is your problems'
        k (integer): eg. 3

        Output: List of k relevant summaries sorted according to order of
        relevance given a query. A summary is a dictionary that follows the
        schema: { 'summary ': string, 'id ': integer}
        '''

        keywords = query.split()
        keywords = [self._clean_keyword(kw) for kw in keywords]

        relevant_summary_indices = []
        for keyword in keywords:
            matched_summary_indices = list(self.inverted_index[keyword])
            relevant_summary_indices.extend(matched_summary_indices)

        counter = Counter(relevant_summary_indices)
        matched_indices_with_count = counter.items()
        matched_indices_with_count = sorted(matched_indices_with_count, key=lambda x: (-x[1], x[0]))
        matched_indices_with_count = matched_indices_with_count[:k]
        k_relevant_summary_indices = [item[0] for item in matched_indices_with_count]

        return [self.summaries[idx] for idx in k_relevant_summary_indices]
