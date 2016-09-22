# coding=utf-8
import argparse
import json
import re

# Define commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument("--infile", type=str,
                    help="In-file in bibtext format")
args = parser.parse_args()


# Replacements to be ran on the values in bibtex entries, before converting to
# front matter in the publication markdown files.
value_replacements = {
    r'{\"O}': 'Ö',
    r'{\"A}': 'Ä',
    r'{\AA}': 'Å',
    r'{\"o}': 'ö',
    r'{\"a}': 'ä',
    r'{\aa}': 'å',
    r'{\&}amp;': '&',
    r'{\’e;}': 'é',
    r'{\"u}': 'ü',
    r'{\’a;}': 'á',
    ' :': ':',
    r'\&': '&',
    '{': '',
    '}': '',
    '\\': ''
}
# Some replacements that have to be done, so as not to override keys used by
# HUGO
key_replacements = {
    'type': 'bibtex_type',
    'url': 'url_html',
}

publications = []
with open(args.infile) as infile:
    publication = {}
    for line in infile:
        if line.startswith('@'):
            publications.append(publication)
            publication = {}
        m = re.match('^\s*([^\=]*)\=(.*)$', line)
        if m:
            # If m is not None, this line is a key/value line in the bibtex
            v = m.group(2).strip(' {},')
            for srch, repl in value_replacements.iteritems():
                v = v.replace(srch, repl)
            # json.dumps ensures that quotes are escaped etc.
            publication[m.group(1).strip()] = json.dumps(v).strip('"')
    publications.append(publication)

filename_replacements = {
    '.' : '',
    ',' : '',
    ' ': '-',
    ':': '',
    '\'': '',
    '(': '',
    ')': '',
    '---': '-',
    '--': '-',
}

for publication in publications:
    if not len(publication) == 0:
        if not 'title' in publication:
            print "Warning! no title in: " + str(publication)
        else:
            year = publication['year']
            publication['title'] = publication['title'].replace('.', '')
            filename = year + '-' + publication['title'].lower()
            for srch, repl in filename_replacements.iteritems():
                filename = filename.replace(srch, repl)
            filename += '.md'

            with open(filename, 'w') as outfile:
                outfile.write('+++\n')
                for k, v in publication.iteritems():
                    for srch, repl in key_replacements.iteritems():
                        k = k.replace(srch, repl)
                    outfile.write(k + ' = "' + v + '"\n')
                outfile.write('+++\n\n')
                print 'Wrote file: ' + filename

