import argparse
import os
import Queue


def append_new_action(new_action):
    f = open('.actions', 'a')
    new_action += '\n'
    f.write(new_action)
    write_file_to_disk(f)


def get_first_action():
    f = open('.actions', 'r')
    action = f.readline()
    f.close()
    print action


def delete_first_action(default):
    f = open('.actions', 'r')
    lines = f.readlines()
    print 'Deleted: ' + lines.pop(0)
    f.close()

    f = open('.actions', 'w')
    f.writelines(lines)
    write_file_to_disk(f)


def cycle_to_next_action(default):
    f = open('.actions', 'r')
    lines = f.readlines()
    f.close()

    action_item = str(lines.pop(0))
    lines.append(action_item)

    f = open('.actions', 'w')
    f.writelines(lines)
    write_file_to_disk(f)


def reverse_action_queue(default):
    f = open('.actions', 'r')
    lines = f.readlines()
    f.close()

    length = len(lines)
    new_lines = []
    for n in xrange(length, 0, -1):
        # adjust for 0 index: n-1 or length-1?
        new_lines.append(lines[n-1])

    f = open('.actions', 'w')
    f.writelines(new_lines)
    write_file_to_disk(f)


def write_file_to_disk(f):
    f.flush()
    os.fsync(f.fileno())
    f.close()


def test_func(default):
    val = os.access('.actions', os.R_OK)
    print val


parser = argparse.ArgumentParser(description='Project actions')

parser.add_argument(
    '--new', '-n',
    type=append_new_action,
    help='Add a new action.',
)
parser.add_argument(
    '--action', '-a',
    nargs='?',
    default=get_first_action(),
    help='Display current action.',
)
parser.add_argument(
    '--delete', '-d',
    type=delete_first_action,
    help='Delete current action.',
)
parser.add_argument(
    '--cycle', '-c',
    type=cycle_to_next_action,
    help='Cycle to the next action',
)
parser.add_argument(
    '--reverse', '-r',
    type=reverse_action_queue,
    help='Reverse the queue.',
)
parser.add_argument(
    '-t',
    type=test_func,
)
options = parser.parse_args()

action_filename = '.actions'

