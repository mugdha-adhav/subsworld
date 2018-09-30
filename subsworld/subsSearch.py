import os
import zipfile
import requests
from subsworld.subsOpensubtitle import OpenSubtitles, getOpensubtitleSubs
from subsworld.subsSubscene import getSubsceneSubs
from subsworld.subsEnd import endSubStatus

def searchSubtitle(sub):
    print('\nPlease wait ... ')
    count = 0
    FOpenSub = 0
    FSubscene = 0
    try:
        subscenceData = getSubsceneSubs(sub)
        if subscenceData is not None:
            FSubscene = 1
        else:
            print('Error fetching subtitles from subscene... Trying another source')
    except Exception:
        print('Error fetching subtitles from subscene... Trying another source')

    try:
        ost = OpenSubtitles()
        ost.login('subsworld', 'subsworld')
        openSubsdata = getOpensubtitleSubs(sub)
        if openSubsdata is not False:
            FOpenSub = 1
        else:
            print('Error fetching subtitles from opensubtitles... Trying another source')
    except Exception:
        print('Error fetching subtitles from opensubtitles... Trying another source')

    while FOpenSub != 0 or FSubscene !=0:
        if FSubscene is not 0:
            print('\nSearching in Subscene ... ')
            try:
                response = requests.get(subscenceData.subtitles[count].zipped_url)
                fpath = os.path.join(sub.MDIR, "subzip")
                with open(fpath, 'wb') as f:
                    f.write(response.content)
                zip_ref = zipfile.ZipFile(fpath, 'r')
                zip_ref.extractall(sub.MDIR)
                zip_ref.close()
                os.remove(fpath)
                endSubStatus(0)
            except Exception:
                print('Error fetching subtitles from subscene... Trying another source')

        if FOpenSub is not 0:
            print('\nSearching in Opensubtitle ... ')
            try:
                ost.download_subtitles([openSubsdata[count].get('IDSubtitleFile')], sub.MNAME, sub.MDIR)
                endSubStatus(0)
            except Exception as e:
                print('Fuck off Error fetching subtitles from opensubtitles... Trying another source')

        count=count+1
        if FOpenSub == 1 and count >= len(openSubsdata):
            FOpenSub = 0
        if FSubscene == 1 and count >= len(subscenceData.subtitles):
            FSubscene = 0

    endSubStatus(2)

    return