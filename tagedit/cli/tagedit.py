# tagedit <https://github.com/msikma/tagedit>
# © MIT license

import sys
import argparse
import pkg_resources
from tagedit.tag import open_file, update_file

PACKAGE = pkg_resources.require('tagedit')[0]


def main():
    """
    Command line script for TagEdit.
    """
    argparser = argparse.ArgumentParser(add_help=True)
    argparser.description = 'Simple tagging for media files'

    argparser.add_argument('FILE')
    argparser.add_argument('-u', '--updates-base64', action='store', help='Base64 encoded JSON string of updates to apply')
    argparser.add_argument(
        '-v', '--version',
        action='version', version='{}-{}'.format(
            PACKAGE.project_name,
            PACKAGE.version
        ),
        help='Show version number and exit.'
    )
    args = argparser.parse_args()
    
    # Attempt to open the file.
    res = open_file(args.FILE)
    if not res['success']:
        err = res['error']
        if res.get('err'): err = err + ': ' + str(res['err'])
        argparser.error(err)
    
    # Attempt to update the file.
    res = update_file(res['file'], args.updates_base64)
    if not res['success']:
        err = res['error']
        if res.get('err'): err = err + ': ' + str(res['err'])
        argparser.error(err)
    
    print('tagedit: file updated.')
