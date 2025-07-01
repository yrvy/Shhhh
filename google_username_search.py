import argparse
try:
    from googlesearch import search
except ImportError:
    search = None
    import sys
    print('googlesearch library not installed. Install via pip install google')


def search_username(username, num_results=10):
    if search is None:
        raise RuntimeError('googlesearch library not available')
    query = f'"{username}"'
    results = []
    for url in search(query, num_results=num_results, stop=num_results):
        results.append(url)
    return results


def main():
    parser = argparse.ArgumentParser(description='Search Google for occurrences of a username.')
    parser.add_argument('username', help='Username to search for')
    parser.add_argument('-n', '--num', type=int, default=10, help='Number of results to return')
    args = parser.parse_args()
    try:
        results = search_username(args.username, args.num)
        for link in results:
            print(link)
    except Exception as e:
        print(f'Error performing search: {e}')


if __name__ == '__main__':
    main()
