import PIL as pl
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Upload image via the file path
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = Image.open(file_path)
        display_image(original_image)

# Display the image using Tkinter
def display_image(image):
    global panel
    if panel is not None:
        panel.destroy()
    img = ImageTk.PhotoImage(image)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack()

# Distance function to compute distance between two points
def dist(a, b):
    sum = 0.
    for i in range(len(a)):
        diff = a[i] - b[i]
        sum += diff**2
    return sum**.5

# K-means algorithm

def kmeans(data, k):
    '''
    Classify the data into k clusters.

    Args:
        data: array of datapoints, where each is an array of floats
        k: number of clusters wanted

    Returns: (means, classifications)
        means: array of datapoints that represent the means of each cluster
        classifications: array of integers that assigns each datapoint to a cluster
    '''
    # Use the first k datapoints as the starting means
    means = []
    for i in range(k):
        means.append(data[i])
    # Put all datapoints in the same group to start with
    classifications = np.zeros((len(data)), dtype=int)
    # Iterate until convergence is reached
    changed = True
    while changed == True:
        changed = False
        # Keep a running total of the points in each cluster
        sums = []
        counts = []
        for i in range(k):
            sums.append(np.zeros((len(data[0]))))
            counts.append(0)
        # Re-classify points
        for i, point in zip(range(len(data)), data):
            # Find the closest mean
            closestMean = means[0]
            closestDistance = dist(closestMean, point)
            closestJ = 0
            for j, mean in zip(range(1, len(means)), means):
                distance = dist(point, mean)
                if distance < closestDistance:
                    closestDistance = distance
                    closestMean = mean
                    closestJ = j
            print(closestJ)
            print(closestDistance)
            # Re-assign point to cluster
            if closestJ != classifications[i]:
                classifications[i] = closestJ
                changed = True
            # Add point to cluster sum
            sums[closestJ] += point
            counts[closestJ] += 1
        # Re-calculate means
        for i in range(len(means)):
            means[i] = [sums[i][j] / counts[i] if counts[i] > 0 else data[0][j] for j in range(len(sums[0]))]
    return (means, classifications)

root = tk.Tk()
root.title("Image Posterizer")

panel = None
original_image = None

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

root.mainloop()