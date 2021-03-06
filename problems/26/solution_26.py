def coding_problem_26(not_a_linked_list, k):
    """
    Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be
    smaller than the length of the list. The list is very long, so making more than one pass is prohibitively expensive.
    Do this in constant space and in one pass.

    >>> coding_problem_26(range(10), 3)
    [0, 1, 2, 3, 4, 5, 6, 7, 9]

    Note: not using a linked list out of convenience, but moving through it with iterators which do have a similar
    usage patterns.

    Note2: what I coded below was my first and only solution. However, using two pointers/indexes/iterators equates to
    two passes in my book. I checked on Google, and all the solutions are equivalent to this. The alternative, a
    k-buffer of the stream, would not be constant space. If you're reading this and have better ideas, let me know!
    """
    iter_to_the_end = iter(not_a_linked_list)
    for _ in range(k):
        next(iter_to_the_end)  # k is guaranteed < len(list)

    result = []
    iter_lagging_behind = iter(not_a_linked_list)
    while True:
        result.append(next(iter_lagging_behind))
        try:
            next(iter_to_the_end)
        except StopIteration:
            break

    next(iter_lagging_behind)  # gobble an element
    result.extend(iter_lagging_behind)
    return result


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
