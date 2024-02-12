import cv2

# Open the default camera (usually 0 or -1) if not present the use for loop till 4 th index
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  #codec should be change as needed
#out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (640, 480))  # Adjust parameters as needed for sepcific file type and its size

while cap.isOpened():
    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized_img = cv2.equalizeHist(gray_frame)

    # Convert to BGRA (including alpha channel)
    colour = cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGRA)
    
    # Display the frame
    cv2.imshow('Captured Video', colour)

    # Write the frame to the output video file
#    out.write(colour)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
cap.release()
#out.release()  # Release the ouputfile object
cv2.destroyAllWindows()
