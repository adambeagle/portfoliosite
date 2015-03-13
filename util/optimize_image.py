"""
optimize_image.py

PURPOSE:
    Given an image path or path to a directory containing images via the command
    line, this script uses the tinypng.com service to overwrite png and jpg files
    with optimized versions of the images.

USAGE:
    python optimize_image.py [-r --recursive] PATH

    PATH may be a single file or directory. If the -r/--recursive flag is set,
    a directory given by PATH is traversed recursively.
    
NOTES:
    Expects an environment variable named TINYPNG_API_KEY.
"""
import argparse
from base64 import b64encode
from os import environ
from os.path import splitext
from urllib.request import Request, urlopen

from imageutil import iter_image_paths

ERROR_LOG = 'tinypng.log'

def optimize_with_tinypng(imgpath, api_key):
    """
    Use the tinypng.com API to optimize a png or jpg image given by `imgpath.`
    Original file is overwritten.
    """
    with open(imgpath, 'rb') as f:
        request = Request("https://api.tinypng.com/shrink", f.read())
        
    auth = b64encode(bytes("api:" + api_key, "ascii")).decode("ascii")
    request.add_header("Authorization", "Basic %s" % auth)
    
    response = urlopen(request)
    
    if response.status == 201:
        # Compression was successful, retrieve output from Location header.
        result = urlopen(response.getheader("Location")).read()
        with open(imgpath, 'wb') as f:
            f.write(result)
            
        print('Successfully optimized', imgpath)
    else:
        with open(ERROR_LOG, 'w') as f:
            f.write(response)
        print("Compression failed. See {} for more.".format(ERROR_LOG))

##############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Optimize image(s) using PIL")
    parser.add_argument('path', 
        help='Image file or directory containing images', 
    )
    parser.add_argument('-r', '--recursive',
        help='Turn on recursive directory traversal',
        action='store_true',
    )
    args = parser.parse_args()
    
    # Note iter_image_paths returns absolute paths, and also accepts a
    # single file path
    for imgpath in iter_image_paths(args.path, recursive=args.recursive, formats=['png', 'jpg', 'jpeg', 'thumbnail']):
        optimize_with_tinypng(imgpath, api_key=environ['TINYPNG_API_KEY'])

