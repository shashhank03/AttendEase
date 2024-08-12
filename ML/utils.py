import cv2
import face_recognition
import os
import numpy as np
import pandas as pd
from datetime import datetime
import csv

# Path to the folder containing student images
path = 'student_images'
attendance_path = 'attendance'  # Path for CSV files

def load_images():
    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        if curImg is not None:
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
    return images, classNames

def find_encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encodeList.append(encodings[0])
    return encodeList

def get_csv_filename(subject):
    # Create a CSV file name based on the subject and path
    return os.path.join(attendance_path, f'{subject}_Attendance.csv')

def create_csv_if_not_exists(subject):
    filename = get_csv_filename(subject)
    if not os.path.isfile(filename):
        os.makedirs(attendance_path, exist_ok=True)  # Ensure directory exists
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Subject', 'Time', 'Date'])  # Write header

def mark_attendance(name, subject):
    filename = get_csv_filename(subject)
    now = datetime.now()
    time_str = now.strftime('%I:%M:%S %p')
    date_str = now.strftime('%d-%B-%Y')

    # Ensure the 'attendance' directory exists
    os.makedirs(attendance_path, exist_ok=True)

    # Check if the file exists and create it if it doesn't
    if not os.path.isfile(filename):
        create_csv_if_not_exists(subject)

    # Append the attendance record
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, subject, time_str, date_str])

def view_attendance(subject):
    filename = get_csv_filename(subject)
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        return df
    else:
        return pd.DataFrame(columns=['Name', 'Subject', 'Time', 'Date'])

# Initialize face encodings globally
encoded_face_train = find_encodings(load_images()[0])
