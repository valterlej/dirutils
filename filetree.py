from anytree import Node, RenderTree
from anytree.iterators import LevelOrderIter
from anytree.resolver import Resolver
from anytree.dotexport import RenderTreeGraph
import os


class File(Node):

    def __init__(self, name, parent=None, children=None, load=False):
        super(File, self).__init__(name, parent, children)
        self.name = name
        self.length = 0
        self.width = 0
        self.parent = parent
        if children:
            self.children = children
        if load:
            self.list_dir(self)

    def list_dir(self, r):
        if not os.path.isfile(r.get_path()):
            files = os.listdir(r.get_path())
            for f in files:
                file = File(f, parent=r)
                self.list_dir(file)

    def get_path(self):
        x = self.path[-1]
        path = os.path.join('', self.name)
        while x.parent is not None:
            x = x.parent
            path = os.path.join(x.name, path)
        return path

    def get_name(self):
        return self.name

    def get_all_sub_files(self, filter=None):
        nodes = [node for node in LevelOrderIter(self)]
        paths = []
        for node in nodes:
            if node.is_file():
                if filter is None:
                    paths.append(node)
                elif node.name.find(filter) != -1:
                    paths.append(node)
        return paths

    def get_all_sub_files_path(self, filter=None):
        nodes = [node for node in LevelOrderIter(self)]
        paths = []
        for node in nodes:
            if node.is_file():
                if filter is None:
                    paths.append(node.get_path())
                elif node.name.find(filter) != -1:
                    paths.append(node.get_path())
        return paths

    def get_all_sub_files_name(self, filter=None):
        nodes = [node for node in LevelOrderIter(self)]
        names = []
        for node in nodes:
            if node.is_file():
                if filter is None:
                    names.append(node.name)
                elif node.name.find(filter) != -1:
                    names.append(node.name)
        return names

    def get_all_files_from_here(self, filter=None):
        if not self.is_file():
            if filter is None:
                return [file for file in self.children if file.is_file()]
            else:
                return [file for file in self.children if file.is_file() and file.name.find(filter) != -1]
        else:
            return []

    def get_all_files_path_from_here(self, filter=None):
        if not self.is_file():
            if filter is None:
                return [file.get_path() for file in self.children if file.is_file()]
            else:
                return [file.get_path() for file in self.children if file.is_file() and file.name.find(filter) != -1]
        else:
            return []

    def get_all_files_name_from_here(self, filter=None):
        if not self.is_file():
            if filter is None:
                return [file.name for file in self.children if file.is_file()]
            else:
                return [file.name for file in self.children if file.is_file() and file.name.find(filter) != -1]
        else:
            return []

    def get_file_by_name(self, name=None):
        r = Resolver('name')
        nodes = [node for node in LevelOrderIter(self)]
        for node in nodes:
            try:
                node = r.get(node, name)
                if node.is_file():
                    return node
            except:
                pass
        return None

    def get_file_path_by_name(self, name=None):
        r = Resolver('name')
        nodes = [node for node in LevelOrderIter(self)]
        for node in nodes:
            try:
                node = r.get(node, name)
                if node.is_file():
                    return node.get_path()
            except:
                pass
        return None

    def get_directory_by_name(self, name=None):
        r = Resolver('name')
        nodes = [node for node in LevelOrderIter(self)]
        for node in nodes:
            try:
                node = r.get(node, name)
                if not node.is_file():
                    return node
            except:
                pass
        return None

    def get_directory_path_by_name(self, name=None):
        r = Resolver('name')
        nodes = [node for node in LevelOrderIter(self)]
        for node in nodes:
            try:
                node = r.get(node, name)
                if not node.is_file():
                    return node.get_path()
            except:
                pass
        return None

    def get_sub_directories_from_here(self):
        return [file for file in self.children if not file.is_file()]

    def get_sub_directories_path_from_here(self):
        return [file.get_path() for file in self.children if not file.is_file()]

    def get_sub_directories_name_from_here(self):
        return [file.name for file in self.children if not file.is_file()]

    def is_file(self):
        if self.children is None or len(self.children) == 0:
            return True
        else:
            return False

    def print_tree(self):
        for pre, fill, node in RenderTree(self):
            print('%s%s' % (pre, node.name))

    def export_as_image(self, file_name='tree.png'):
        RenderTreeGraph(self).to_picture(file_name)
