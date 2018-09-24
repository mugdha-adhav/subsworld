from subsworld.subsSearch import searchSubtitle

class subsInput:
    MLANG = '1'
    MPATH = '0'
    MNAME = '0'
    MDIR = '0'

    def subsEnter(self):
        self.MLANG = self.setSubsLang()
        self.MPATH = self.setMovName()
        self.MNAME = self.formatMovName()
        self.MDIR = self.getMovDir()
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
        while True:
            name = input('\nPlease enter movie/series name(with location): ')
            if name:
                return name

    def formatMovName(self):
        name = self.MPATH.rsplit('\\', 1)[1]

        return name.rsplit('.', 1)[0]

    def getMovDir(self):
        path = self.MPATH.rsplit('\\',1)
        return path[0]

def subsworld():
        sub = subsInput()

        sub.subsEnter()

        searchSubtitle(sub)

        subsworld()