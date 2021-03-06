import csv
import random

labels = ['A', 'B', 'C', 'D', 'E', 'F']


def generate_data(path):
    with open(path, 'w') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',')

        data_writer.writerow(['x', 'y', 'label'])

        for _ in range(100):
            centerX, centerY = random.random() * 5.0, random.random() * 5.0
            data_writer.writerow([random.gauss(centerX, 0.5), random.gauss(centerY, 0.5), random.choice(labels)])


if __name__ == '__main__':
    generate_data('bayes_data.csv')
