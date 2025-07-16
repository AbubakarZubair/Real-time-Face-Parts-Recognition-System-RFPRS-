import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

import cv2
import mediapipe as mp
import pyttsx3
import threading
import time

# Initialize MediaPipe Face Mesh and Hands solutions
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create instances
face_mesh = mp_face_mesh.FaceMesh()
hands = mp_hands.Hands()

# Initialize TTS engine with better settings
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Faster speech rate
engine.setProperty('volume', 0.9)  # Set volume level

# Global variables for tracking
last_spoken_part = None
last_speak_time = 0
speech_cooldown = 0.2  # Reduced cooldown time
is_speaking = False  # Track if currently speaking

# Text-to-speech function with improved threading
def speak(text):
    global is_speaking
    
    def speak_thread():
        global is_speaking
        try:
            is_speaking = True
            # Stop any current speech
            engine.stop()
            # Clear the queue
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")
        finally:
            is_speaking = False
    
    # Don't start new speech if already speaking
    if not is_speaking:
        thread = threading.Thread(target=speak_thread)
        thread.daemon = True
        thread.start()

# Open webcam
cap = cv2.VideoCapture(0)

# Landmark indices for specific face parts (corrected for mirror effect)
FACE_PARTS = {
    1: "Nose",
    33: "Left Eye",  # Flipped: was Right Eye
    263: "Right Eye",  # Flipped: was Left Eye
    61: "Mouth",
    10: "Forehead",
    50: "Left Cheek",  # Flipped: was Right Cheek
    280: "Right Cheek"  # Flipped: was Left Cheek
}

# Additional face part indices for better coverage (corrected for mirror effect)
ADDITIONAL_FACE_PARTS = {
    # More nose points
    2: "Nose",
    5: "Nose",
    6: "Nose",
    
    # More eye points (flipped)
    159: "Left Eye",  # Flipped: was Right Eye
    145: "Left Eye",  # Flipped: was Right Eye
    133: "Left Eye",  # Flipped: was Right Eye
    386: "Right Eye",  # Flipped: was Left Eye
    374: "Right Eye",  # Flipped: was Left Eye
    362: "Right Eye",  # Flipped: was Left Eye
    
    # More mouth points
    13: "Mouth",
    14: "Mouth",
    17: "Mouth",
    18: "Mouth",
    200: "Mouth",
    
    # More forehead points
    9: "Forehead",
    151: "Forehead",
    
    # More cheek points (flipped)
    116: "Left Cheek",  # Flipped: was Right Cheek
    117: "Left Cheek",  # Flipped: was Right Cheek
    118: "Left Cheek",  # Flipped: was Right Cheek
    345: "Right Cheek",  # Flipped: was Left Cheek
    346: "Right Cheek",  # Flipped: was Left Cheek
    347: "Right Cheek"  # Flipped: was Left Cheek
}

# Combine all face parts
ALL_FACE_PARTS = {**FACE_PARTS, **ADDITIONAL_FACE_PARTS}

current_detected_part = "None"

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for mirror effect
    image = cv2.flip(image, 1)
    
    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image for face and hand landmarks
    face_results = face_mesh.process(image_rgb)
    hand_results = hands.process(image_rgb)
    
    # Reset current detected part
    current_detected_part = "None"
    
    if face_results.multi_face_landmarks and hand_results.multi_hand_landmarks:
        face_landmarks = face_results.multi_face_landmarks[0]
        
        # Optional: Draw only hand landmarks (remove face mesh clutter)
        # mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)
        
        for hand_landmarks in hand_results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the index finger tip coordinates
            finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            fx, fy = finger_tip.x, finger_tip.y
            
            # Convert to pixel coordinates for display
            h, w, _ = image.shape
            finger_x, finger_y = int(fx * w), int(fy * h)
            
            # Draw finger tip
            cv2.circle(image, (finger_x, finger_y), 10, (0, 255, 0), -1)
            
            # Check proximity to face landmarks
            closest_part = None
            min_distance = float('inf')
            
            for id, landmark in enumerate(face_landmarks.landmark):
                lx, ly = landmark.x, landmark.y
                
                # Calculate distance
                distance = ((fx - lx) ** 2 + (fy - ly) ** 2) ** 0.5
                
                # Check if finger is close to this landmark
                if distance < 0.03:  # Adjusted threshold
                    if id in ALL_FACE_PARTS and distance < min_distance:
                        min_distance = distance
                        closest_part = ALL_FACE_PARTS[id]
            
            if closest_part:
                current_detected_part = closest_part
                current_time = time.time()
                
                # More aggressive speech triggering
                should_speak = (
                    closest_part != last_spoken_part or 
                    current_time - last_speak_time > speech_cooldown
                ) and not is_speaking
                
                if should_speak:
                    print(f"Detected: {closest_part}")  # Print to console
                    speak(closest_part)
                    last_spoken_part = closest_part
                    last_speak_time = current_time
    
    # Display current detected part on screen with speech status
    speech_status = "Speaking..." if is_speaking else "Ready"
    cv2.putText(image, f"Detected: {current_detected_part} ({speech_status})", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    # Display instructions
    cv2.putText(image, "Point your index finger at face parts", 
                (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(image, "Press 'q' to quit", 
                (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Display the image
    cv2.imshow('Face Parts Detection', image)
    
    # Listen for key events to exit the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()