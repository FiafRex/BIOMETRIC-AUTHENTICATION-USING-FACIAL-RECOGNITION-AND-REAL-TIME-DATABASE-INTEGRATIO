# BIOMETRIC AUTHENTICATION USING FACIAL RECOGNITION AND REAL-TIME DATABASE INTEGRATION

This project presents a comprehensive system that leverages the power of facial recognition coupled with real-time database integration to authenticate individuals. The primary objective is to identify faces and mark their attendance. A unique feature of this system is its ability to prevent marking attendance for a face if it reappears before a set interval.

## Key Features:

- **Real-time Face Attendance System**: The core functionality revolves around capturing faces in real-time and marking their attendance.
  
- **Graphical Interface**: Plans are in place to enhance the system with a user-friendly graphical interface.

- **Live Database Integration**: The system is not just about recognizing faces. It integrates with a live database to update attendance records in real-time.

## Technical Details:

- **Languages & Tools**: The project predominantly uses Python for its implementation.
  
- **Face Scanning**: Faces are captured using a webcam. The captured graphics are then processed, and images are loaded for further operations.
  
- **Encoding Generator**: After loading the images, the system generates encodings which are essential for the face recognition process.
  
- **Face Recognition**: The actual recognition of faces is achieved using a combination of various components and algorithms.
  
- **Database Management**: The system integrates with a database where images and attendance records are stored. The real-time database gets updated as and when faces are recognized.
  
- **Development Environment**: The code is run using Visual Studio community edition with the C++ compiler.
  
- **Libraries Used**:
  - **OpenCV**: A library that uses machine learning algorithms to search for faces within an image.
  - **numPy**: Provides a list containing the coordinates of detected faces.
  - **cvzone**: A computer vision package that simplifies the execution of image processing and AI functions. It is built upon OpenCV and Mediapipe libraries.
  - **Pickle**: Used as a support library to connect various elements of the project.
  
- **Database Setup**: The database is set up using the Firebase console, ensuring a seamless and efficient real-time update mechanism.

## Conclusion:

This project stands as a testament to the advancements in biometric authentication systems. By integrating facial recognition with real-time database updates, it offers a robust solution for attendance systems and can find applications in various other domains as well.
