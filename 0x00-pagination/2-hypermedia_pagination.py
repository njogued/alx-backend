#!/usr/bin/env python3
"""Return a list of entries in dataset given page and page_size"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
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
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert (page > 0)
        assert (page_size > 0)
        try:
            indexes = index_range(page, page_size)
            return self.dataset()[indexes[0]:indexes[1]]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary of several k-v pairs"""
        data = self.get_page(page, page_size)
        if len(self.dataset()) % page_size == 0:
            total_pages = len(self.dataset()) // page_size
        else:
            total_pages = len(self.dataset()) // page_size + 1
        next_page = None if (page + 1) > total_pages else page + 1
        prev_page = None if page - 1 < 0 else page - 1
        page_info = {}
        page_info['page_size'] = page_size
        page_info['page'] = page
        page_info['data'] = data
        page_info['next_page'] = next_page
        page_info['prev_page'] = prev_page
        page_info['total_pages'] = total_pages
        return page_info
