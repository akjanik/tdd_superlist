from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Let's do a to-do list straight away
        # go to homepage
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is a still a text box allowing to add a new item
        # Let's add "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # Page updates, and two items are on to-do list
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Page generates unique url for use - there is some explaantory
        # text to that effect
        # After visiting url - user's to-do list is there
        self.fail('Finish the test!')
        # browser.quit()
