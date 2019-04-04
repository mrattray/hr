import pytest

from hr import cli

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_fails_without_arguments(parser):
    """
    Test errors with no arguments
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_succeeds_with_path_argument(parser):
    """
    Test success when path provided
    """
    args = parser.parse_args(["path/to/file"])
    assert args.path == "path/to/file"

def test_export_set_to_false(parser):
    """
    Test export set to false when no flag provided
    """
    args = parser.parse_args(["path/to/file"])
    assert args.export == False

def test_export_set_to_true(parser):
    """
    Test export set to true when flag provided
    """
    args = parser.parse_args(["--export", "path/to/file"])
    assert args.export == True


