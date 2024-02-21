import PIL as pl
import numpy as np

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
    classifications = np.zeros((len(data)))
    # Iterate until convergence is reached
    changed = False
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
            # Re-assign point to cluster
            if closestJ != classifications[i]:
                classifications[i] = closestJ
                changed = True
            # Add point to cluster sum
            sums[closestJ] += point
            counts[closestJ] += 1
        # Re-calculate means
        for i in range(len(means)):
            means[i] = sums[i] / counts[i]
    return (means, classifications)
