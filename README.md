Face Recognition Security Camera

This is a Python script that uses face recognition to implement a simple security camera system. It detects faces in the webcam feed and compares them with known allowed faces to determine whether the person is authorized or not. If a known face is detected, it displays a welcome message. Otherwise, it marks the face as an unknown face and plays an alert sound.

Requirements
    - Python 3.x
    - OpenCV (cv2)
    - Numpy
    - face_recognition
    - pygame

You can install the required Python packages using pip:

    - pip install opencv-python numpy face-recognition pygame

Usage

Prepare the known allowed faces:

    - Save the images of known allowed faces in PNG format.
    - Update the paths of the known allowed face images in the code:
        face1 = face_recognition.load_image_file('face_allowed1.png')
        face2 = face_recognition.load_image_file('face_allowed2.png')

Prepare the alert sound:

Save the alert sound file (e.g., alert.mp3) to be played when an unknown face is detected.
Make sure that the audio file is in a format supported by pygame.

Execute the script using the following command:
    - python3 face_recog.py

Interaction:

The script will start capturing the webcam feed and processing each frame.
If a known allowed face is detected, it will draw a green rectangle around the face and display the message "Welcome"
If an unknown face is detected, it will draw a red rectangle around the face and display the message "Unknown Face." Additionally, it will play the alert sound.
Exiting the script:

Press 'q' to quit the script. The script will display a "Goodbye!" message for 2 seconds before closing.
----------------------------------------------------------------------------------------------------------------
Note

To improve security, a cooldown period has been implemented to avoid multiple consecutive detections of known faces. The cooldown period is set to 10 seconds by default, which means that once a known face is detected and welcomed, the system will ignore any new face detections for the next 10 seconds.
The code can be modified to add more known allowed faces by loading additional images and updating the known_faces and known_face_encodings lists accordingly.
Remember that this is a simple demonstration of face recognition for a security camera system. Depending on the use case, you might need to implement more sophisticated security measures and fine-tune the face recognition parameters.
