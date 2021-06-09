class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    # the function receives another cluster and appends all of its samples to self, then deletes the another cluster
    def merge(self, other):
        for sample in other.samples:
            self.samples.append(sample)
        self.samples.sort(key=lambda x: x.s_id)
        del other

    # returns lexicographically sorted list of dominant labels of the cluster
    def compute_dominant_label(self):
        label_count = {}
        for s in self.samples:
            label_count[s.label] = 0
        for s in self.samples:
            label_count[s.label] = label_count[s.label] + 1
        maximum_label = max(label_count.values())
        dominant_labels_list = []
        for key in label_count.keys():
            if label_count[key] == maximum_label:
                dominant_labels_list.append(key)
        dominant_labels_list.sort()
        return dominant_labels_list

    # receives silhouette of self and prints the details of the cluster as requested
    def print_details(self, silhouette):
        self.samples.sort(key=lambda x: x.s_id)
        id_list = [sample.s_id for sample in self.samples]
        label = self.compute_dominant_label()
        print("Cluster {}: {id}, dominant label = {dominant}, silhouette = {sil:.3f}".format(self.c_id,
                                                                                             id=id_list,
                                                                                             dominant=label,
                                                                                             sil=silhouette))
