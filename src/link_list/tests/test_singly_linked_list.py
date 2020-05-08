from ..singly_linked_list import SinglyLinkList


def test_prepend_in_empty_linked_list():
    linked_list = SinglyLinkList()
    assert len(linked_list) == 0

    linked_list.prepend('test')
    assert linked_list.head.value == 'test'
    assert linked_list.tail.value == 'test'
    assert len(linked_list) == 1


def test_prepend_in_non_empty_linked_list():
    pass
