import unittest
import selenium
from selenium import webdriver

class TestBlogValidity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/catzheng/Coding/chromedriver')

    def test_blog_posts(self):
        driver = self.driver
        driver.get("https://catzheng22.github.io/blog/")
        self.assertIn("Catherine Zheng", driver.title)
        # blog_window = driver.window_handles[0]
        # titles = [ post.text for post in driver.find_elements_by_class_name("post-link") ]
        links = [ post.get_attribute('href') for post in driver.find_elements_by_class_name("post-link") ]
        
        for link in links:
            driver.execute_script("window.open('{}', 'new window')".format(link))
            link_window = driver.window_handles[1]
            driver.switch_to.window(link_window)
            title = driver.find_element_by_xpath("//h1[1]")
            if title.text == "404":
                print("404 not found: blog post link was invalid")
                return 1
            print(title.text)

        # test 404
        # driver.execute_script("window.open('http://localhost:4000/bleh/', 'new window')")
        # title = driver.find_element_by_xpath("//h1[1]")
        # if title.text == "404":
        #     print("404 not found: blog post link was invalid")
        #     return 1

if __name__ == "__main__":
    unittest.main()