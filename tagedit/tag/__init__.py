# tagedit <https://github.com/msikma/tagedit>
# © MIT license

"""
Module for running MediaFile to edit tags.
"""
import sys
import base64
import mediafile
import json


def read_cover(path):
    """
    Returns the cover image in bytes.
    """
    in_file = open(path, 'rb')
    data = in_file.read()
    in_file.close()
    return data



def open_file(path):
    """
    Opens a given file. Returns an error if the current file type is not supported.
    """
    try:
        file = mediafile.MediaFile(path)
        return { 'success': True, 'file': file }
    except mediafile.UnreadableFileError:
        return { 'error': 'the given file could not be read', 'success': False }
    except mediafile.FileTypeError:
        return { 'error': 'the given file could not be read', 'success': False }
    except mediafile.MutagenError as err:
        return { 'error': 'an internal error occurred', 'success': False, 'err': err }
    except:
        err = sys.exc_info()[1]
        return { 'error': 'an error occurred', 'success': False, 'err': err }


def update_file(file_object, updates):
    """
    Updates a file with a new set of tags.
    """
    try:
        decoded = base64.b64decode(updates).decode('utf-8')
        data = json.loads(decoded)
        if data['art']:
            data['art'] = read_cover(data['art'])
        file_object.update(data)
        file_object.save()
        return { 'success': True }
    except json.decoder.JSONDecodeError as err:
        return { 'error': 'the given updates are not valid JSON', 'success': False, 'err': err }
    except:
        err = sys.exc_info()[1]
        return { 'error': 'an error occurred', 'success': False, 'err': err }
