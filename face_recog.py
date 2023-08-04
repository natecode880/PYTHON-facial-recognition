import numpy as np
import cv2
import face_recognition
import pygame

# Load the known faces and their respective encodings
known_faces = []
known_face_encodings = []

# Load the first known face (allowed face)
face1 = face_recognition.load_image_file('face_allowed1.png')
face1_encoding = face_recognition.face_encodings(face1)[0]
known_faces.append(face1)
known_face_encodings.append(face1_encoding)

# Load the second known face
face2 = face_recognition.load_image_file('face_allowed2.png')
face2_encoding = face_recognition.face_encodings(face2)[0]
known_faces.append(face2)
known_face_encodings.append(face2_encoding)

# Initialize the video capture from webcam
cap = cv2.VideoCapture(0)

# Initialize pygame for audio playback
pygame.mixer.init()
unidentified_sound = pygame.mixer.Sound('alert.mp3')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Find face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare the current face with the known allowed faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        top, right, bottom, left = face_location

        if True in matches:
            # Draw a rectangle around the allowed face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, 'Welcome', (left, top - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, 'Unknown Face', (left, top - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            # Play the audio file for unidentified face
            unidentified_sound.play()

    # Display the resulting frame
    cv2.imshow('Security Camera', frame)

    # Check if 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # Display the "Goodbye!" message on the camera window
        cv2.putText(frame, 'Goodbye!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.imshow('Security Camera', frame)
        cv2.waitKey(2000)  # Display the "Goodbye!" message for 2 seconds
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
