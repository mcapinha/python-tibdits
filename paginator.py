from math import ceil,floor

class Paginator:

    def __init__(self,total_items, current_page , page_size, max_visible_pages ):
        self.total_items = total_items
        self.current_page = current_page
        self.page_size = page_size
        self.max_visible_pages = max_visible_pages

        total_pages = int( ceil( total_items / page_size ) )
        min_pages_before = int (  ceil( max_visible_pages / 2 ) )
        max_pages_after = max_visible_pages - min_pages_before

        self.first = 1
        self.last = total_pages
        self.next = min (self.current_page + 1  , self.last )
        self.previous = max(1, self.current_page - 1)

        ## No need to shorten page list, show all
        if total_pages <= max_visible_pages:
            self.list = list(range(1,(total_pages+1)))
            return

        ## Pad with more pages to the right
        if current_page <= min_pages_before:
            start_page = 1
            self.list = list(range(start_page,start_page+max_visible_pages))
            return

        if (total_pages - current_page ) < max_pages_after:
            self.list = list(range( total_pages - max_visible_pages , total_pages  ))
            return

        self.list = list(range(current_page - min_pages_before , current_page + max_pages_after ))
        return

