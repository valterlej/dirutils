from filetree import File

print('Creating a root file and loading all subdirectories and files.')

root = File('/media/valter/Arquivos/Datasets/UCF-101',load=True)
root.print_tree()

files = root.get_all_files_from_here(filter='.avi')
print(files)