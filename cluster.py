class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        for sample in other.samples:
            self.samples.append(sample)

        del other

    def compute_dominant_label(self):
        label_list = [s.label for s in self.samples]
        return max(label_list, key=label_list.count)

    def print_details(self, silhouette):
        self.samples.sort(key=lambda x: x.s_id)
        id_list = [sample.label for sample in self.samples]
        print(f'The IDs in this cluster are: {id_list}')
        print(f'The dominant label of this cluster is: {self.compute_dominant_label()}')
        print(f'The silhouette of the cluster is: {silhouette}')



