import numpy as np
import cv2
import os 

def add_salt_pepper_noise(image, noise_level):
    noisy_image = np.copy(image)
    height, width = noisy_image.shape
    
    # Calculate the number of noisy pixels
    num_noisy_pixels = int(height * width * noise_level)
    
    # Generate random coordinates for noisy pixels
    noise_coords = np.random.randint(0, height, num_noisy_pixels), np.random.randint(0, width, num_noisy_pixels)
    
    # Half of the noisy pixels will be white (255) and the other half black (0)
    noisy_image[noise_coords[0][:num_noisy_pixels // 2], noise_coords[1][:num_noisy_pixels // 2]] = 255
    noisy_image[noise_coords[0][num_noisy_pixels // 2:], noise_coords[1][num_noisy_pixels // 2:]] = 0
    
    return noisy_image

def apply_mean_filter(image):
    return cv2.blur(image, (3, 3))

def apply_median_filter(image):
    return cv2.medianBlur(image, 3)

# Load image and convert to grayscale
color_image = cv2.imread(r"C:\Users\AliWH\Desktop\AI og data\Lektion 3\fruits..jpg")
image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Define noise level (X% of pixels)
noise_level = 0.05  # Adjust this value as needed

# Add salt-pepper noise
noisy_image = add_salt_pepper_noise(image, noise_level)

# Apply mean filter
mean_filtered_image = apply_mean_filter(noisy_image)

# Apply median filter
median_filtered_image = apply_median_filter(noisy_image)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Mean Filtered Image", mean_filtered_image)
cv2.imshow("Median Filtered Image", median_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create directory to save processed images
output_folder = r"C:\Users\AliWH\Desktop\AI og data\Lektion 3"
os.makedirs(output_folder, exist_ok=True)

# Save processed images
cv2.imwrite(os.path.join(output_folder, "original_grayscale_image.jpg"), image)
cv2.imwrite(os.path.join(output_folder, "noisy_image.jpg"), noisy_image)
cv2.imwrite(os.path.join(output_folder, "mean_filtered_image.jpg"), mean_filtered_image)
cv2.imwrite(os.path.join(output_folder, "median_filtered_image.jpg"), median_filtered_image)
