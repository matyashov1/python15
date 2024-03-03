import os
import unittest
from your_script import get_file_info, FileInfo

class TestGetFileInfo(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir, exist_ok=True)
        open(os.path.join(self.test_dir, "file1.txt"), "w").close()
        open(os.path.join(self.test_dir, "file2.docx"), "w").close()
        os.makedirs(os.path.join(self.test_dir, "subdir"), exist_ok=True)
        open(os.path.join(self.test_dir, "subdir", "file3.pdf"), "w").close()

    def tearDown(self):
        os.system("rm -rf {}".format(self.test_dir))

    def test_get_file_info(self):
        expected = [
            FileInfo(name="file1", extension=".txt", is_dir=False, parent="test_directory"),
            FileInfo(name="file2", extension=".docx", is_dir=False, parent="test_directory"),
            FileInfo(name="subdir", extension=None, is_dir=True, parent="test_directory")
        ]
        result = get_file_info(self.test_dir)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
