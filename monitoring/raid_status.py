#! /usr/bin/env python3

import json
import subprocess

from argparse import ArgumentParser
from pprint import pprint
from prettytable import PrettyTable


def get_raid_detail(array):
    out = subprocess.run(
        f'sudo mdadm --detail {array}',
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return out.stdout.decode('utf-8')


def detail_to_dict(detail):
    d_list = [i.strip().split(':', 1) for i in detail.split('\n') if i != ''][:-3]
    array_name = d_list[0][0]
    array_list = d_list[1:]
    d_dict = {}
    for item in array_list:
        d_dict['name'] = array_name
        if item is not None:
            key, value = item
            d_dict[key.strip()] = value.strip()
    return d_dict


def main():
    parser = ArgumentParser()
    parser.add_argument('array_names', type=str, nargs='+')
    parser.add_argument('-v', '--values', type=str, nargs='+')
    parser.add_argument('--pretty', action='store_true')
    args = parser.parse_args()
    array_output = []
    for array_name in args.array_names:
        try:
            detail_dict = get_raid_detail(array_name)
        except Exception:
            raise
        array_output.append(detail_to_dict(detail_dict))
    if args.values:
        prettytable = PrettyTable(border=False, header=False)
        header_row = ['name']
        header_row.extend(args.values)
        prettytable.field_names = header_row
        for i in array_output:
            row_list = [i['name']]
            for value in args.values:
                row_list.append(i[value])
            prettytable.add_row(row_list)
        print(prettytable)
    elif args.pretty:
        pprint(array_output)
    else:
        print(json.dumps(array_output))


if __name__ == '__main__':
    main()
