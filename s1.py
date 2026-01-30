import cv2
import os

# Get the person ID
person_id = input("Enter person ID: ")
person_folders = {}
if person_id not in person_folders:
    person_folder = f'faces/{person_id}'
    isExist = os.path.exists(person_folder)
    if isExist == 0:
        os.makedirs(person_folder)
person_folders[person_id] = person_folder

# Create a folder to save the extracted faces
if not os.path.exists('faces'):
    os.makedirs('faces')

# Create a dictionary to store the person IDs and their corresponding folders

# Create a VideoCapture object to read the camera
cap = cv2.VideoCapture(0)
currentframe = 0
while currentframe < 1:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    cv2.imshow("Video Frame", frame)
    cv2.waitKey()
    currentframe += 1
if not cap.isOpened():
    print("Cannot open camera")
    exit()

currentframe = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use OpenCV's Haar cascade classifier to detect faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        if currentframe < 11:
            # Extract the face from the frame
            face = frame[y:y + h, x:x + w]
            # Create a folder for the person if it doesn't exist
            # Save the face to the person's folder
            filename = f'{person_folder}/face_{currentframe}.jpg'
            if cv2.imwrite(filename, face):
                print(f'Saved face to {filename}')
            else:
                print(f'Failed to save face to {filename}')

    # Display the video frame
    cv2.imshow('Video Frame', frame)

    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    currentframe += 1

cap.release()
cv2.destroyAllWindows()
