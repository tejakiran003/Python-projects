import cv2

def main():
    # Load the pre-trained Haar Cascade classifier
    
    cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    
    # Open the camera
    cap = cv2.VideoCapture(0)#or instead of 0 we can give video link
    
    if not cap.isOpened():
        print("Cannot open camera")
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        detections = cascade_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in detections:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Properly release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        cv2.destroyAllWindows()
