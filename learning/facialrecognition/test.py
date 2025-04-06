import face_recognition
import cv2
import numpy as np
import csvput
import time
import datetime
from tkinter import Canvas
import tkinter as tk
from PIL import ImageTk,Image

def cmd():
    video_capture = cv2.VideoCapture(0)
    rb=tk.Tk()
    

    parth_image = face_recognition.load_image_file("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code/face/parth.jpg")

    parth_face_encoding = face_recognition.face_encodings(parth_image)[0]

    puru_image = face_recognition.load_image_file("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code/face/puru.jpeg")
    puru_face_encoding = face_recognition.face_encodings(puru_image)[0]
    super_image = face_recognition.load_image_file("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code/face/monkey.jpg")
    super_face_encoding = face_recognition.face_encodings(super_image)[0]





    known_face_encodings = [
        parth_face_encoding,
        puru_face_encoding,
        super_face_encoding,
    ]
    known_face_names = [
        "Parth Amradkar",
        "Puru Amradkar",
        "Atharva Amradkar"
    ]


    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    
    
    ret, frame = video_capture.read()

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
                time.sleep(5)
                datetime_object = datetime.datetime.now()
                print(datetime_object)
                camera = cv2.VideoCapture(0)
                l1=tk.Label(rb,text=name)
                l1.pack()
                
                return_value, image = camera.read()
                cv2.imwrite(name+'.png', image)
               
                print("DONE")
                z=0 
                csvput.fun1(name)
               
                            
            face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
        
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

        
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        #cv2.imshow('Video', frame)
        #custom piece of code
        
    
       

    
    rb.mainloop
    
    video_capture.release()
    cv2.destroyAllWindows()
