from selenium import webdriver
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
        self.fail('Finish the test!')

        # Type "buy peacock feathers" into a text box
        # After hitting enter, page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is a still a text box allowing to add a new item
        # Let's add "Use peacock feathers to make a fly"

        # Page updates, and two items are on to-do list

        # Page generates unique url for use - there is some explaantory
        # text to that effect
        # After visiting url - user's to-do list is there

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
