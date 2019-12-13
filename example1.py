from filetree import File

r = File('/')
home = File('home', parent=r)
user = File('user', parent=home)
d1 = File('Documents', parent=user)
d2 = File('Downloads', parent=user)
f1 = File('aaa.avi', parent=d1)
f2 = File('bbb.avi', parent=d2)
f3 = File('ccc.txt', parent=d1)

print('Showing the tree structure')
r.print_tree()

print('Searching for Documents directory')
print(r.get_directory_by_name('Documents'))
print(r.get_directory_path_by_name('Documents'))

print('Searching for .avi files from root')
print(r.get_all_sub_files(filter='.avi'))
print(r.get_all_sub_files_path(filter='.avi'))
print(r.get_all_sub_files_name(filter='.avi'))

print('Searching for .avi files from Documents directory')
directory = r.get_directory_by_name('Documents')
print(directory.get_all_sub_files(filter='.avi'))
print(directory.get_all_sub_files_path(filter='.avi'))

# if you install graphviz uncomment these lines
r.export_as_image()
directory.export_as_image('subdir.png')