import abc


class Link:
    @abc.abstractmethod
    def compute(self, cluster, other):
        return


class SingleLink(Link):
    def compute(self, cluster, other):
        min_d = cluster.samples[0].compute_euclidean_distance(other.samples[0])
        for s_cluster in cluster.samples:
            for s_other in other.samples:
                if s_cluster.compute_euclidean_distance(s_other) < min_d:
                    min_d = s_cluster.compute_euclidean_distance(s_other)
        return min_d


class CompleteLink(Link):
    def compute(self, cluster, other):
        max_d = cluster.samples[0].compute_euclidean_distance(other.samples[0])
        for s_cluster in cluster.samples:
            for s_other in other.samples:
                if s_cluster.compute_euclidean_distance(s_other) > max_d:
                    max_d = s_cluster.compute_euclidean_distance(s_other)
        return max_d
