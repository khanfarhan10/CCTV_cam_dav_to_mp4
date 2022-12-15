"""
cd CamCode
python convert_dav_to_mp4.py

ffmpeg -y -i file.dav -vcodec libx264 -crf 24 file.mp4

batchedffmpeg * -i "D:\HemantFight29JanIllegal" * "D:\HemantFight29JanIllegalFull.mp4"
"""

INPUT_DIRECTORY = r"D:\Test" # r"D:\HemantFight29JanIllegal"
OUTPUT_DIRECTORY = r"D:\Test_Out" # r"D:\HemantFight29JanIllegal_Output"


import os, fnmatch

os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
from subprocess import call
def find(pattern, path):
    """Utility to find files wrt a regex search"""
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

FIND_FOLDER=INPUT_DIRECTORY

# dav_files=find('*.dav', FIND_FOLDER) + find('*.DAV', FIND_FOLDER)

def advanced_listdir(direc):
    x = os.listdir(direc)
    new = []
    for e in x:
        new.append(os.path.join(direc,e))
    return new

dav_files=advanced_listdir(FIND_FOLDER)

def getBaseNameNoExt(givenPath):
    """Returns the basename of the file without the extension"""
    filename = os.path.splitext(os.path.basename(givenPath))[0]
    return filename

for each_file in dav_files:
    # out_path = os.path.join(OUTPUT_DIRECTORY, getBaseNameNoExt(each_file) + ".mp4")
    out_path = os.path.join(OUTPUT_DIRECTORY, each_file.replace(".dav",".mp4").replace(".DAV",".mp4"))
    print("Converting: " + out_path)
    # call(['ffmpeg', '-y', '-i', each_file, "-vcodec", "libx264", "-crf", "24", out_path])
    os.system(f'cmd /k "ffmpeg -y -i "{each_file}" -vcodec libx264 -crf 24 "{out_path}""')
    print ("Converted: " + out_path)
