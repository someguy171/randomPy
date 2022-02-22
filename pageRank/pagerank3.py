# PageRank(A) = (1 - damping) + daming(PageRank(N)/OutLink(N)...)

# dictionary to store all pages
pageList = {}

# adjacency matrix
adj = []

# damping factor
d = 0.85

class Page:
    def __init__(self, name):
        """Initialise a new page.

        Args:
            name (string): The name of the page.
        """
        self.name = name
        self.pageRank = 1
        self.position = len(pageList)
        self.links = []
        self.linkCount = 0
    
    
    def link(self, connectionName):
        """Create an outbound link from the current page to another.

        Args:
            connectionName (string): The name of the link's destination.
        """
        self.links.append(connectionName)
    
    
    def countLinks(self):
        for x in adj[self.position]:
            if x == 1: self.linkCount += 1
        
    
def addPage(name):
    """Create a new page.

    Args:
        name (string): The name of the page.
    """
    pageList[name] = Page(name)
    adj.append([])
    
    for row in range(len(adj)):
        while len(adj[row]) <= len(pageList):
            adj[row].append(0)
    
    print(adj)
    print("\n\n\n")
        


def createLink(origin, dest):
    """Create a link between one page and another.

    Args:
        origin (string): The name of the page with the link.
        dest (string): The name of the page which the link goes to.
    """
    pageList[origin].link(dest)


def calcPR(pageName):
    # PageRank(A) = (1 - damping) + daming(PageRank(N)/OutLink(N) + ...)
    
    mainB = 0
    for pageName in pageList:
        page = pageList[pageName]
        for targetName in pageList:
            if targetName in page.links:
                target = pageList[targetName]
                mainB += (target.pageRank / target.linkCount)
    
    page.pageRank = (1 - d) + d * mainB

# column = inbound
# row = outbound
def finishSetup():
    for pageName in pageList:
        page = pageList[pageName]
        for connection in page.links:
            dest = pageList[connection]
            adj[page.position][dest.position] = 1
    
    for pageName in pageList:
        page = pageList[pageName]
        page.countLinks()
        print(pageName, "has links to", page.links)
        print(pageName, "has", page.linkCount, "links.\n")
    
    for x in range(len(pageList)):
        for i in pageList:
            calcPR(pageList[i])
    
    for x in pageList:
        print(x, "=", pageList[x].pageRank)
    

addPage("A")
addPage("B")
addPage("C")
addPage("D")

createLink("A", "B")
createLink("A", "C")
createLink("A", "D")
createLink("B", "C")
createLink("B", "D")
createLink("D", "C")

finishSetup()
    
