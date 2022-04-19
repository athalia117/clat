import xml.etree.ElementTree as Et
import os


class PosTagAnnotator:
    def __init__(self, folder):
        self.folder = folder
        self.files = []
        self.sentences = []
        self.data = []
        self.annotated = 'raw'

    def get_trees(self):
        for filename in sorted(os.listdir(self.folder)):
            self.files.append(filename)
            f = os.path.join(self.folder, filename)
            if os.path.isfile(f):
                root = Et.parse(f).getroot()
                self.sentences.append(root.find('sentence').text.split())
                self.data.append([{'begin': x.get('begin'),
                                   'word': x.get('word'),
                                   'pt': x.get('pt')}
                                  for x in root.iter('node')
                                  if x.get('word') is not None])

    def save_data(self):
        for filename, data in zip(self.files, self.data):
            with open(f'files/out/{self.folder.split("/")[-1]}/{self.annotated}/{filename.split(".")[0]}.tsv', 'w') as f:
                for i, word in enumerate(data):
                    if i > 0:
                        f.write('\n')
                    f.write(f'{word["begin"]}\t{word["word"]}\t{word["pt"]}')
