import argparse
import json
from requests_sse import EventSource
import datetime
import csv
from typing import TypedDict


class WikiEvent(TypedDict):
    timestamp: int
    title: str
    user: str
    comment: str
    wiki: str
    type: str
    user: str
    bot: bool


def collect_wiki_recent_change():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datetime", dest="datetime", help="Please use datetime format of ISO 8601")
    args = parser.parse_args()

    since = args.datetime
    start_time = datetime.datetime.fromisoformat(since)
    url = f'https//stream.wikimedia.org/v2/stream/recentchange?since={since}'
    with EventSource(url) as stream:
        current_batch = start_time  # timestamp each 5 minutes
        data = []
        for event in stream:
            if event.type == 'message':
                change = json.loads(event.data)
                current_time = datetime.datetime.utcfromtimestamp(change.timestamp)

                if current_time >= start_time + datetime.timedelta(hours=24, minutes=5):
                    break

                if current_time >= current_batch + datetime.timedelta(minutes=5):
                    save_batch(data, f'{current_batch.isoformat()}.csv')
                    current_batch = current_batch + datetime.timedelta(minutes=5)
                    data = []

                if current_time < start_time + datetime.timedelta(hours=24):
                    data.append(extract_change(change))


def extract_change(change: WikiEvent):
    return [change['timestamp'], change['title'], change['user'],
            change['comment'], change['wiki'], change['type'],
            change['user'], change['bot']]


def save_batch(data, path):
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(data)


collect_wiki_recent_change()
