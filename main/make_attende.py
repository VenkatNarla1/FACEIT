from librabries import *
video_capture = cv2.VideoCapture(0)
# video_capture = cv2.VideoCapture("http://192.168.183.155:8080/video")
def Find_attend(known_face_encodings,known_face_names):
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    c=0
    l2={}
    l1=[]
    while True:
        ret, frame = video_capture.read()
        c+=1
        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                l1.append(name)
                face_names.append(name)
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (random.choice(range(0,256)), random.choice(range(0,256)), random.choice(range(0,256))), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (random.choice(range(0,256)), random.choice(range(0,256)), random.choice(range(0,256))), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
        process_this_frame = not process_this_frame
        cv2.imshow('Video', frame)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    # print frmaes present
    for i in l1:
        if i not in l2:
            l2[i]=1
        else:
            l2[i]+=1
    l1.clear()
    c=c//2
    for i in l2:
        if l2[i]>c:
            l1.append(i)
    return list(set(l1))