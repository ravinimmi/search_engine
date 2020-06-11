import json
import sys

from search_util import SearchUtil


if __name__ == '__main__':
    su = SearchUtil()
    su.load_data(sys.argv[1])
    su.generate_inverted_indices()
    res = su.search('is your problems', 5)
    for summary in res:
        print(json.dumps(summary, indent=4))
