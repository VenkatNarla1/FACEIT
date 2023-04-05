from librabries import *
from enocoding import *
from make_attende import *
from write_attend import *
# folder path to be given
path = r"data"
images = []
classNames = []
myList = os.listdir(path)
# print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# print(images)
known_face_encodings = findEncodings(images)
known_face_names = classNames

a=Find_attend(known_face_encodings,known_face_names)

markAttendance(a)