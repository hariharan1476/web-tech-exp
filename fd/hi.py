import serial
import time
import cv2
from pyzbar.pyzbar import decode

# Function to read RFID tags
def read_rfid():
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust port and baud rate as needed
    try:
        while True:
            data = ser.read(12)  # Assuming RFID tag data is 12 characters
            if data:
                print("RFID Tag:", data.decode('utf-8'))
    except KeyboardInterrupt:
        ser.close()

# Function to capture and decode barcodes from camera
def read_barcode():
    cap = cv2.VideoCapture(0)  # Use default camera (index 0), adjust if needed
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            decoded_objects = decode(gray)
            for obj in decoded_objects:
                print("Barcode Type:", obj.type)
                print("Barcode Data:", obj.data.decode('utf-8'))
                # Draw a rectangle around the barcode
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points
                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
            cv2.imshow('Barcode Scanner', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Starting RFID scanning...")
    read_rfid()