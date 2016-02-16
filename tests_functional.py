from selenium import webdriver
import unittest


class SearchYayaTest(unittest.TestCase):

    """
    Test to check if user can search for a yaya
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def runTest(self):
        # User wants to check the listings for available yayas
        self.browser.get('http://localhost:8000')

        # User checks the page title and notices it says "GrabYaya"
        self.assertIn('GrabYaya', self.browser.title)
        self.fail('Finish the test!')

        # User sees a list of yayas

        # User searches for yayas between ages 18-25

        # The page shows yayas between ages 18-25

if __name__ == '__main__':
    unittest.main()
