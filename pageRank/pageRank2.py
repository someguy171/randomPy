pageList = []
d = 0.85

class Page:
    def __init__(self, name):
        self.name = name
        self.pageRank = 1
        self.pageListDict = {}

        pageList.append(self.name)


pages = {}

def newPage(name):
    pages[name].append(Page(name))


def pageRankCalc(pageName):
    for check in pageList:
        if check == pageName:
            tempPageList = pageList.remove(pageName)
            mainB = 0
            for targetPage in tempPageList:
                mainB += (pages[targetPage].pageRank / check.pageListDict[targetPage])

            return (1-d) + d * mainB


def startCalc():
    for page in pages:
        page.pageListDict[input(page.name, "Inbound page: ")].append(int("How many outbound links on that page: "))

    for x in range(len(pageList) * 3):
        for page in pages:
            page.pageRank = pageRankCalc(page)

    for x in pageList:
        print(x + ": " + pages[x].pageRank)

newPage("Page A")
pages["Page A"].pageListDict["Page B"]
