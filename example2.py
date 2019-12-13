from itertools import accumulate

from filetree import File
import cv2

print('Creating a root file loading all subdirectories and files.')


root = File('/media/valter/Arquivos/Datasets/UCF-101',load=True)
#root.print_tree()

files = root.get_all_files_from_here(filter='.wei')

print(files)