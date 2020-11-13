import argparse, re, io
from os import listdir
from os.path import isfile, join, isdir

te_re = re.compile(r'\{(?:{[^{}]*}|[^{}])*}', re.U | re.I | re.M | re.S)

def apply_formating(params):
    params[0] = params[0]

    params[1] = "({})".format(params[1]) if params[1] else ''

    params[2] = "\\textit{\MakeLowercase{" + params[2] + "}}" if params[2] else ''

    params[3] = "({})".format(params[3]) if params[3] else ''

    params[4] = "(\\textit{" + params[4] + "})" if params[4] else ''

    params[5] = "({})".format(params[5]) if params[5] else ''

    params[6] = params[6]
    params[7] = params[7]
    params[8] = params[8]
    return [params[i] for i in [2, 4, 5, 0, 1, 3, 6, 7, 8]]

def postprocess_tex(filename):
    with io.open(filename, 'r+', encoding='utf-8') as f:
        data = f.read()

        if '\\begin{dictionaryentry}' not in data: # no dictionary entries
            return

        entries = data.split('\end{dictionaryentry}')
        entries = [e.replace('\\begin{dictionaryentry}', '') for e in entries]

        output = []
        for e in entries:
            dictionary_entry_data = []
            translations = e.split('\\translation')

            entry = translations.pop(0).strip()
            if not entry:
                continue

            print(entry)

            dictionary_entry_data.append(entry)
            for ti, t in enumerate(translations):
                t = t.strip()
                params = [p[1:-1] for p in te_re.findall(t)]
                params = apply_formating(params)

                params = [p for p in params if p] # remove empty strings

                if not params:
                    print(entry)
                    continue

                for i in range(len(params) - 1):
                    if not params[i + 1].startswith(';'): # " ;" -> ";"
                        params[i] += ' '
                params[-1] = params[-1]
                if (params[-1].endswith('.})') or params[-1].endswith('.)')) and ti < len(translations) - 1: # mon.) -> mon.),
                    params[-1] += ','

                dictionary_entry_data.append("\\rawtext{" + "".join(params) + "}")

            entry_str = '\\begin{dictionaryentry}\n' + '\n'.join(dictionary_entry_data) + '\n\\end{dictionaryentry}'
            output.append(entry_str)

        f.seek(0)
        f.write('\n\n'.join(output))
        f.truncate()

def main(*args, **kwargs):
    export_directory = kwargs.get('directory')
    if not isdir(export_directory):
        print(f"Directory {export_directory} doesn't exist")
        exit()

    # get all files
    tex_files = [join(export_directory, f) for f in listdir(export_directory)]
    # get only tex files
    tex_files = [f for f in tex_files if isfile(f) and f.endswith('.tex')]

    for f in tex_files: postprocess_tex(f)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Postprocess fin-sms LaTex files.')
    parser.add_argument('-d', '--directory', type=str, required=True, help="The path to the export directory from Ver'dd.")
    args = parser.parse_args()

    main(**args.__dict__)
