

class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    # recieves another sample and returns euclidean distance to it
    def compute_euclidean_distance(self, other):
        distance_list = []
        for i in range(len(self.genes)):
            distance_list.append((self.genes[i] - other.genes[i]) ** 2)
        return sum(distance_list) ** 0.5
