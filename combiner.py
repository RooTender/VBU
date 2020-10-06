import ffmpeg
import os
import glob


def getFilesWithExtension(dir, extension):
    origDir = os.getcwd()
    os.chdir(dir)

    out = glob.glob(extension)
    os.chdir(origDir)
    return out


def getVideo(dir):
    return getFilesWithExtension(dir, 'output*')


def getAudio(dir):
    return getFilesWithExtension(dir, 'audio*')


def combine(dir, output):
    print(getVideo(dir))
    print(getAudio(dir))
