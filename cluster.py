class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        for sample in other.samples:
            self.samples.append(sample)
        self.samples.sort(key=lambda x: x.s_id)
        del other

    def compute_dominant_label(self):
        label_list = [s.label for s in self.samples]
        return max(label_list, key=label_list.count)

    def print_details(self, silhouette):
        self.samples.sort(key=lambda x: x.s_id)
        id_list = [sample.s_id for sample in self.samples]
        label = self.compute_dominant_label()
        print("Cluster {:.3f}: {id}, dominant label = {dominant}, silhouette = {sil:.3f}".format(self.c_id,
                                                                                                 id=id_list,
                                                                                                 dominant=label,
                                                                                                 sil=silhouette))
