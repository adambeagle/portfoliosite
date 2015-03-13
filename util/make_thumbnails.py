"""
make_thumbnails.py
Author: Adam Beagle

NOTE: This file requires PIL/Pillow, which is not part of the acwedding_project
requirements. See docs/installation.rst.

PURPOSE
=======
  This module automates the creation of thumbnails.
  Thumbnails are ugly-cropped to fit a square.
  
USAGE
=====
  python make_thumbnails.py [-r --recursive] SRCPATH DESTPATH
  
  If SRCPATH is a directory path, thumbnils of all image files within the 
  directory (non-recursive) will be placed in DESTPATH
  
  If SRCPATH is a file path, its thumbnail will be placed in DESTPATH.
  
  The thumbnail files are the original filename, with extension,
  with ".thumbnail" appended. 

EXAMPLE
=======
  Assuming the following directory structure:
    make_thumbnails.py
    images/
      image1.png
      image2.jpg
    thumbnails/
    
  After running the following command...
  
    python make_thumbnails.py images thumbnails
    
  ...the directory structure would be the following:
  
  make_thumbnails.py
  images/
    image1.png
    image2.jpg
  thumbnails/
    image1.png.thumbnail
    image2.jpg.thumbnail
"""
from argparse import ArgumentParser
from os import makedirs
from os.path import basename, isdir, join

from PIL import Image, ImageOps

from imageutil import iter_image_paths

MAX_SIZE = (100, 100)

def make_thumbnail(srcpath, destdir, max_size=MAX_SIZE):
    """
    Saves a thumbnail of image pointed to by 'srcpath' in 'destdir.'
    MAX_SIZE expects length 2 container (width, height).
    
    If `destdir` does not exist, its creation will be attempted with os.makedirs.
    """
    image = Image.open(srcpath)
    image = ImageOps.fit(image, MAX_SIZE, Image.ANTIALIAS)
    
    # Try to create destdir if it does not exist
    if not isdir(destdir):
        makedirs(destdir)
    
    destpath = join(destdir, basename(srcpath)  + '.thumbnail')
    image.save(destpath, 'png')
    print('Thumbnail for {0} saved to {1}'.format(srcpath, destpath))

##############################################################################
if __name__ == '__main__':
    parser = ArgumentParser(description="Make image thumbnails with PIL")
    parser.add_argument('srcpath',
        help='Path to image or directory containing images'
    )
    parser.add_argument('destpath',
        help='Path to directory where thumbnails will be placed'
    )
    parser.add_argument('-r', '--recursive',
        help='Turn on recursive directory traversal',
        action='store_true',
    )
    args = parser.parse_args()
        
    for imgpath in iter_image_paths(args.srcpath, recursive=args.recursive):
        make_thumbnail(imgpath, args.destpath)
