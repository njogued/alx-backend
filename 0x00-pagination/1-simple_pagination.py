import csv
import math
from typing import List
from typing import Tuple



def index_range(self, page: int, page_size: int) -> Tuple:
    """Create and return a tuple of indexes"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the list of entries of the appropriately paginated dataset"""
        try:
            assert (page > 0 or page_size > 0)
            assert isinstance(page, int)
            assert isinstance(page_size, int)
            indexes = index_range(page, page_size)
            return self.dataset()[indexes[0]:indexes[1]]
        except Exception:
            return []
