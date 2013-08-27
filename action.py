import os
import argparse
import Queue


def get_working_action():
    pass

def add_action_to_queue():
    pass

def delete_working_action():
    pass


def test_func(default):
    print('printing test function')

parser = argparse.ArgumentParser(description='Active action tracker.')

parser.add_argument(
    '-t',
    type=test_func,
)

options = parser.parse_args()
