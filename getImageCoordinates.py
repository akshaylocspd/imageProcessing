import tempfile
import os
import cv2


def locateCenterOnImage(template_image_path, source_image_path):
    # Load the template and source images
    template = cv2.imread(template_image_path, cv2.IMREAD_GRAYSCALE)
    source = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # Calculate the center point of the template in the source image
    template_w, template_h = template.shape[::-1]
    center_x = int(max_loc[0] + template_w / 2)
    center_y = int(max_loc[1] + template_h / 2)

    # Return the center point as a tuple
    return (center_x, center_y)

def getCoordinates(img_data_a,img_data_b):
    # Create a temporary directory to store the PNG files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Write bytes to PNG files in the temporary directory
        with open(os.path.join(temp_dir, 'A.png'), 'wb') as f:
            f.write(img_data_a)
        with open(os.path.join(temp_dir, 'B.png'), 'wb') as f:
            f.write(img_data_b)

            aFilePath=os.path.join(temp_dir, 'A.png')
            bFilePath=os.path.join(temp_dir, 'B.png')
        # Call the locateCenterOnImage function with the file paths in the temporary directory
        return locateCenterOnImage(aFilePath, bFilePath),is_A_is_SubsetOf_B(aFilePath,bFilePath)


def is_A_is_SubsetOf_B(aFilePath,bFilePath):
    # Load images
    img_a = cv2.imread(aFilePath, 0)
    img_b = cv2.imread(bFilePath, 0)
    # Perform template matching
    result = cv2.matchTemplate(img_b, img_a, cv2.TM_CCOEFF_NORMED)

    # Define a threshold for similarity
    threshold = 0.8

    # Get the location of the matched area
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        print("A.png is found within B.png")
        # You can access the top-left and bottom-right coordinates of the matched area using max_loc
        top_left = max_loc
        bottom_right = (top_left[0] + img_a.shape[1], top_left[1] + img_a.shape[0])
        print("Matched Area Coordinates: Top Left:", top_left, "Bottom Right:", bottom_right)
        return True
    else:
        print("A.png is not found within B.png")
        return False
