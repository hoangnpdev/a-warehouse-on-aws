import argparse
import json
from requests_sse import EvenSource


def collect_wiki_recent_change():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", dest="date")
    args = parser.parse_args()

    date = args.date
    # todo format date
    url = f'https//stream.wikimedia.org/v2/stream/recentchange?since={date}'
    with EvenSource(url) as stream:
        for event in stream:
            current_batch= '' # timestamp each 5 minutes
            data = []
            if event.type == 'message':
                # todo append event to local file each 5 minutes
                change = json.loads(event.data)
                if change.timestamp > batch_period:
                    save_batch(data, f'{current_batch}.csv')
                    data = []
                    current_batch = 'next batch' # todo next batch
                if change.timestamp < date + 24 hour:
                    data.append(extract_change(change))

                if change.timestamp > date + 24 hour + 5 minutes:
                    break

def extract_change(change):
    return

def save_batch(data, path):
    return

collect_wiki_recent_change()