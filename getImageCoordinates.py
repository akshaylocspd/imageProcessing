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

        # Call the locateCenterOnImage function with the file paths in the temporary directory
        return locateCenterOnImage(os.path.join(temp_dir, 'A.png'), os.path.join(temp_dir, 'B.png'))

