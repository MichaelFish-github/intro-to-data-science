import cluster


class AgglomerativeClustering:
    distances = {}

    def __init__(self, link, samples):
        self.link = link
        self.clusters = [cluster.Cluster(s.s_id, [s]) for s in samples]

    def compute_silhoeutte(self):
        sil_dict = {}
        for c in self.clusters:
            for samp in c.samples:
                in_val = self.compute_cluster_d(samp, c, True)
                outs_values = [self.compute_cluster_d(samp, out_c, False)
                               for out_c in self.clusters if c != out_c]
                out_val = min(outs_values)
                sil_val = (out_val - in_val) / max(in_val, out_val) if in_val != 0 else 0
                sil_dict[samp.s_id] = sil_val
        return sil_dict

    def compute_summary_silhoeutte(self):
        sil_dict = self.compute_silhoeutte()
        summary_dict = {}
        population_size = 0
        population_sum = 0
        for c in self.clusters:
            cluster_sum = sum([sil_dict[s.s_id] for s in c.samples])
            population_sum += cluster_sum
            population_size += len(c.samples)
            cluster_sil = cluster_sum / len(c.samples)
            summary_dict[c.c_id] = cluster_sil
        summary_dict[0] = population_sum / population_size
        return summary_dict

    def compute_rand_index(self):
        all_clusters = self.clusters.copy()
        rand_index_dict = {}
        for current_cluster in all_clusters:
            for sample in current_cluster.samples:
                for other_cluster in all_clusters:
                    for other_sample in other_cluster.samples:
                        if sample is not other_sample:
                            if sample.label == other_sample.label:
                                if current_cluster is other_cluster:
                                    rand_index_dict[(sample.s_id, other_sample.s_id)] = [1, 0, 0, 0]
                                else:
                                    rand_index_dict[(sample.s_id, other_sample.s_id)] = [0, 0, 1, 0]
                            else:
                                if current_cluster is other_cluster:
                                    rand_index_dict[(sample.s_id, other_sample.s_id)] = [0, 0, 0, 1]
                                else:
                                    rand_index_dict[(sample.s_id, other_sample.s_id)] = [0, 1, 0, 0]
        tp = sum([v[0] for v in rand_index_dict.values()])
        fp = sum([v[2] for v in rand_index_dict.values()])
        fn = sum([v[3] for v in rand_index_dict.values()])
        tn = sum([v[1] for v in rand_index_dict.values()])
        return (tp + tn) / (tn + tp + fp + fn)

    def run(self, max_clusters):
        self.initialize_distances_dict()
        while len(self.clusters) > max_clusters:
            cluster1 = self.clusters[0]
            cluster2 = self.clusters[1]
            initial_distance = self.link.compute(cluster1, cluster2)
            for this_cluster in self.clusters:
                for other_cluster in self.clusters:
                    if this_cluster is not other_cluster:
                        current_distance = self.link.compute(this_cluster, other_cluster)
                        if current_distance < initial_distance:
                            initial_distance = current_distance
                            cluster1 = this_cluster
                            cluster2 = other_cluster
            temp_cluster = cluster2
            self.clusters.remove(cluster2)
            cluster1.merge(temp_cluster)
        summary_dict = self.compute_summary_silhoeutte()
        for c in self.clusters:
            c.print_details(summary_dict[c.c_id])
        rand_index = self.compute_rand_index()
        silhouette = summary_dict[0]
        print("Whole data silhouette = {:.3f}, RI = {:.3f}".format(float(silhouette), rand_index))

    def compute_cluster_d(self, sample, cluster_to, is_sample_cluster):
        cluster_size = len(cluster_to.samples) - 1 if is_sample_cluster else len(cluster_to.samples)
        if cluster_size == 0:
            return 0
        sum_of_distances = 0
        for other_sample in cluster_to.samples:
            if sample is not other_sample:
                sum_of_distances = sum_of_distances + self.distances[(sample.s_id, other_sample.s_id)]
        return sum_of_distances / cluster_size

    def initialize_distances_dict(self):
        for this_cluster in self.clusters:
            for other_cluster in self.clusters:
                for other_sample in other_cluster.samples:
                    for this_sample in this_cluster.samples:
                        if this_sample is not other_sample and (
                                this_sample.s_id, other_sample.s_id) not in self.distances.keys():
                            self.distances[
                                (this_sample.s_id, other_sample.s_id)] = this_sample.compute_euclidean_distance(
                                other_sample)
