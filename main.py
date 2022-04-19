import sys
from sentence_annotator import SentenceAnnotator


def main(argv):
    _, infile = argv
    sa = SentenceAnnotator(infile)
    sa.annotate()
    sa.save_tree()


if __name__ == '__main__':
    main(sys.argv)
