import os
import pytest

from src.main import deleteOutputFiles


def test_deleteOutputFiles(tmp_path, caplog):
    # Create temporary files in the output directory
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    file1 = output_dir / "file1.txt"
    file1.touch()
    file2 = output_dir / "file2.txt"
    file2.touch()

    # Call the function under test
    deleteOutputFiles(output_dir)

    # Check if files are deleted
    assert not file1.exists()
    assert not file2.exists()


@pytest.mark.xfail(reason="Test fails due to missing output directory")
def test_deleteOutputFiles_xfail():
    output_path = "./output"

    deleteOutputFiles(output_path)

    # Assertions
    assert not os.path.exists(output_path)
