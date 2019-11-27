#! /usr/bin/env python

"""
Convert CSV to (nested) YAML

Usage:
  csv2yaml [-d <CHAR>] <csv>

Options:
  -d <CHAR>  :  Delimiter character [default: auto]
  <csv>      :  Input CSV/TSV

"""

import yaml
import pandas as pd
from docopt import docopt


def _delimiter(path):
    with open(path, 'r') as f:
        txt = f.read()

        delimiter = None
        count_max = 0
        for d in [',', '\t', '|']:
            _count = txt.count(d)
            if _count > count_max:
                count_max = _count
                delimiter = d

    if not delimiter:
        raise('Delimiter could not be determined.')

    return delimiter


def _row_to_dict(row: pd.Series):
    dict_ = None

    for item in reversed(row):
        dict_ = {item: dict_} if dict_ else item

    return dict_


# NOTE: With reference to stack overflow
# https://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge
def _merge_dict(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            # NOTE: When the dict is nested, make a recursive call
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(_merge_dict(dict1[k], dict2[k])))
            else:
                yield (k, dict2[k])
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])


def main():
    options = docopt(__doc__)

    input_path = options['<csv>']
    delimiter = options['-d']
    if delimiter == 'auto':
        delimiter = _delimiter(input_path)

    csv_df = pd.read_table(input_path, delimiter=delimiter, header=None)
    dicts = [_row_to_dict(r) for i, r in csv_df.iterrows()]

    merged_dict = None
    for d in dicts:
        if not merged_dict:
            merged_dict = d
            continue

        merged_dict = dict(_merge_dict(merged_dict, d))

    print(yaml.dump(merged_dict))


if __name__ == '__main__':
    main()
