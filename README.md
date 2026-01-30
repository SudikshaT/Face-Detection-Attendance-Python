📌 Project Description

This project is a Smart Attendance System developed using Python and OpenCV that automatically marks attendance by detecting and recognizing faces in real time. The system captures facial images, compares them with stored data, and records attendance in an Excel file.

🚀 Features

Face detection using OpenCV Haar Cascade

Face image dataset creation

Real-time face recognition

Automatic attendance marking

Attendance stored in Excel format

Simple and efficient system

🛠 Technologies Used

Python

OpenCV

NumPy

OpenPyXL

Datetime Module

📖 How to Use the Smart Attendance System

Follow the steps below to run the project successfully.

Step 1: Clone the Repository

Download the project to your local system.

git clone https://github.com/SudikshaT/Face-Detection-Attendance-Python

Step 2: Navigate to the Project Folder
cd smart-attendance-system-opencv

Step 3: Install Required Libraries

Make sure Python is installed, then run:

pip install -r requirements.txt

Step 4: Collect Face Data

Run the face data collection script.

python s1.py


Enter the person ID when prompted

The webcam will open

The system captures multiple face images

Images are stored in the faces/ folder

Step 5: Run the Attendance System
python s2.py


Enter the same person ID

The system detects and compares faces

If matched, attendance is marked

Step 6: Check Attendance File

After successful recognition:

An Excel file named attendance_student.xlsx is created

It contains:

Name

Date

Time

Attendance Status

📌 Notes

Ensure good lighting for better accuracy

Keep the camera stable

Face should be clearly visible

Works best with limited users
