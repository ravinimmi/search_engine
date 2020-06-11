import json
from collections import defaultdict
from collections import Counter


class SearchUtil:

    def __init__(self):
        self.summaries = []
        self.inverted_index = defaultdict(set)

    def load_data(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.summaries = data['summaries']

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
                self.inverted_index[keyword].add(idx)

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

        relevant_summary_indices = []
        for keyword in keywords:
            matched_summary_indices = list(self.inverted_index[keyword])
            relevant_summary_indices.extend(matched_summary_indices)

        counter = Counter(relevant_summary_indices)
        matched_indices_with_count = counter.most_common(k)
        k_relevant_summary_indices = [item[0] for item in matched_indices_with_count]

        return [self.summaries[idx] for idx in k_relevant_summary_indices]
