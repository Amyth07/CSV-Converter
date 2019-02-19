import io
import os
import csv
import json
from validators.url import url

filename = "data.csv"


def is_valid_name(name):
    if isinstance(name.get('name'), str):
        return True
    return False


def is_valid_url(uri):
    if url(uri.get('uri')):
        return True
    return False


def is_valid_stars(star):
    if 0 <= int(star.get('stars')) <= 5:
        return True
    return False


def validate_fields(line):
    if is_valid_name(line) and is_valid_url(line) and is_valid_stars(line):
        return True
    return False


def convert_row_to_xml(row):
    return f"""<data>
        <name>{row.get('name')}</name>
        <address>{row.get('address')}</address>
        <stars>{row.get('stars')}</stars>
        <phone>{row.get('phone')}</phone>
        <uri>{row.get('uri')}</uri>
    </data>\n"""


def generate_json_file(rows, cwd):
    filepath = '\\data.json'
    with io.open(cwd + filepath, 'w', encoding='UTF8') as f:
        json.dump(rows, f, ensure_ascii=False)


def generate_xml_file(rows, cwd):
    filepath = '\\data.xml'
    with io.open(cwd + filepath, 'w') as f:
        f.write('<dataListings>')
        for line in rows:
            f.write(convert_row_to_xml(line))
        f.write('</dataListings>')


def driver():
    cwd = os.getcwd()
    if os.path.isfile(filename):
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list()

            next(csv_reader)
            for line in csv_reader:
                if line and validate_fields(line):
                    rows.append(line)

            generate_json_file(rows, cwd + '\\data')
            generate_xml_file(rows, cwd + '\\data')


if __name__ == '__main__':
    print('CSV are being converted to JSON and XML.')
    print('....')
    driver()
    print('data.json and data.xml file generated.')