import os
from pathlib import Path

packDir = input("\nEndter absolute path to pack directory: ")
soundDir = packDir+"/assets/minecraft/sounds/custom"
try:
    soundFiles = []
    for root, dirs, files in os.walk(soundDir, topdown=False):
        for name in files:
            soundFiles.append(name)
except:
    print("crate a folder named custom in souds")
    quit()

print("\ncommands:\nconvert - converts all files to .ogg\nadd - add all unknown sound files\nlist - list all files")

def convert():
    for file in soundFiles:
        if file[-1] == "3":
            p = Path(soundDir+"/"+file)
            p.rename(p.with_suffix('.ogg'))

def writeToInedx(notIndexed):
    index = open(packDir+"/assets/minecraft/sounds.json", "r+")
    lines = index.readlines()
    lines = lines[:-1]
    index.truncate(0)
    for line in lines:
        index.write(line)

    for file in notIndexed:
        print("\ncurrent file: "+file)
        soundEvent = input("enter sound event: ")
        index.write('"{action}": {\n"sounds": [\n"custom/{file}"\n],\n"replace": true,\n"subtitle": "lol"\n}\n}'.format(action=soundEvent,file=file))


def add():
    index = open(packDir+"/assets/minecraft/sounds_index.txt", "r+")
    if index.readline() != "indexed files:":
        index.write("indexed files:")
    print(index.read())
    lines = index.readlines()
    realIndex = open(packDir+"/assets/minecraft/sounds.json", "r+")
    realLines = realIndex.readlines()
    realLines = realLines[:-1]
    index.truncate(0)
    for l in realLines:
        realIndex.write(l)
    for file in soundFiles:
        for indexedFile in lines:
            if file == indexedFile:
                continue
            else:
                print("current file: "+file)
                soundEvent = input("enter sound event: ")
                realIndex.write('"{action}": {\n"sounds": [\n"custom/{file}"\n],\n"replace": true,\n"subtitle": "lol"\n}\n}'.format(action=soundEvent,file=file))
                index.write("\n"+file)


    index.close()

while True:
    action = input("\nEnter action: ")
    if action == "convert":
        convert()
    elif action == "add":
        add()
        print("add")
    elif action == "list":
        for file in soundFiles:
            print(file)
    else:
        print("invalid action")
