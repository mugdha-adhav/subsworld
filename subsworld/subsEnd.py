def endSubStatus(val):
    if val == 0:
        print('\nSubtitle Downloaded Successfully... ')
        if not input('\nPlease press enter to keep searching the same or press any other key to search other substitle: '):
            return
        else:
            from subsworld import subsworld
            subsworld()

    elif val == 1:
        print('\nUnknown Error Occured... ')
        return

    elif val == 2:
        print('\nSubtitles not found... ')
        if not input('\nPlease press enter to exit or press any other key to search other substitle: '):
            print('Thanks for using subsworld ... ')
            exit(0)
        else:
            return