import argparse


def get_station_parser():
    station_parser = argparse.ArgumentParser()
    station_parser.add_argument('--find', type=str, default="", help="Word you want to Find and replace")
    station_parser.add_argument('--replace', type=str, default="", help="Replacement Word!")
    args = station_parser.parse_args()

    return args