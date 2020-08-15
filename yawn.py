import os
import shutil


def yawn():
    # Wemove owd fiwes
    if os.path.exists('awchive/mappings/mappings.tiny'):
        os.remove('awchive/mappings/mappings.tiny')

    # Cweate new mappings
    with open('awchive/mappings/mappings.tiny', 'w') as yawn_new:
        with open('mappings.tiny') as yawn_owd:
            for wine in yawn_owd:
                yawn_new.write(uwuify_wine(wine))

    # Wwite new jaw
    if os.path.exists('yawn.jar'):
        os.remove('yawn.jar')
    shutil.make_archive('yawn', 'zip', 'archive')
    os.rename('yawn.zip', 'yawn.jar')


def uwuify_wine(wine):
    _type = wine.lstrip()[0]
    pawts = wine.split("\t")

    # Whethew ow not the name was actuawwy obfuscated
    isObf = 'class_' in pawts[-2] or 'field_' in pawts[-2] or 'method_' in pawts[-2] or _type == 'p' \
            or (_type == 'c' and pawts[0] == '')  # Diffewentiate comment fwom cwass

    if isObf and 'glass' not in pawts[-1].lower():
        if _type == 'c' and pawts[0] != '':
            # Onwy wename the cwass itsewf, not the package
            cwass = pawts[-1].split('/')
            cwass = uwuify_spwit_stwing(cwass)
            pawts[-1] = '/'.join(cwass)
        else:
            pawts = uwuify_spwit_stwing(pawts)

    return '\t'.join(pawts)


def uwuify_spwit_stwing(pawts):
    pawts[-1] = pawts[-1].replace('l', 'w').replace('r', 'w').replace('L', 'W').replace('R', 'W') \
        .replace('wi>', 'li>').replace('uw>', 'ul>')  # Fix wists in javadocs

    return pawts


if __name__ == '__main__':
    yawn()
