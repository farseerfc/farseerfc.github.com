import fnmatch
import os

zhposts = []

for root, dirs, filenames in os.walk('posts'):
    for filename in fnmatch.filter(filenames,'*.rst'):
        if fnmatch.fnmatch(filename, '*.*.rst'):
            continue
        zhposts.append((root, filename))


        
for root, post in zhposts:
    cpcmd = 'copy %s opencc\\input.txt'%(os.path.join(root, post))
    print cpcmd
    os.system(cpcmd)
    os.chdir('opencc')
    cccmd = 'opencc -czht2zhs.ini -iinput.txt -ooutput.txt'
    print cccmd
    os.system(cccmd)
    os.chdir('..')
    name = post[:-4]+'.zhs.rst'
    cpcmd = 'copy opencc\\output.txt %s'%(os.path.join(root, name))
    print cpcmd
    os.system(cpcmd)
    
    fd=open(os.path.join(root,name))
    lines = fd.readlines()
    fd.close()
    for i in range(len(lines)):
        if lines[i].strip() == ':lang: zh':
            lines[i]=':lang: zhs\n'
    fd=open(os.path.join(root,name),'w')
    fd.writelines(lines)
    fd.close()
