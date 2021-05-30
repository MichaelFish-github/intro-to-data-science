import sys
import data, sample, cluster, link, agglomerative_clustering


def main(argv):
    dataset = data.Data(argv[1])
    samples = dataset.create_samples()
    print("Single Link")
    main_algorithm = agglomerative_clustering.AgglomerativeClustering(link.SingleLink(), samples)
    main_algorithm.run(7)
    print()
    print("Complete Link")
    main_algorithm = agglomerative_clustering.AgglomerativeClustering(link.CompleteLink(), samples)
    main_algorithm.run(7)


if __name__ == '__main__':
    main(sys.argv)
