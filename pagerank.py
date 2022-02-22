pageList = []
d = 0.85

class Page:
    def __init__(self, name, outLink, pageLink):
        self.name = name
        self.pageRank = 1
        self.outLink = outLink
        self.pageLink = pageLink

        pageList.append(self.name)


pages = {
    "Page A": 0,
    "Page B": 0,
    "Page C": 0,
    "Page D": 0
}

def newPage(name, outLink, pageLink):
    pages[name].append(Page(name, outLink, pageLink))


def pageRankCalc(pageName):
    for original in pageList:
        if original == pageName:
            tempPageList = pageList.remove(pageName)
            mainB = 0
            for target in tempPageList:
                if target in pages[original].pageLink:
                    mainB += (pages[target].pageRank / pages[target].outLink)

            return (1-d) + d * mainB


def startCalc():
    for x in range(len(pageList) * 3):
        for page in pages:
            page.pageRank = pageRankCalc(page)

    for x in pageList:
        print(x + ": " + pages[x].pageRank)


def full():
    newPage("Page A", 1, ["Page B", "Page C"])
    newPage("Page B", 2, ["Page A"])
    newPage("Page C", 1, ["Page B", "Page D"])
    newPage("Page D", 1, [])

    startCalc()

full()