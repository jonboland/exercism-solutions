from typing import Iterator, List


BOOK_COST = 800
DISCOUNTS = (1, .95, .9, .8, .75)
PRICES = {
    size: BOOK_COST * discount * size
    for size, discount in zip(range(1, 6), DISCOUNTS)
}


def total(basket: List[int]) -> float:
    """
    Calculates the lowest price of a shopping
    basket containing books from the same series.
    """
    if (basket_size := len(basket)) == 1:
        return BOOK_COST
    book_group_sizes = configure(basket)
    if basket_size < 8:
        return cheapest_deal(book_group_sizes)
    replaced_sizes = replace(book_group_sizes)
    return cheapest_deal(replaced_sizes)


def configure(basket: List[int]) -> Iterator[int]:
    """
    Configures basket into groups of unique books,
    and yields the book group sizes.
    """
    basket_copy = basket[:]
    while book_group := set(basket_copy):
        yield len(book_group)
        for book in book_group:
            basket_copy.remove(book)


def replace(sizes: Iterator[int]) -> Iterator[int]:
    """
    Replaces groups of three and five with
    two groups of four, which is cheaper.
    """
    size_list = list(sizes)
    while {3, 5}.issubset(size_list):
        size_list.remove(3)
        size_list.remove(5)
        yield from (4, 4)
    yield from size_list


def cheapest_deal(sizes: Iterator[int]) -> float:
    """Returns the cost of the cheapest deal."""
    return sum(PRICES[size] for size in sizes)
