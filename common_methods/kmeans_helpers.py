import math
import random

import numpy as np

from scipy.spatial.distance import euclidean

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale


def retrieve_cluster_points(cluster_index, labels, samples_matrix):
    """
    In a clustering, retrieve points (their coordinates)
    belonging to given cluster. Return array of such points.
    samples_matrix is a Numpy array.
    """

    cluster_points = []
    for sample_index in np.where(labels == cluster_index)[0]:
        cluster_points.append(samples_matrix[sample_index, :])
    cluster_points = np.array(cluster_points)

    return np.array(cluster_points)


def compute_wcss(centroids, labels, samples_matrix):
    """
    Compute the WCSS for a k-means clustering, given the
    centroids and the dataset matrix of samples.
    samples_matrix is a Numpy array.
    """

    k = len(centroids)
    wcss = 0
    for cluster_index in range(k):
        cluster_points = retrieve_cluster_points(cluster_index,
                                                 labels,
                                                 samples_matrix)
        wcss += sum([euclidean(point, centroids[cluster_index])
                    for point in cluster_points])

    return wcss


def compute_gap_statistic(samples_matrix,
                          k,
                          b=10,
                          scale_data=True):
    """
    Compute the Gap Statistic for a k-means clustering.
    b is the number of replicates to use (defaults to 10);
    k is the chosen number of clusters;
    scale_data (defaults to True): if to scale replicates samples matrix.
    Return the gap statistic, the stdev of the Monte Carlo replicas and
    the simulation error.
    samples_matrix is a Numpy array.
    """

    if scale_data:
        samples_matrix = scale(samples_matrix)
    fit = KMeans(n_clusters=k).fit(samples_matrix)
    centroids = fit.cluster_centers_
    labels = fit.labels_
    Wk = compute_wcss(centroids, labels, samples_matrix)
    Wkb = []
    for i in range(b):
        replicate = []
        for sample in range(samples_matrix.shape[0]):
            replicate_sample = \
                [random.uniform(min(samples_matrix[:, feature]),
                                max(samples_matrix[:, feature]))
                 for feature in range(samples_matrix.shape[1])]
            replicate.append(replicate_sample)
        replicate = np.array(replicate)
        if scale_data:
            replicate = scale(replicate)
        fit = KMeans(n_clusters=k).fit(replicate)
        replicate_centroids = fit.cluster_centers_
        replicate_labels = fit.labels_
        Wkb.append(compute_wcss(replicate_centroids,
                                replicate_labels,
                                replicate))
    gap = np.mean(np.log(Wkb)) - np.log(Wk)
    stdk = np.std(np.log(Wkb))
    sk = math.sqrt(1 + 1. / b) * stdk

    return gap, stdk, sk


def evaluate_gap_statistic_best_k(samples_matrix,
                                  k_min=1,
                                  k_max=10,
                                  b=10,
                                  scale_data=True):
    """
    Return the best k based on the gap statistic calculation.
    samples_matrix is a Numpy array.
    """

    k_gap = {}
    for k in range(k_min, k_max + 1):
        gap_return = compute_gap_statistic(samples_matrix,
                                           k,
                                           b=b,
                                           scale_data=scale_data)
        k_gap[k] = gap_return[0], gap_return[2]
    for k in range(k_min, k_max):
        if k_gap[k][0] - k_gap[k + 1][0] + k_gap[k + 1][1] >= 0:
            return k
    return
