import pytest

@pytest.fixture(autouse=True)
def isolated_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path
