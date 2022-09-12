
#! functional test 👉 frontend test
#! unit test 👉 backend test

from selenium import webdriver
from django.test import TestCase
from .forms import HashForm
import hashlib

#? browser = webdriver.Firefox()

# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')


""" class FunctionalTestCase(TestCase):
    # Before the test run
    # We want the browser become ready
    # The setUp is part of initialization, this method will get called before every test function which you are going to write in this test case class. Here you are creating the instance of Firefox WebDriver.
    def setUp(self):
        #self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome()

    # Between, write your test
    # Give a descriptive name
    # This is the test case method. The test case method should always start with characters test.
    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enter hash here',self.browser.page_source)
        #! Is this text 👆 available in browser?

    def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000')
        # Find the element with id "text"
        text = self.browser.find_element_by_id("id_text")
        # Simulate user types "hello"
        # send_keys method is used to send text to any field, such as input field of a form or even to anchor tag paragraph, etc. It replaces its contents on the webpage in your browser.
        text.send_keys("hello")
        # Simulate click to the submit button
        self.browser.find_element_by_name("submit").click()
        # Result must be the correct walue
        self.assertInHTML('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    # After the test run
    # The tearDown method will get called after every test method. This is a place to do all cleanup actions. In the current method, the browser window is closed. You can also call quit method instead of close. The quit will exit the entire browser, whereas close will close a tab, but if it is the only tab opened, by default most browser will exit entirely.
    def tearDown(self):
        self.browser.quit() """

class UnitTestCase(TestCase):

    def test_home_homepage_tempalte(self):
        response = self.client.get('/')
        #? The client 👆 is testing on scripts, not on the browser
        self.assertTemplateUsed(response, 'hashing/home.html')

    # There should be a form the user enters a text to
    # find corresponding hash
    def test_hash_form(self):
        #! Check if there is a form, needs to filled with some data, for not to be an empty form which basically equals to False
        form = HashForm(data={'text': 'hello'})
        # Check if it is valid
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self):
        # Need to import haslib library to generate hash
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        # hash.hexdigest() Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.
        # Info about hashlib: https://docs.python.org/3/library/hashlib.html
        # Check our result equals to the true one
        # Go to any of the website to generate hash
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)
        # No need to write extra code for that, because it checks the library of hashlib only.


