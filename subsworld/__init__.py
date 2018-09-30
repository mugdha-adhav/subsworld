from subsworld.subsSearch import searchSubtitle

class subsInput:
    MLANG = '1'
    MPATH = '0'
    MNAME = '0'
    MDIR = '0'

    def subsEnter(self):
        self.MPATH = self.setMovName()
        self.MNAME = self.formatMovName()
        self.MDIR = self.getMovDir()
        self.MLANG = self.setSubsLang()
        return

    def setSubsLang(self):
        print('\nPlease select your language')
        print('\t1. English')
        print('\t2. French')
        print('\t3. Arabic')
        option = input('Enter option(1-3): ')
        if option == '1':
            return '1'
        elif option == '2':
            return '2'
        elif option == '3':
            return '3'
        else:
            print('\nInvalid option... Try again')
            return self.setSubsLang()

    def setMovName(self):
        name = input('\nPlease enter exact movie/series path: ')
        if name is None or ('/' not in name and '\\' not in name):
            print('\nInvalid movie path... Please try again...')
            name = self.setMovName()
        return name

    def formatMovName(self):
        try:
            name = self.MPATH.rsplit('\\', 1)[1]
            if name is None:
                name = self.MPATH.rsplit('/', 1)[1]
            return name.rsplit('.', 1)[0]
        except:
            print('\nInvalid movie path... Please try again...')
            self.subsEnter()

    def getMovDir(self):
        path = self.MPATH.rsplit('\\',1)
        if path is None:
            path = self.MPATH.rsplit('/', 1)
        return path[0]

def subsworld():
        sub = subsInput()

        sub.subsEnter()

        searchSubtitle(sub)

        subsworld()