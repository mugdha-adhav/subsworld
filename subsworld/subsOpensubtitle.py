import base64
import struct
import zlib
import os,re,io
import os.path
from xmlrpc.client import ServerProxy, Transport
import random

class Settings(object):
    OPENSUBTITLES_SERVER = 'http://api.opensubtitles.org/xml-rpc'
    USER_AGENT = 'TemporaryUserAgent'
    LANGUAGE = 'en'

class OpenSubtitles(object):

    def __init__(self, language=None, user_agent=None):
        self.language = language or Settings.LANGUAGE
        self.token = None
        self.user_agent = user_agent or os.getenv('OS_USER_AGENT') or Settings.USER_AGENT

        transport = Transport()
        transport.user_agent = self.user_agent

        self.xmlrpc = ServerProxy(Settings.OPENSUBTITLES_SERVER,
                                  allow_none=True, transport=transport)

    def _get_from_data_or_none(self, key):
        status = self.data.get('status').split()[0]
        return self.data.get(key) if '200' == status else None

    def login(self, username, password):
        self.data = self.xmlrpc.LogIn(username, password,
                                      self.language, self.user_agent)
        token = self._get_from_data_or_none('token')
        if token:
            self.token = token
        return token

    def logout(self):
        data = self.xmlrpc.LogOut(self.token)
        return '200' in data.get('status')

    def search_subtitles(self, params):
        self.data = self.xmlrpc.SearchSubtitles(self.token, params)
        return self._get_from_data_or_none('data')

    def download_subtitles(self, ids, filename,
                           output_directory, extension='srt'):
        self.data = self.xmlrpc.DownloadSubtitles(self.token, ids)
        encoded_data = self._get_from_data_or_none('data')
        if not encoded_data:
            return
        try:
            decoded_data = base64.b64decode(encoded_data[0].get('data'))
            decoded_data = base64.b64decode(encoded_data[0].get('data'))
            decoded_data = zlib.decompress(decoded_data, 16+zlib.MAX_WBITS)
            decoded_data = decoded_data.decode('utf-8')
        except:
            return
        if not decoded_data:
            return
        else:
            filename = filename.rsplit('.',1)[0] + str(random.randint(1,10000)) + '.srt'
            fpath = os.path.join(output_directory, filename)
            try:
                with io.open(fpath, 'w', encoding='utf-8') as f:
                    f.write(decoded_data)
            except Exception:
                pass
        return

def getOpensubtitleSubs(subData):
    ost = OpenSubtitles()
    token = ost.login('mugdhaadhav', 'yui4avii')
    if token is None:
        print('\n\nInvalid credentials for OpenSubtitle...')
        return False
    else:
        langFile = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"languages.txt"), "r")
        for l in langFile:
            if re.match(subData.MLANG+' ', l):
                mLanguage = l.split(' ')[2]
        langFile.close()
        file = File(subData.MPATH)
        hash = file.get_hash()
        size = file.size
        data = ost.search_subtitles([{'sublanguageid': mLanguage, 'moviehash': hash, 'moviebytesize': size}])
        return data


class File(object):
    def __init__(self, path):
        self.path = path
        self.size = str(os.path.getsize(path))

    def get_hash(self):
        longlongformat = 'q'  # long long
        bytesize = struct.calcsize(longlongformat)

        try:
            f = open(self.path, "rb")
        except(IOError):
            return "IOError"

        hash = int(self.size)

        if int(self.size) < 65536 * 2:
            return "SizeError"

        for x in range(65536 // bytesize):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF  # to remain as 64bit number

        f.seek(max(0, int(self.size) - 65536), 0)
        for x in range(65536 // bytesize):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

        f.close()
        returnedhash = "%016x" % hash
        return str(returnedhash)


