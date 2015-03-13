"""
transfer.py

Transfers a file or directory with SSH (via scp) to a remote machine with 
an identical hierarchy.

This script isn't meant to be a complete wrapper for scp, merely a 
convenience for a specific circumstance.

USAGE:
    python transfer.py TO PATH

    TO - name or address of machine to transfer to
    PATH - file or directory to transfer
    
EXAMPLES:
    python transfer.py remotename /home/username/file.ext
    
    The above is identical to:
    scp /home/username/file.ext remotename:/home/username/
    
    ======================
    
    python transfer.py remotename /home/username/somedir/
    
    The above is identical to:
    scp -r /home/username/somedir/ remotename:/home/username/
    
NOTES:
    Absolute paths (as shown in the examples for clarity) are not necessary.
"""
from argparse import ArgumentParser
from os.path import abspath, dirname, isdir, isfile
from subprocess import call

if __name__ == '__main__':
    # Build parser
    parser = ArgumentParser(
        description="Transfer file or directory to remote with identical layout"
    )
    parser.add_argument('to',
        help='Name of remote machine to ssh into'
    )
    parser.add_argument('path',
        help='File or directory to transfer'
    )
    args = parser.parse_args()
    
    # Transfer, or show error message if path does not point to file or dir
    path = abspath(args.path)
    if isfile(args.path):
        cmd = 'scp {} {}:{}/'.format(path, args.to, dirname(path))
    elif isdir(args.path):
        cmd = 'scp -r {}/ {}:{}/'.format(path, args.to, dirname(path))
    else:
        print('`path` is not a valid file or directory on this system.')
        exit(1)
        
    call(cmd, shell=True)
