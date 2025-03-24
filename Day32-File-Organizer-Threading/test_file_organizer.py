import unittest
import file_organizer


class TestFileOrganizer(unittest.TestCase):
    def test_check_type_valid(self):
        name, ext = file_organizer.check_type("book.pdf")
        self.assertEqual(name, "book")
        self.assertEqual(ext, "pdf")

    def test_find_matching_folder_image(self):
        self.assertEqual(file_organizer.find_matching_folder("jpg"), "Images")
        self.assertEqual(file_organizer.find_matching_folder("png"), "Images")

    def test_find_matching_folder_documents(self):
        self.assertEqual(file_organizer.find_matching_folder("pdf"), "Documents")
        self.assertEqual(file_organizer.find_matching_folder("docx"), "Documents")

    def test_find_matching_folder_videos(self):
        self.assertEqual(file_organizer.find_matching_folder("mp4"), "Videos")
        self.assertEqual(file_organizer.find_matching_folder("mov"), "Videos")

    def test_find_matching_folder_unknown(self):
        self.assertEqual(file_organizer.find_matching_folder("exe"), "Others")
    




if __name__ == "__main__":
    unittest.main()