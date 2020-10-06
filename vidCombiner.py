import ffmpeg
import os
import glob


def getVideoFilename(dir):
    origDir = os.getcwd()
    os.chdir(dir)

    out = glob.glob('*.avi')
    os.chdir(origDir)
    return out[0]


def combine(dir, output):
    print(getVideoFilename(dir))
