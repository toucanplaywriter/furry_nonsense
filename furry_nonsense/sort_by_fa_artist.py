import argparse
from glob import glob
import os
import re


FA_REGEX = re.compile(r"\d{10}\.([^_]+)_.*")


def sort_by_artist(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for src_file in glob(src + "/*"):
        # Check if the filename matches that of an FA download file.
        temp = FA_REGEX.findall(src_file)

        #
        _, filename = os.path.split(src_file)
        filename, extension = os.path.splitext(filename)

        if temp:
            artist = temp[0]
            artist_dir = os.path.join(dest, artist)
            dest_file = os.path.join(dest, artist, f"{filename}{extension}")

            if not os.path.exists(artist_dir):
                os.mkdir(artist_dir)

            k = 1
            while os.path.exists(dest_file):
                dest_file = os.path.join(dest, artist, f"{filename}_({k}){extension}")
                k += 1

            #         print(artist)
            #         print(filename)
            #         print(extension)
            print(src_file)
            print(dest_file)
            print()
            os.rename(src_file, dest_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sorts files downloaded from FurAffinity into artist folders.')
    parser.add_argument('src', type=str, help='the source directory')
    parser.add_argument('dest', type=str, help='the destination directory')

    args = parser.parse_args()
    sort_by_artist(args.src, args.dest)
