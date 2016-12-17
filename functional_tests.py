from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Let's do a to-do list straight away
        # go to homepage
        self.browser.get('http://localhost:8000')

        # Notice, page title should inform that it is a to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # There is a place to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # Type "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        # After hitting enter, page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "new to-do item did not appear in table"
        )

        # There is a still a text box allowing to add a new item
        # Let's add "Use peacock feathers to make a fly"
        self.fail('Finish the tes!')
        # Page updates, and two items are on to-do list

        # Page generates unique url for use - there is some explaantory
        # text to that effect
        # After visiting url - user's to-do list is there

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
