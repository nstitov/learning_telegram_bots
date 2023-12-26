import os
import sys
from pathlib import Path

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int = PAGE_SIZE) -> tuple[str, int]:
    P_SIGNS = ',.!:;?'
    if len(text) < start + page_size:
        s = text[start:]
    else:
        s = text[start: start + page_size]

        if s[-1] in P_SIGNS:
            if text[len(s)] in P_SIGNS:
                while s[-1] in P_SIGNS:
                    s = s[:-1]
        while s[-1] not in P_SIGNS:
            s = s[:-1]
            if len(s) == 0:
                break
    return s, len(s)


def prepare_book(path: Path) -> None:
    with open(path, 'r', encoding='utf-8') as book_file:
        text = book_file.read()

    page_start, page_num = 0, 0
    while page_start < len(text):
        page, page_len = _get_part_text(text, page_start, PAGE_SIZE)
        page_start += page_len
        page_num += 1

        book[page_num] = page.lstrip()


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))