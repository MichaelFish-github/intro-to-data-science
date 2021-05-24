import sys
import data, sample, cluster, link, agglomerative_clustering


def main(argv):
    dataset = data.Data(argv[1])
    samples = dataset.create_samples()
    print(samples[2].genes[:5])


if __name__ == '__main__':
    main(sys.argv)
