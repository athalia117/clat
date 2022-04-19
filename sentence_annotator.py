import xml.etree.ElementTree as Et


class SentenceAnnotator:
    def __init__(self, f):
        self.f = f
        self.tree = None
        self.root = None
        self.sent = None
        self.data = None
        self.get_tree()
        self.get_sent()

    def get_tree(self):
        self.tree = Et.parse(self.f)
        self.root = self.tree.getroot()

    def get_sent(self):
        self.sent = self.root.find('sentence').text.split()
        self.data = [{'begin': x.get('begin'),
                      'id': x.get('id'),
                      'word': x.get('word'),
                      'pt': x.get('pt')}
                     for x in self.root.iter('node')
                     if x.get('word') is not None]

    def update_tree(self, node_id, pt):
        print(node_id, pt)
        el = self.root.find(f'.//node[@id="{node_id}"]')
        el.set('pt', pt)

    def annotate(self):
        for word in self.data:
            answer = input(f'{word["word"]} {word["pt"]}: y/n')
            if answer == 'n':
                tag = input('Correct tag: ')
                self.update_tree(word["id"], tag)

    def save_tree(self):
        print(Et.dump(self.tree))

