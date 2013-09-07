import argparse


def test_func(a):
    print('hello')


parser = argparse.ArgumentParser(description='Test example')

parser.add_argument(
    '-t',

    dest='a',
    type=test_func,
    help='Display current action.',
)
parser.add_argument(
    '-b',
    dest='b',
    action='store_true',
)


options = parser.parse_args()


print(options.b)

