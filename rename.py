import os
import glob

files = glob.glob('./downloads/original/*')

for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, './downloads/renamed/other' + '{0:d}'.format(i) + fext)
    
