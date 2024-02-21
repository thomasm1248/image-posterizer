import PIL as pl

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
    classifications = None # TODO
    # Iterate until convergence is reached
    changed = False
    while changed == True:
        changed = False
        # Re-classify points and keep running total
        # Re-calculate means
    return (means, classifications)
