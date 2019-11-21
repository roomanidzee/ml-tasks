from pathlib import Path

import pytest


@pytest.fixture
def file_path():
    file_path = Path(
        __file__
    ).parent.parent.parent.parent / Path('resources', 'bayes_data.csv')

    return str(file_path)
