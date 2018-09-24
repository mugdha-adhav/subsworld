import os
import zipfile
import requests
from subsworld.subsOpensubtitle import OpenSubtitles, getOpensubtitleSubs
from subsworld.subsSubscene import getSubsceneSubs
from subsworld.subsEnd import endSubStatus

def searchSubtitle(sub):
    print('\nPlease wait ... ')
    ost = OpenSubtitles()
    ost.login('subsworld', 'subsworld')
    count = 0
    FOpenSub = 0
    FSubscene = 0
    try:
        subscenceData = getSubsceneSubs(sub)
    except:
        Exception
    if subscenceData is not None:
        FSubscene = 1
    else:
        print('Error fetching subtitles from subscene... Trying another source')

    try:
        openSubsdata = getOpensubtitleSubs(sub)
    except:
        Exception
    if openSubsdata is not False:
        FOpenSub = 1
    else:
        print('Error fetching subtitles from opensubtitles... Trying another source')


    while count < len(openSubsdata) or count < len(subscenceData.subtitles) is 1:

        if count >= len(openSubsdata):
            FOpenSub = 0

        if count >= len(subscenceData.subtitles):
            FSubscene = 0
        
        if FSubscene is not 0:
            print('\nSearching in Subscene ... ')
            try:
                response = requests.get(subscenceData.subtitles[count].zipped_url)
            except:
                Exception
            fpath = os.path.join(sub.MDIR, "subzip")
            with open(fpath, 'wb') as f:
                f.write(response.content)

            zip_ref = zipfile.ZipFile(fpath, 'r')
            zip_ref.extractall(sub.MDIR)
            zip_ref.close()
            os.remove(fpath)
            endSubStatus(0)

        if FOpenSub is not 0:
            print('\nSearching in Opensubtitle ... ')
            try:
                ost.download_subtitles([openSubsdata[count].get('IDSubtitleFile')], sub.MNAME, sub.MDIR)
            except:
                Exception
            endSubStatus(0)

        count=count+1

    endSubStatus(2)

    return