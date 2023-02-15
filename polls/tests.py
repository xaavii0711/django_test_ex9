from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from django.conf import settings

    
class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json',]
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.headless = settings.HEADLESS_TESTS
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
    
    @classmethod
    def tearDownClass(cls):
        # no sortim el browser per comprovar visualment com ha anat
        #cls.selenium.quit()
        super().tearDownClass()
    
    # def test_login(self):
    #     self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
    #     username_input = self.selenium.find_element(By.NAME,"username")
    #     username_input.send_keys('xmartinez')
    #     password_input = self.selenium.find_element(By.NAME,"password")
    #     password_input.send_keys('Superlocal123')
    #     self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

    #     # self.selenium.find_element(By.XPATH,'//a[@href="/admin/auth/user/]').click()

    #     self.selenium.find_element(By.XPATH,'//a[text()="Users"]').click()
    #     self.selenium.find_element(By.XPATH,"//a[contains(text(),'Add user')]").click()

    #     username_input2 = self.selenium.find_element(By.NAME,"username")
    #     username_input2.send_keys('ex9')

    #     password_input2 = self.selenium.find_element(By.NAME,"password1")
    #     password_input2.send_keys('Superlocal123')

    #     password_input3 = self.selenium.find_element(By.NAME,"password2")
    #     password_input3.send_keys('Superlocal123')

    #     self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

    #     self.selenium.find_element(By.XPATH,'//input[@id="id_is_staff"]').click()

    #     self.selenium.find_element(By.XPATH,'//option[@title="auth | user | Can view user"]').click()

    #     self.selenium.find_element(By.XPATH,'//a[@id="id_user_permissions_add_link"]').click()

    #     self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

    #     self.selenium.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()

    #     self.selenium.find_element(By.XPATH,"//a[contains(text(),'Log in again')]").click()

    #     username_input4 = self.selenium.find_element(By.NAME,"username")
    #     username_input4.send_keys('ex9')

    #     password_input = self.selenium.find_element(By.NAME,"password")
    #     password_input.send_keys('Superlocal123')

    #     self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

    #     self.selenium.find_element(By.XPATH,"//a[contains(text(),'Users')]").click()
    
    #     try:
    #         self.selenium.find_element(By.XPATH,"//a[contains(text(),'Add user')]")
    #         assert False, "Trobat element que NO hi ha de ser"
    #     except NoSuchElementException:
    #         pass

    #     self.selenium.find_element(By.XPATH,"//a[contains(text(),'xmartinez')]").click()

    #     try:
    #         self.selenium.find_element(By.XPATH,"//a[text()='Delete']")
    #         assert False, "Trobat element que NO hi ha de ser"
    #     except NoSuchElementException:
    #         pass

class MySeleniumTests2(StaticLiveServerTestCase):
    fixtures = ['testdb.json',]
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.headless = settings.HEADLESS_TESTS
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
    
    @classmethod
    def tearDownClass(cls):
        # no sortim el browser per comprovar visualment com ha anat
        #cls.selenium.quit()
        super().tearDownClass()
    
    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('xmartinez')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('Superlocal123')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
        self.selenium.find_element(By.XPATH,'//a[@href="/admin/auth/user/"]').click()
        self.selenium.find_element(By.XPATH,"//a[contains(text(),'Add user')]").click()

        username_input2 = self.selenium.find_element(By.NAME,"username")
        username_input2.send_keys('ex16')

        password_input2 = self.selenium.find_element(By.NAME,"password1")
        password_input2.send_keys('Superlocal123')

        password_input3 = self.selenium.find_element(By.NAME,"password2")
        password_input3.send_keys('Superlocal123')

        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,'//input[@id="id_is_staff"]').click()

        self.selenium.find_element(By.XPATH,'//option[@title="auth | user | Can view user"]').click()

        self.selenium.find_element(By.XPATH,'//a[@id="id_user_permissions_add_link"]').click()

        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,"//a[contains(text(),'Add user')]").click()

        username_input2 = self.selenium.find_element(By.NAME,"username")
        username_input2.send_keys('prova1')

        password_input2 = self.selenium.find_element(By.NAME,"password1")
        password_input2.send_keys('Superlocal123')

        password_input3 = self.selenium.find_element(By.NAME,"password2")
        password_input3.send_keys('Superlocal123')
        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,'//input[@id="id_is_superuser"]').click()

        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,"//a[contains(text(),'Add user')]").click()

        username_input2 = self.selenium.find_element(By.NAME,"username")
        username_input2.send_keys('prova2')

        password_input2 = self.selenium.find_element(By.NAME,"password1")
        password_input2.send_keys('Superlocal123')

        password_input3 = self.selenium.find_element(By.NAME,"password2")
        password_input3.send_keys('Superlocal123')
        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,'//input[@id="id_is_superuser"]').click()

        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,"//a[contains(text(),'Add user')]").click()

        username_input2 = self.selenium.find_element(By.NAME,"username")
        username_input2.send_keys('prova3')

        password_input2 = self.selenium.find_element(By.NAME,"password1")
        password_input2.send_keys('Superlocal123')

        password_input3 = self.selenium.find_element(By.NAME,"password2")
        password_input3.send_keys('Superlocal123')
        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,'//input[@id="id_is_superuser"]').click()

        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        self.selenium.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()

        self.selenium.find_element(By.XPATH,"//a[contains(text(),'Log in again')]").click()

        username_input4 = self.selenium.find_element(By.NAME,"username")
        username_input4.send_keys('ex16')

        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('Superlocal123')

        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

        self.selenium.find_element(By.XPATH,'//a[@href="/admin/auth/user/"]').click()

        self.selenium.find_element(By.XPATH,"//a[text()='prova1']").click()

        try:
            self.selenium.find_element(By.XPATH,"//input[@value='Save and add another']")
            assert False, "Trobat element que NO hi ha de ser"
        except NoSuchElementException:
            pass

