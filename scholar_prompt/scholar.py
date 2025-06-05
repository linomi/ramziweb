from logging import raiseExceptions
from scholarly import scholarly,ProxyGenerator

pg = ProxyGenerator()
success = pg.FreeProxies()

scholarly.use_proxy(pg)

class Gscholar(): 
    def __init__(self,author_query:str):
        self.authors = scholarly.search_author(author_query)
    def get(self):

        return list(self.authors)
    def set_author(self,author:dict): 
        self.author = author 
    def get_publications(self,pubcount:int):
        try:
            fill_author = scholarly.fill(self.author,sections=['publications'],sortby='year',publication_limit=10)
        except: 
            raise ValueError('set author first')
        return fill_author['publications']

        
    