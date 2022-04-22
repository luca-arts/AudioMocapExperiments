# this script taskes a video file and a "deeptrack" text file and outputs a cleaned textfile for l;ater processign
import cv2
from cv2 import perspectiveTransform
from numpy import real


#startvariables
currentframe = 0
noperson = []
realperson = []
personmatch = {}
framelist = []
# parse Command line arguments
def parseargs():
    import argparse
    parser = argparse.ArgumentParser(description='Clean up deeptrack text file')
    parser.add_argument('-iv', '--inputvideo', help='input video, tracked with deeptrack', required=True)
    parser.add_argument('-it', '--inputtext', help='input text, output from deeptrack', required=True)
    parser.add_argument('-t', '--threshold', help='minimum detection threshold', required=False)
    parser.add_argument('-o', '--output', help='output file', required=True)
    args = parser.parse_args()
    return args


#load video
def loadvideo():
    cap = cv2.VideoCapture(args.inputvideo)
    return cap

def loadtext():
    with open(args.inputtext, 'r') as f:
        txt = f.readlines()
    return txt

#goto frame number in video
def gotoFrameAndShow(cap, frame):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
    #display frame
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    # return frame



def parseTextAndGetNextFrame():
    print(int(currentframe))
    # parse text file
    # 3 1 660 824 414 938 -1 -1 -1 -1 
    # frame number, person_id, x, y, width, height, confidence, xmin, ymin, xmax, ymax
    persons = []
    for line in txt:
        data = line.split(' ')
        # print(data[0])
        if (int(data[0]) == int(currentframe)):
            # print(line)
            # currentframe = int(data[0])
            if int(data[1]) not in noperson:
                persons.append({"id": int(data[1]), "x": int(data[2]), "y" : int(data[3]), "w": int(data[4]), "h": int(data[5])})
    return persons


args = parseargs()
cap = loadvideo()
txt = loadtext()
    
while True:
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    personlist = parseTextAndGetNextFrame()
    print(personmatch)
    cap.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
    ret, frame = cap.read()
    newpersonlist = []
    if len(personlist) > 0 :
        print(personlist)
        
        for person in personlist:
            cv2.rectangle(frame, (person["x"], person["y"]), (person["x"] + person["w"], person["y"] + person["h"]), (0, 255, 0), 2)
            # cv2.putText(frame, "World", (50,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
            cv2.putText(frame, str(person["id"]), (person["x"], person["y"]), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 50)
            if person["id"] in noperson:
                # just ignore
                print("ignoring")
            elif person["id"] in realperson:
                # just add frame to finallist using previous ID match
                if person['id'] in personmatch[1]:
                    realID = 1
                else: 
                    realID = 2 
                framelist[currentframe]
                print("adding")
            #draw rectangle
            else:
                print("newperson")
                newpersonlist.append(person)
                #newperson

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    for person in newpersonlist:
        idmatch = input("who is  person: " + str(person["id"]) + "? ")
        if idmatch == "3":
            noperson.append(person["id"])
        try: 
            personmatch[idmatch].append(person["id"])
        except:
            personmatch[idmatch] = []
            personmatch[idmatch].append(person["id"])
        realperson.append(person["id"])

    
    
    currentframe = currentframe + 1
    if key == ord('q'):
        break







