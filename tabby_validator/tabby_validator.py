
from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass

import pandas


@dataclass
class ObjectInfo:
    column_names: tuple[str]
    repeatable: bool
    column_definitions: list


argument_parser = ArgumentParser("tabby_validator - a tool the reads a tabby schema and can validate a tabby document")
argument_parser.add_argument('schema_file')


def process_row(index: int,
                row: pandas.Series,
                errors: list,
                schema: dict,
                ):
    print(f'{index} {row[0]}------------------------')


def parse_schema_table(table: pandas.DataFrame) -> dict:
    errors = list()
    schema = dict()
    for index, row in table.iterrows():
        process_row(index, row, errors, schema)


def main():
    arguments = argument_parser.parse_args()
    table = pandas.read_excel(arguments.schema_file, header=None)
    print(table)
    rules = parse_schema_table(table)


if __name__ == '__main__':
    main()
