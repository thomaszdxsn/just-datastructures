from ..singly_linked_list import SinglyLinkList


def test_prepend_in_empty_linked_list():
    linked_list = SinglyLinkList()
    assert len(linked_list) == 0

    linked_list.prepend('test')
    assert linked_list.head == 'test'
    assert linked_list.tail == 'test'
    assert len(linked_list) == 1


def test_prepend_in_non_empty_linked_list():
    linked_list = SinglyLinkList([1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.head == 1

    linked_list.prepend(0)
    assert len(linked_list) == 4
    assert linked_list.head == 0
    assert list(linked_list) == [0, 1, 2, 3]


def test_append_in_empty_linked_list():
    linked_list = SinglyLinkList()
    assert len(linked_list) == 0

    linked_list.append('test')
    assert linked_list.head == 'test'
    assert linked_list.tail == 'test'
    assert len(linked_list) == 1


def test_append_in_non_empty_linked_list():
    linked_list = SinglyLinkList([1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.tail == 3

    linked_list.append(4)
    assert linked_list.tail == 4
    assert list(linked_list) == [1, 2, 3, 4]


def test_extend_in_empty_linked_list():
    linked_list = SinglyLinkList()
    assert len(linked_list) == 0

    linked_list.extend([1, 2, 3])
    assert len(linked_list) == 3
    assert list(linked_list) == [1, 2, 3]


def test_extend_in_non_empty_linked_list():
    linked_list = SinglyLinkList([1, 2, 3])
    assert len(linked_list) == 3

    linked_list.extend([4, 5, 6])
    assert len(linked_list) == 6
    assert list(linked_list) == [1, 2, 3, 4, 5, 6]
