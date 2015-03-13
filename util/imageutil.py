"""
imageutil.py
Author: Adam Beagle

PURPOSE:
  This module contains functionalty common to image processing tasks.
  
USAGE:
    The only public function is iter_image_paths, which yields absolute image
    paths in a given directory.
"""
from os import listdir, walk
from os.path import abspath, exists, isdir, isfile, join, splitext
import re

FORMATS = ['png', 'jpg', 'jpeg']

def _format_formats(formats):
    """
    Return list in which all items from `formats` have a leading period.
    If items in `formats` not of form 'ext' or '.ext', ValueError is raised 
    (this is because they are compared against os.path.splitext()).
    """
    for f in formats:
        if not re.match('\.?[a-z0-9]+$', f, re.IGNORECASE):
            raise ValueError(
                "Extensions in `formats` should be of form 'ext' or '.ext'." +
                "Got: {}".format(formats)
            )
    return ['.{}'.format(ext.lower()) for ext in formats if ext[0] != '.']

FORMATS = _format_formats(FORMATS)

def _is_image(path, formats):
    """
    Return True if `path` points to an image file, i.e. it has an extension
    found in`formats.`
    
    Assumes items in `formats` have leading periods.
    """
    return isfile(path) and splitext(path)[1].lower() in formats
    
def _walk_image_paths(srcpath, formats):
    """
    Recursively walk through directory given by `srcpath` and yield any image
    paths (as defined in _is_image) found.
    
    Assumes `srcpath` is an absolute path to an existing directory., and that
    items in `formats` formatted as by _format_formats().
    """
    for (dirpath, dirnames, filenames) in walk(srcpath):
        for filename in filenames:
            joined = join(dirpath, filename)
            if _is_image(joined, formats):
                yield joined
                
def _list_image_paths(srcpath, formats):
    """
    Yield all image paths (as defined by _is_image) in a single directory 
    given by `srcpath.`
    
    Assumes `srcpath` is an absolute path to an existing directory., and that
    items in `formats` are formatted as by _format_formats().
    """
    for filename in listdir(srcpath):
        joined = join(srcpath, filename)
        
        if _is_image(joined, formats):
            yield joined

def iter_image_paths(srcpath, recursive=True, formats=FORMATS):
    """
    Yield absolute paths of all images in path given by 'srcpath.'
    
    A file is considered an image if its extension matches those given in
    container 'formats' (case insensitive).
    
    If srcpath points to a file, its absolute path will be yielded if it is 
    an image. If it is not an image, nothing will be yielded (and no
    exceptions will be raised).
    
    If srcpath does not point to an existing file or directory, ValueError will be raised.
    
    `recursive` determines whether a directory given by `srcpath` is traversed
    recursively.
    """
    if formats is not FORMATS:
        formats = _format_formats(formats)

    srcpath = abspath(srcpath)
    if not exists(srcpath):
        raise ValueError(
            "{0} not a path to an existing file or directory".format(srcpath)
        )
    
    # If srcpath is directory, yield all image paths
    if isdir(srcpath):
        # Set correct generator function 
        if recursive:
            image_paths_generator = _walk_image_paths
        else:
            image_paths_generator = _list_image_paths
            
        # Yield paths
        for imgpath in image_paths_generator(srcpath, formats):
            yield imgpath
                
    # If srcpath is file, yield if image
    elif isfile(srcpath):
            if _is_image(srcpath, formats):
                yield srcpath

    # If somehow exists() passes, but isfile() and isdir() fail, 
    # raise ValueError
    else:
        raise ValueError("Invalid path: {}".format(srcpath))
