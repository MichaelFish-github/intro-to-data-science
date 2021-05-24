import pandas
from sample import Sample


class Data:
    def __init__(self, path):
        """
                :param path: path of the csv file
                initiating data object, loading the data from the csv file and casting it to dictionary
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        samples = []
        not_genes = ["samples", "type"]
        item_num = len(self.data["samples"])
        for i in range(item_num):
            s_id = self.data["samples"][i]
            label = self.data["type"][i]
            genes = [self.data[k][i] for k in self.data if k not in not_genes]
            samples.append(Sample(s_id, genes, label))
        return samples

