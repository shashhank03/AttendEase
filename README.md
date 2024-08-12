# AttendEase
Here's a README file for your Face Recognition Attendance System project:

---

# Face Recognition Attendance System

## Overview

The Face Recognition Attendance System is a Python-based application that automates the process of taking attendance using face recognition technology. The system uses a webcam to capture images of students, matches them against a pre-trained dataset of student images, and records attendance in real-time.

## Features

- **Student Registration:** Easily register new students by uploading their images through the interface.
- **Automated Attendance:** Capture real-time attendance through a webcam. The system recognizes multiple faces simultaneously and marks attendance for the recognized individuals.
- **View Attendance Records:** View and manage attendance records for different subjects directly from the application.

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - `tkinter`: For building the graphical user interface (GUI).
  - `face_recognition`: For face detection and recognition, utilizing HOG and CNN models.
  - `OpenCV`: For image processing and webcam integration.
  - `NumPy`: For numerical operations.
  - `Pandas`: For handling attendance records.

## Model Accuracy

- **Face Recognition Accuracy:** Approximately **95%** under optimal conditions (good lighting and clear visibility).
- **Haar Cascade Classifier Accuracy:** Around **90-95%** for face detection in typical scenarios.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python attendance_app.py
   ```

## How to Use

1. **Register New Student:**
   - Open the application.
   - Click on "Register" and enter the student's name.
   - Select and upload the student's image.

2. **Take Attendance:**
   - Enter the subject name.
   - Click on "Start Attendance."
   - The system will capture images via the webcam and mark attendance for recognized faces.

3. **View Attendance:**
   - Click on "View Attendance."
   - Enter the subject name to view the attendance records.

## Directory Structure

```
face-recognition-attendance-system/
│
├── attendance_app.py          # Main application file
├── utils.py                   # Utility functions for image processing and attendance
├── student_images/            # Directory to store registered student images
├── attendance_records/        # Directory to store attendance records
└── requirements.txt           # List of required libraries
```

## Future Enhancements

- **Enhanced Recognition Accuracy:** Integrating additional models or fine-tuning existing ones for improved accuracy.
- **Mobile Integration:** Developing a mobile app interface for easier access and management.
- **Real-Time Notifications:** Adding functionality to send notifications or alerts when attendance is taken.
- **Database Integration:** Storing attendance records in a database for better scalability and management.

## Acknowledgments

- Special thanks to the developers of the `face_recognition` and `OpenCV` libraries for providing robust tools for face detection and recognition.

---

This README provides an overview of your project, including how to install, run, and use it, along with a description of its features, technologies, and potential future enhancements.
