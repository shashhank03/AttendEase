import os
import dlib
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import cv2
import numpy as np
import time
import face_recognition
from utils import load_images, find_encodings, mark_attendance, view_attendance, encoded_face_train

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System")
        self.root.geometry("800x600")
        self.root.configure(bg='#F0F8FF')  # Light blue background

        # File paths
        shape_predictor_path = 'models/shape_predictor_68_face_landmarks.dat'
        face_recognition_model_path = 'models/dlib_face_recognition_resnet_model_v1.dat'

        # Check if the files exist
        if not os.path.isfile(shape_predictor_path):
            raise FileNotFoundError(f"Shape predictor file not found at: {shape_predictor_path}")
        if not os.path.isfile(face_recognition_model_path):
            raise FileNotFoundError(f"Face recognition model file not found at: {face_recognition_model_path}")

        # Initialize dlib's face detector and face recognition model
        self.detector = dlib.get_frontal_face_detector()
        self.sp = dlib.shape_predictor(shape_predictor_path)
        self.facerec = dlib.face_recognition_model_v1(face_recognition_model_path)

        self.subject_var = tk.StringVar()

        # Title Section
        title_frame = tk.Frame(root, bg='#4682B4', bd=5)
        title_frame.pack(fill=tk.X)
        tk.Label(title_frame, text="Face Recognition Attendance System", bg='#4682B4', fg='white', font=('Helvetica', 20, 'bold')).pack(pady=10)

        # Main Frame
        main_frame = tk.Frame(root, bg='#F0F8FF', pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Registration Section
        reg_frame = tk.LabelFrame(main_frame, text="Register New Student", bg='#F0F8FF', font=('Helvetica', 14, 'bold'), pady=10, padx=10)
        reg_frame.pack(fill=tk.X, padx=20, pady=10)
        tk.Button(reg_frame, text="Register", command=self.register_student, bg='#4CAF50', fg='white', font=('Helvetica', 12), width=20).pack(pady=5)

        # Attendance Section
        att_frame = tk.LabelFrame(main_frame, text="Take Attendance", bg='#F0F8FF', font=('Helvetica', 14, 'bold'), pady=10, padx=10)
        att_frame.pack(fill=tk.X, padx=20, pady=10)
        tk.Label(att_frame, text="Subject:", bg='#F0F8FF', font=('Helvetica', 12)).pack(pady=5)
        tk.Entry(att_frame, textvariable=self.subject_var, font=('Helvetica', 12), width=30).pack(pady=5)
        tk.Button(att_frame, text="Start Attendance", command=self.start_attendance, bg='#2196F3', fg='white', font=('Helvetica', 12), width=20).pack(pady=5)

        # View Attendance Section
        view_frame = tk.LabelFrame(main_frame, text="View Attendance", bg='#F0F8FF', font=('Helvetica', 14, 'bold'), pady=10, padx=10)
        view_frame.pack(fill=tk.X, padx=20, pady=10)
        tk.Button(view_frame, text="View", command=self.view_attendance, bg='#FF5722', fg='white', font=('Helvetica', 12), width=20).pack(pady=5)

        self.cap = None
        self.attendance_taken = False

    def register_student(self):
        name = simpledialog.askstring("Input", "Enter student's name:")
        if name:
            img_path = filedialog.askopenfilename(title="Select Student Image", filetypes=[("Image Files", "*.jpg;*.png")])
            if img_path:
                img = cv2.imread(img_path)
                cv2.imwrite(f'student_images/{name}.jpg', img)
                global encoded_face_train
                encoded_face_train = find_encodings(load_images()[0])
                messagebox.showinfo("Success", "Student registered successfully!")

    def start_attendance(self):
        self.subject = self.subject_var.get()
        if not self.subject:
            messagebox.showwarning("Input Error", "Please enter the subject.")
            return

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam.")
            return

        # Set video capture properties to a reasonable resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cap.set(cv2.CAP_PROP_FPS, 60)

        start_time = time.time()
        duration = 15  # Duration to keep webcam open in seconds
        marked_names = set()  # To avoid re-marking attendance for the same person
        frame_skip = 1  # Process every nth frame to reduce computational load
        frame_count = 0

        cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Webcam', 1280, 720)  # Adjust the size to match the resolution

        tolerance = 0.5  # Adjust the tolerance value to improve accuracy

        while True:
            success, img = self.cap.read()
            if not success:
                messagebox.showerror("Error", "Failed to capture image.")
                break

            frame_count += 1
            if frame_count % frame_skip != 0:
                continue  # Skip processing this frame

            imgS = cv2.resize(img, (0, 0), None, 0.5, 0.5)  # Scale down the image
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faces_in_frame = face_recognition.face_locations(imgS)
            encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

            for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
                matches = face_recognition.compare_faces(encoded_face_train, encode_face, tolerance)
                faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
                matchIndex = np.argmin(faceDist)

                if matches[matchIndex]:
                    name = load_images()[1][matchIndex].upper()
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2  # Adjust bounding box
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

                    if name not in marked_names:
                        mark_attendance(name, self.subject)
                        marked_names.add(name)

            elapsed_time = time.time() - start_time
            if elapsed_time > duration:
                break

            cv2.imshow('Webcam', img)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

        if marked_names:
            messagebox.showinfo("Attendance", f"Attendance recorded for: {', '.join(marked_names)}")
        else:
            messagebox.showwarning("Attendance", "No faces detected for attendance.")


    def view_attendance(self):
        subject = simpledialog.askstring("Input", "Enter the subject to view attendance:")
        if subject:
            df = view_attendance(subject)
            if not df.empty:
                self.show_attendance(df)
            else:
                messagebox.showinfo("No Records", f"No attendance records found for the subject: {subject}.")

    def show_attendance(self, df):
        top = tk.Toplevel(self.root)
        top.title("Attendance Records")
        top.geometry("800x600")
        top.configure(bg='#F0F8FF')

        table_frame = tk.Frame(top, bg='#F0F8FF')
        table_frame.pack(pady=10)

        for i, column in enumerate(df.columns):
            tk.Label(table_frame, text=column, bg='#F0F8FF', font=('Helvetica', 12, 'bold')).grid(row=0, column=i, padx=10, pady=5)

        for i, row in df.iterrows():
            for j, value in enumerate(row):
                tk.Label(table_frame, text=value, bg='#F0F8FF', font=('Helvetica', 12)).grid(row=i+1, column=j, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
