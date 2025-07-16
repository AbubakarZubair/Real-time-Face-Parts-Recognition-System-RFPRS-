# Real-time-Face-Parts-Recognition-System-RFPRS

## **Project Overview**

The Real-time-Face-Parts-Recognition-System-RFPRS is an innovative computer vision application that combines real-time face detection, hand tracking, and text-to-speech technology to create an interactive learning experience for facial anatomy. The system detects when a user points their index finger at different parts of their face and provides both visual and auditory feedback about the identified facial features.

## **Features**

### **Core Functionality**
- **Real-time Face Detection**: Advanced MediaPipe face mesh detection with 468 facial landmarks
- **Hand Tracking**: Precise index finger tip tracking for interaction
- **Voice Feedback**: Text-to-speech pronunciation of facial parts
- **Visual Feedback**: On-screen display of detected facial parts
- **Mirror Mode**: Horizontally flipped display for natural interaction

### **Facial Parts Detection**
- **Eyes**: Left Eye, Right Eye (multiple detection points)
- **Nose**: Multiple nose landmark points for accurate detection
- **Mouth**: Various mouth regions and lip detection
- **Cheeks**: Left Cheek, Right Cheek detection
- **Forehead**: Upper facial region detection

### **Technical Features**
- **Threading**: Non-blocking text-to-speech implementation
- **Cooldown System**: Prevents repetitive speech announcements
- **Distance-based Detection**: Proximity algorithms for accurate touch detection
- **Real-time Processing**: Optimized for smooth video processing

## **Technology Stack**

### **Core Libraries**
- **OpenCV (cv2)**: Computer vision and image processing
- **MediaPipe**: Google's machine learning framework for face and hand detection
- **pyttsx3**: Text-to-speech synthesis
- **Threading**: Concurrent speech processing
- **Time**: Cooldown and timing management

### **System Requirements**
- **Python**: 3.7 or higher
- **Webcam**: USB or built-in camera
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 4GB RAM recommended
- **Processor**: Multi-core processor for optimal performance

## **Installation**

### **Prerequisites**
Ensure you have Python 3.7+ installed on your system.

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/AbubakarZubair/Real-time-Face-Parts-Recognition-System-RFPRS.git
cd Real-time-Face-Parts-Recognition-System-RFPRS
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Manual Installation (if requirements.txt is not available)**
```bash
pip install opencv-python
pip install mediapipe
pip install pyttsx3
```

## **Usage**

### **Running the Application**
```bash
python main.py
```

### **How to Use**
1. **Launch the application** - Run the Python script
2. **Position yourself** - Sit in front of your webcam with good lighting
3. **Point your finger** - Use your index finger to point at different parts of your face
4. **Listen and learn** - The system will announce the facial part you're pointing at
5. **Exit** - Press 'q' to quit the application

### **Tips for Best Performance**
- **Lighting**: Ensure good, even lighting on your face
- **Distance**: Maintain 2-3 feet distance from the camera
- **Background**: Use a plain background for better detection
- **Finger Position**: Point directly at facial features for accurate detection

## **Technical Architecture**

### **Core Components**

#### **1. Face Detection Module**
- Utilizes MediaPipe's Face Mesh solution
- Processes 468 facial landmarks in real-time
- Optimized for single-face detection

#### **2. Hand Tracking Module**
- MediaPipe Hands solution for precise finger tracking
- Focuses on index finger tip coordinates
- Real-time hand gesture recognition

#### **3. Speech Engine**
- pyttsx3 integration for text-to-speech
- Threaded implementation for non-blocking operation
- Configurable speech rate and volume

#### **4. Detection Algorithm**
```python
# Proximity Detection Logic
distance = sqrt((finger_x - landmark_x)² + (finger_y - landmark_y)²)
if distance < threshold:
    trigger_speech(facial_part)
```

## **Configuration**

### **Adjustable Parameters**
- **Detection Threshold**: Modify proximity sensitivity
- **Speech Cooldown**: Adjust time between announcements
- **Speech Rate**: Configure speaking speed
- **Volume Level**: Set audio output level

### **Customization Options**
```python
# In main.py
speech_cooldown = 0.5  # Time between speech (seconds)
detection_threshold = 0.03  # Proximity threshold
speech_rate = 200  # Words per minute
volume_level = 0.9  # Volume (0.0 to 1.0)
```

## **Facial Landmarks Reference**

### **Primary Detection Points**
| Facial Part | Landmark IDs | Description |
|-------------|--------------|-------------|
| Nose | 1, 2, 5, 6 | Nose tip and bridge |
| Left Eye | 263, 386, 374, 362 | Eye corners and center |
| Right Eye | 33, 159, 145, 133 | Eye corners and center |
| Mouth | 61, 13, 14, 17, 18, 200 | Lip corners and center |
| Forehead | 9, 10, 151 | Upper facial region |
| Left Cheek | 280, 345, 346, 347 | Left facial side |
| Right Cheek | 50, 116, 117, 118 | Right facial side |

## **Troubleshooting**

### **Common Issues**

#### **Camera Not Detected**
- Ensure webcam is connected and not used by other applications
- Check camera permissions in system settings
- Try different camera index: `cv2.VideoCapture(1)`

#### **Speech Not Working**
- Verify pyttsx3 installation
- Check system audio settings
- Try different TTS engines:
```python
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
```

#### **Poor Detection Accuracy**
- Improve lighting conditions
- Adjust detection threshold
- Ensure proper distance from camera
- Check camera resolution and quality

#### **Performance Issues**
- Close unnecessary applications
- Reduce detection threshold
- Disable face mesh visualization
- Use lower camera resolution

## **Future Enhancements**

### **Planned Features**
- **Multi-language Support**: Support for different languages
- **Custom Voice Training**: Personalized voice models
- **Gesture Recognition**: Additional hand gestures
- **Mobile App**: iOS and Android versions
- **AR Integration**: Augmented reality overlay
- **Educational Games**: Interactive learning modules

### **Technical Improvements**
- **GPU Acceleration**: CUDA support for faster processing
- **Model Optimization**: Lightweight models for mobile devices
- **Cloud Integration**: Remote processing capabilities
- **Analytics Dashboard**: Usage statistics and learning progress


### **Contribution Guidelines**
- Follow PEP 8 coding standards
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation as needed


## **Acknowledgments**

- **Google MediaPipe Team** - For the excellent face and hand detection frameworks
- **OpenCV Community** - For computer vision tools and documentation
- **pyttsx3 Developers** - For the text-to-speech library
- **Contributors** - Myself

## **Contact Information**

- **Project Maintainer**: [AbuBakkar Zubair]
- **Email**: [abubakarkhan17110@gmail.com]
- **GitHub**: [(https://github.com/AbubakarZubair)]

## **Version History**

### **v1.0.0** (Current)
- Initial release
- Basic face parts detection
- Text-to-speech integration
- Real-time hand tracking

### **Upcoming Releases**
- **v1.1.0**: Enhanced detection accuracy
- **v1.2.0**: Multi-language support
- **v2.0.0**: Mobile application

---

**Made with ❤️ for interactive learning and computer vision**
