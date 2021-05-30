import abc
from agglomerative_clustering import AgglomerativeClustering
import sys


class Link:
    @abc.abstractmethod
    def compute(self, cluster, other):
        return


class SingleLink(Link):
    def __init__(self):
        pass

    def compute(self, cluster, other):
        distances = AgglomerativeClustering.distances
        min_d = distances[(cluster.samples[0].s_id, other.samples[0].s_id)]
        for s_cluster in cluster.samples:
            for s_other in other.samples:
                current_distance = distances[(s_cluster.s_id, s_other.s_id)]
                if current_distance < min_d:
                    min_d = current_distance
        return min_d


class CompleteLink(Link):
    def __init__(self):
        pass

    def compute(self, cluster, other):
        distances = AgglomerativeClustering.distances
        max_d = distances[(cluster.samples[0].s_id, other.samples[0].s_id)]
        for s_cluster in cluster.samples:
            for s_other in other.samples:
                current_distance = distances[(s_cluster.s_id, s_other.s_id)]
                if current_distance > max_d:
                    max_d = current_distance
        return max_d
