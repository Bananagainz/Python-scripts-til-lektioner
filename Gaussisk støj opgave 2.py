import numpy as np
import cv2
import os 

def add_gaussian_noise(image, mean, sigma):
    height, width = image.shape
    gaussian_noise = np.random.normal(mean, sigma, (height, width))
    noisy_image = np.clip(image + gaussian_noise, 0, 255).astype(np.uint8)
    return noisy_image

def apply_mean_filter(image):
    return cv2.blur(image, (3, 3))

def apply_median_filter(image):
    return cv2.medianBlur(image, 3)

# Load image and convert to grayscale
color_image = cv2.imread(r"C:\Users\AliWH\Desktop\AI og data\Lektion 3\fruits..jpg")
image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Define parameters for Gaussian noise
mean = 0
sigma = 25  # Adjust sigma as needed

# Add Gaussian noise
noisy_image = add_gaussian_noise(image, mean, sigma)

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
output_folder = r"C:\Users\AliWH\Desktop\AI og data\Lektion 3\opgave 2"
os.makedirs(output_folder, exist_ok=True)

# Save processed images
cv2.imwrite(os.path.join(output_folder, "original_grayscale_image.jpg"), image)
cv2.imwrite(os.path.join(output_folder, "noisy_image.jpg"), noisy_image)
cv2.imwrite(os.path.join(output_folder, "mean_filtered_image.jpg"), mean_filtered_image)
cv2.imwrite(os.path.join(output_folder, "median_filtered_image.jpg"), median_filtered_image)
