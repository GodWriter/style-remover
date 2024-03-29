import argparse
import yaml


def parse_args():
    """
    parsing and configuration
    :return: parse_args
    """
    desc = "TensorFlow implementation of fast-style-GAN"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--module', type=str, default='test',
                        help='Module to select: train, test, test_dataset, create_dataset, train_without_affine')
    parser.add_argument('--training', type=bool, default=False,
                        help='If the model is train, this argument should be true, else False')
    parser.add_argument('--GPU', type=str, default='0',
                        help='GPU used to train the model')
    parser.add_argument('--model_file', type=str, default='model/style-remover.ckpt-done',
                        help='The model used to test')
    parser.add_argument('--test_image', type=str, default='test_image.jpg',
                        help='File path of the test image')
    parser.add_argument('--test_dir', type=str, default='data/test',
                        help='images to transfer')
    parser.add_argument('--save_dir', type=str, default='generated',
                        help='Path to save the generated images')
    parser.add_argument('--config', type=str, default='config/experiment-huanghun.yml',
                        help='Path of config file for testing')

    return parser.parse_args()


def read_conf_file(conf_file):
    class Args(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)

    with open(conf_file) as f:
        args = Args(**yaml.load(f))
    return args
