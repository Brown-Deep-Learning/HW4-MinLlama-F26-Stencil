# Brown University CSCI 2470: Deep Learning (Fall 2026)
#
# Adapted from the minllama-assignment by Vijay Viswanathan, developed for
# Carnegie Mellon University's CS11-711 Advanced NLP (Graham Neubig).
# Original repository: https://github.com/neubig/minllama-assignment

#

# create a zip file for submission

import os
import sys
import zipfile

required_files = {'run_llama.py',
                  'llama.py',
                  'optimizer.py',
                  'classifier.py',
                  'rope.py',
                  'generated-sentence-temp-0.txt',
                  'generated-sentence-temp-1.txt',
                  'sst-dev-prompting-output.txt',
                  'sst-test-prompting-output.txt',
                  'sst-dev-finetuning-output.txt',
                  'sst-test-finetuning-output.txt',
                  'cfimdb-dev-prompting-output.txt',
                  'cfimdb-test-prompting-output.txt',
                  'cfimdb-dev-finetuning-output.txt',
                  'cfimdb-test-finetuning-output.txt'}

optional_files = set()

def check_file(file: str, check_uid: str):
    global required_files

    target_prefix = None
    # --
    inside_files = set()
    with zipfile.ZipFile(file, 'r') as zz:
        # --
        print(f"Read zipfile {file}:")
        zz.printdir()
        print("#--")
        # --
        for info in zz.infolist():
            if info.filename.startswith("_"):
                continue  # ignore these files
            if target_prefix is None:
                target_prefix, _ = info.filename.split("/", 1)
                target_prefix = target_prefix + "/"
            # --
            assert info.filename.startswith(target_prefix), \
                'There should only be one top-level dir (with your Brown username as the dir-name) inside the zip file.'
            ff = info.filename[len(target_prefix):]
            inside_files.add(ff)
        # --
    # --
    required_files -= inside_files
    combined_files = required_files | optional_files
    combined_files -= inside_files
      
    assert len(required_files) == 0, f"Some required files are missing: {required_files}"
    # --
    assert target_prefix[:-1] == check_uid, f"Brown username mismatched: {target_prefix[:-1]} vs {check_uid}"
    print(f"Read zipfile {file}, please check that your Brown username is: {target_prefix[:-1]}")
    print(f"And it contains the following files: {sorted(list(inside_files))}")
    # -- OPTIONAL CHECK --
    assert len(combined_files) in [4,0], f"[Optional check] Some of your advanced outputs are missing: {combined_files}"
    # --

def main(path: str, uid: str):
    uid = uid.strip()
    if os.path.isdir(path):
        with zipfile.ZipFile(f"{uid}.zip", 'w') as zz:
            for root, dirs, files in os.walk(path):
                if '.git' in root or '__pycache__' in root:
                    continue  # ignore some parts
                for file in files:
                    if file.endswith(".zip"):
                        continue
                    ff = os.path.join(root, file)
                    rpath = os.path.relpath(ff, path)
                    zz.write(ff, os.path.join(".", uid, rpath))
                    if rpath in required_files:
                        required_files.remove(rpath)
        assert len(required_files) == 0, breakpoint()
        # --
        print(f"Submission zip file created from DIR={path} for {uid}: {uid}.zip")
        check_file(f'{uid}.zip', uid)
    else:  # directly check
        check_file(path, uid)
    # --

if __name__ == '__main__':
    main(*sys.argv[1:])
