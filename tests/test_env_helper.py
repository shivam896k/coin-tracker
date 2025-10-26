import os

from utils.env_helper import load_env


def test_load_env_creates_env_vars(tmp_path, monkeypatch):
    env_file = tmp_path / ".env.sample"
    env_file.write_text("FOO=bar\n#comment\nBAZ=qux")
    monkeypatch.chdir(tmp_path)

    load_env()

    assert os.environ.get('FOO') == 'bar'
    assert os.environ.get('BAZ') == 'qux'
