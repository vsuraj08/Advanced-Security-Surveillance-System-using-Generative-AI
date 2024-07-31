import serial
import cv2
import time
# Establish serial connection with Arduino
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with the appropriate port for your Arduino

# Open webcam
cap = cv2.VideoCapture(0)
print("start")
while True:
    # Check for signal from Arduino
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').rstrip()
        if message == "DoorbellPressed":
            print("Doorbell pressed detected!")

            # Capture an image from the webcam
            ret, image = cap.read()
            
            # Save the captured image
            cv2.imwrite('captured_image.jpg', image)
            
    # Sleep for a short duration to avoid high CPU usage
    # You can adjust the sleep time according to your requirements
    time.sleep(0.1)

# Release resources
cap.release()
cv2.destroyAllWindows()



# import serial
# import cv2

# # Establish serial connection with Arduino
# ser = serial.Serial('COM4',9600)  # Replace 'COM3' with the appropriate port for your Arduino

# # Open webcam
# cap = cv2.VideoCapture(0)

# doorbell_pressed = False

# while True:
#     # Check for signal from Arduino
#     if ser.in_waiting > 0:
#         message = ser.readline().decode('utf-8').rstrip()
#         if message == "DoorbellPressed":
#             print("Doorbell pressed detected!")
#             doorbell_pressed = True
            
#             # Capture an image from the webcam
#             ret, image = cap.read()
            
#             # Save the captured image
#             cv2.imwrite('captured_image.jpg', image)
            
#             # Exit the loop after capturing the image
#             break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
