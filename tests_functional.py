from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.browser.get('http://localhost:8000/amos')

        # User checks the page title and notices it says "GrabYaya"
        self.assertIn('GrabYaya', self.browser.title)

        # User sees a list of yayas
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Yayas For Hire', header_text)

        # User searches for yayas with name "John Doe"
        searchbox = self.browser.find_element_by_id('searchbox')
        self.assertEqual(searchbox.get_attribute('placeholder'), 'Search')
        searchbox.send_keys('John Doe')
        searchbox.send_keys(Keys.ENTER)

        # The page shows yayas with name "John Doe"
        table = self.browser.find_element_by_class('table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == 'John Doe' for row in rows))

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
