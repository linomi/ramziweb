from logging import raiseExceptions
from scholarly import scholarly
class Gscholar(): 
    def __init__(self,author_query:str):
        self.authors = scholarly.search_author(author_query)
    def __next__(self):
        return_list = []
        for i in range(10): 
            try: 
                return_list.append(next(self.authors))
            except: 
                break 
        return return_list
    def set_author(self,author:dict): 
        self.author = author 
    def get_publications(self,pubcount:int):
        try:
            fill_author = scholarly.fill(self.author,sections=['publications'],sortby='year',publication_limit=10)
        except: 
            raise ValueError('set author first')
        publications = fill_author['publications']
        
    