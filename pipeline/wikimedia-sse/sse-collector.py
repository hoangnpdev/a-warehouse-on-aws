import argparse
import json
from requests_sse import EventSource
import datetime
import csv
from typing import TypedDict

BATCH_PERIOD = 5  # minutes


class WikiEvent(TypedDict):
    timestamp: int | None
    title: str | None
    user: str | None
    comment: str | None
    wiki: str | None
    type: str | None
    user: str | None
    bot: bool | None
    length: dict | None


def collect_wiki_recent_change():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datetime",
                        dest="datetime",
                        required=True,
                        help="Please use the datetime format: %Y-%m-%dT%H:%M:%S")
    args = parser.parse_args()
    since = args.datetime
    start_time = datetime.datetime.strptime(since, '%Y-%m-%dT%H:%M:%S')
    url = f'https://stream.wikimedia.org/v2/stream/recentchange?since={since}'
    print(f'url: {url}')
    with EventSource(url) as stream:
        current_batch = start_time  # timestamp each 5 minutes
        data = []
        print('before loop')
        for event in stream:
            if event.type == 'message':
                change = json.loads(event.data)
                if 'timestamp' not in change:
                    print('no timestamp')
                    continue
                current_time = datetime.datetime.utcfromtimestamp(change['timestamp'])
                if current_time >= start_time + datetime.timedelta(hours=24, minutes=BATCH_PERIOD):
                    break
                if current_time >= current_batch + datetime.timedelta(minutes=BATCH_PERIOD):
                    print(f'batch size: {len(data)}, current: {current_time.isoformat()}')
                    save_batch(data, f'{current_batch.isoformat()}.csv')
                    current_batch = current_batch + datetime.timedelta(minutes=BATCH_PERIOD)
                    data = []

                if current_time < start_time + datetime.timedelta(hours=24):
                    data.append(extract_change(change))


def extract_change(change: WikiEvent):
    edit_size = 0
    if 'length' in change and 'new' in change['length'] and 'old' in change['length']:
        edit_size = change['length']['new'] - change['length']['old']
    return [change['title'], change['timestamp'], change['wiki'],
            change['user'], change['comment'], change['bot'],
            change['type'], edit_size]


def save_batch(data, path):
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(data)


collect_wiki_recent_change()
