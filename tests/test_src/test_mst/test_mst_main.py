from src.mst.main import connect_structures, remove_longest_link


def test_connection(prepared_structures):
    connected_links = connect_structures(prepared_structures, len(prepared_structures))

    assert len(connected_links) == 10


def test_clear_links(prepared_structures):
    connected_links = connect_structures(prepared_structures, len(prepared_structures))
    final_links = remove_longest_link(prepared_structures, connected_links)

    assert len(final_links) == 9
