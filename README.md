# AttendEase

---

# Face Recognition Attendance System

This project is a **Face Recognition Attendance System** built using **Python** and **Tkinter**. The system leverages the power of **Dlib’s ResNet-34 face recognition model** for real-time face detection and recognition. This application allows you to register students, take attendance using a webcam, and view attendance records for different subjects.

## Features

- **Student Registration**: Register new students by uploading their images.
- **Real-time Attendance**: Take attendance in real-time using your webcam. The system recognizes faces and marks attendance automatically.
- **View Attendance Records**: Easily view attendance records for different subjects.

## Technologies and Models Used

- **Python**: Core programming language used for the project.
- **Tkinter**: GUI library for Python used to create the application's interface.
- **OpenCV**: Used for capturing and processing images from the webcam.
- **Dlib**: 
  - **Face Detection**: Utilizes Dlib’s HOG-based or CNN-based face detector.
  - **Face Recognition**: Uses Dlib’s ResNet-34 model for generating 128-dimensional face embeddings.
- **Face Recognition Library**: Simplifies the process of face recognition using Dlib’s models.

## Accuracy and Performance

- The face recognition model based on **Dlib's ResNet-34** architecture achieves an accuracy of approximately **99.38%** on the LFW (Labeled Faces in the Wild) dataset.
- The system can recognize multiple faces simultaneously and can handle varying lighting conditions and angles with high robustness.

## Installation

### Prerequisites

- **Python 3.6+** should be installed on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install opencv-python
pip install numpy
pip install dlib
pip install git+https://github.com/ageitgey/face_recognition_models
pip install face_recognition
pip install pandas
```

### Step 3: Download Dlib Models

Ensure you have the required Dlib models:

- **Shape Predictor**: `shape_predictor_68_face_landmarks.dat`
- **Face Recognition Model**: `dlib_face_recognition_resnet_model_v1.dat`

You can download these models from the Dlib model downloads page:
- [Shape Predictor](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
- [Face Recognition Model](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)

Extract the `.dat` files and place them in a `models/` directory within your project.

### Step 4: Run the Application

Run the application using the following command:

```bash
python app.py
```

## Usage

1. **Register a New Student**: Click on "Register", enter the student's name, and upload their image.
2. **Start Attendance**: Enter the subject name and click "Start Attendance". The system will use the webcam to recognize faces and mark attendance.
3. **View Attendance**: Click on "View Attendance", enter the subject name, and the attendance records will be displayed.

## Project Structure

```plaintext
├── attendance_app.py        # Main application file
├── utils.py                 # Utility functions for face recognition and attendance
├── student_images/          # Folder containing registered student images
├── attendance_records/      # Folder where attendance records are saved
├── models/                  # Folder containing Dlib's pre-trained models
│   ├── shape_predictor_68_face_landmarks.dat
│   └── dlib_face_recognition_resnet_model_v1.dat
└── README.md                # This file
```

## Future Enhancements

- **Enhanced Recognition Accuracy:** Integrating additional models or fine-tuning existing ones for improved accuracy.
- **Mobile Integration:** Developing a mobile app interface for easier access and management.
- **Real-Time Notifications:** Adding functionality to send notifications or alerts when attendance is taken.
- **Database Integration:** Storing attendance records in a database for better scalability and management.

## Acknowledgments

- Special thanks to the developers of the `face_recognition`,`Dlib` and `OpenCV` libraries for providing robust tools for face detection and recognition.

---
