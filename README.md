# furry_nonsense
A bunch of Python scripts that people might like to use for furry bullshit.

If you want to use them, you should have Python 3.7 or later installed. If you don't know how to do that, definitely don't run these scripts: they aren't complicated, but I don't want you messing up your computer by trying to do something like this.

## sort_by_fa_artist.py
This script expects you to pass two arguments: the path to a source directory, and the path to a destination directory.

Any files in the source directory (and just the source directory, no subdirectories) that follow the FurAffinity naming convention will be moved into the destination directory, placed into subfolders based on the artist's (or, to be technically correct, the uploader's) name.
 
 If there's already a file by that name in the destination directory, the script will try to give it a different name by appending the name with a number in parentheses.
