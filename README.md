# Introduction
This tool is written in python which can run on Windows or mac. It can parse clipping file on your kindle and put highlights on every txt file while named by your books' name, and you don't need to reorganize your highlights or notes manually, especially the amount is huge.

# Prepare Work

1. Connect your kindle device to your computer, and click "Document" folder to find `My Clippings.txt` file;
2. Copy `My Clippings.txt` file to your computer, anywhere is OK.

# For Mac Users
For mac users, open your terminal, and enter `My Clippings.txt` file directory.

1. Run "pwd" to get current directory;
2. Copy the absolute path to `clipping.conf` -> source -> FILE_PATH, DONNOT forget `My Clippings.txt` below;
3. Modify `clipping.conf` -> target -> OUTPUT_DIR with the same path, attached with a directory, no matter it exists or not;
4. run `python hls_cipping.py`.

You can find all your highlights in the same folder.

# For Windows Users
For windows users, you can run the script in `cmd` or `sublime text`, but must have a python 2.x env.

1. Enter the folder where `My Clippings.txt` is, then run `python hls_cipping.py`;
2. Target folder `kindle_hls` is in current directory.
