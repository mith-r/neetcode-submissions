class Page:
    def __init__(self, page: str):
        self.page = page
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        

    def visit(self, url: str) -> None:
        newSite = Page(url)
        newSite.prev = self.homepage
        self.homepage.next = newSite
        self.homepage = newSite
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.homepage.prev:
            self.homepage = self.homepage.prev
            steps -= 1
        return self.homepage.page

        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.homepage.next:
            self.homepage = self.homepage.next
            steps -= 1
        return self.homepage.page

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)