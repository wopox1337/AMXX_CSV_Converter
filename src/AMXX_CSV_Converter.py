import csv
import configparser
import os
import sys
import errno
import ctypes
import platform

__version__ = "1.0.1"


def Convert_CSV_to_INI(input, output, encoding='utf-8'):
    iniWriter = configparser.RawConfigParser()
    iniWriter.optionxform = str
    try:
        with open(input, newline='', encoding=encoding) as csvfile:
            csvReader = csv.DictReader(csvfile)
            for row in csvReader:
                key = ''
                for lang in row:
                    if(lang == ''):
                        key = row[lang]
                        # _print(f'key = {row[lang]}')
                    else:
                        if(not iniWriter.has_section(lang)):
                            iniWriter[lang] = {}
                        # if(row[lang] == ''):
                            # row[lang] = '-'
                        # _print(f'\t[{lang}] {key} = {row[lang]}')
                        if(row[lang]):
                            iniWriter.set(lang, key, row[lang])
    except Exception as err:
        _print(f'\tERROR: {err.args[1]}: "{input}"')
        sys.exit(2)
    try:
        dirName = os.path.dirname(output)
        if(not os.path.exists(dirName) and dirName):
            try:
                os.makedirs(dirName)
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
    except Exception as err:
        _print(f'\tERROR: ({err.args[1]}): "{output}"')
        sys.exit(2)
    with open(output, 'w', encoding=encoding) as configfile:
        iniWriter.write(configfile)
        _print(f'\tDONE: New lang file succefully created: "{output}"', success=1)


def Convert_INI_to_CSV(input, output, encoding='utf-8'):
    iniLang = configparser.RawConfigParser()
    iniLang.optionxform = str
    try:
        iniLang.read(input, encoding=encoding)

        if(len(iniLang.sections()) < 1):
            _print(f'No have sections to parse in file {input}')
            return
        try:
            with(open(output, 'w', encoding=encoding, newline='')) as CSVfile:
                csvWriter = csv.writer(CSVfile, delimiter=',')
                sections = iniLang.sections()
                csvWriter.writerow(['', *sections])
                keys = []
                values = []
                for lang in sections:
                    for key in iniLang.options(lang):
                        if(key not in keys):
                            keys.append(key)
                for lang in sections:
                    valuesForLang = []
                    for key in keys:
                        valuesForLang.append(iniLang.get(lang, key) if iniLang.has_option(lang, key) else '')
                    values.append(valuesForLang)
                rows = zip(keys, *values)
                for row in rows:
                    csvWriter.writerow(row)

                _print(f'\tDONE: New lang file succefully created: "{output}"', success=1)
        except Exception as err:
            _print(f'\tERROR: {err.args[1]}: "{output}"')
            sys.exit(2)
    except Exception as err:
        _print(f'\tERROR: {err.args}: "{input}"')
        sys.exit(2)


def main(argv):
    args_count = len(argv)

    if(args_count < 2):
        programmName = os.path.basename(sys.argv[0])
        _print(f''' Usage: {programmName} <inputfile> <outputfile> <encoding>
    Examples:
{programmName} file.csv file.ini (Converts .csv -> .ini)
{programmName} file.ini file.csv (Converts .ini -> .csv)
{programmName} file.ini (Converts file.ini -> file.csv)
{programmName} file.csv (Converts file.csv -> file.ini)
        ''')
        sys.exit(2)

    inputFile = argv[1]

    if(not os.path.isfile(inputFile)):
        _print(f' \tERROR: Not found file: "{inputFile}"')
        sys.exit(2)

    encoding = argv[3] if(len(argv) > 3) else 'utf-8'

    if('.csv' in inputFile):
        outputFile = (
            inputFile.replace('.csv', '.ini') if (args_count == 2) else argv[2]
        )
        Convert_CSV_to_INI(inputFile, outputFile, encoding)
    elif('.ini' in inputFile or '.txt' in inputFile):
        outputFile = (
            inputFile.replace('.ini', '.csv').replace('.txt', '.csv') if (args_count == 2) else argv[2]
        )
        Convert_INI_to_CSV(inputFile, outputFile, encoding)

    sys.exit(0)


def _print(text, success=0):
    print(text)
    if(platform.system() == 'Windows'):
        ctypes.windll.user32.MessageBoxW(
            0, text.strip(), getAppName(), 0x00000040 if(success == 1) else 0x00000010)


def getAppName():
    return os.path.basename(sys.argv[0]).replace('.exe', '').replace('.py', '') \
        + ' ' + __version__


if __name__ == "__main__":
    main(sys.argv)
