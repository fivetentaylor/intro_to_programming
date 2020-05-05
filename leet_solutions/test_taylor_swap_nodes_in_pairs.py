import taylor_swap_nodes_in_pairs as swap


def test_swap():
    x = [1, 2, 3, 4, 5]
    assert swap.linked_to_list(swap.swap_pairs(swap.make_list(x))) == [2, 1, 4, 3, 5]

    x = [1, 2, 3, 4, 5, 6]
    assert swap.linked_to_list(swap.swap_pairs(swap.make_list(x))) == [2, 1, 4, 3, 6, 5]

    x = [1]
    assert swap.linked_to_list(swap.swap_pairs(swap.make_list(x))) == [1]

    x = []
    assert swap.linked_to_list(swap.swap_pairs(swap.make_list(x))) == []
