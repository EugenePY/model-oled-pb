from click.testing import CliRunner
from keymake.__main__ import oled_utils

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(oled_utils, ['tests/data/'])
  assert result.exit_code == 0

def test_resize_gif():
    ...

def test_resize_png():
    ...
