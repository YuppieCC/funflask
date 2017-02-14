from selenium import webdriver

class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        # start the Chrome
        try:
            cls.client = webdriver.Chrome()
        except:
            pass
        # if start failed, then skip the test.
        if cls.client:
            # create the app
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # No log
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel('ERROR')

            # create db
            db.create_all()
            Role.insert_roles()
            User.generate_fake(10)
            Post.generate_fake(10)

            # add admin
            admin_role = Role.query.filter_by(permissions=0xff)
            admin = User(email='sam@test.com',
                        username='sam', password='test',
                        role=admin_role, confirmed=True)
            db.session.add(admin)
            db.session.commit()

            # start the server
            threading.Thread(target=cls.app.run).start()

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # shutdown server and browser
            clls.client.get('http://localhost:5000/shutdown')
            cls.client.close()

            # drop the db
            db.drop_all()
            db.session.remove()

            # delete the context
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not avaliable')

    def teadDown(self):
        pass

    def test_admin_home_page(self):
        # index
        self.client.get('http://localhost:5000/')
        self.assertTrue(re.search('Hello, \s+Stranger!', self.client.page_source))

        # Login page
        self.client.find_element_by_link_text('LogIn').click()
        self.assertTrue('<h1>LogIn</h1>' in self.client.page_source)

        # login
        self.client.find_element_by_name('email').\
            send_keys('sam@test.com')
        self.client.find_element_by_name('password').send_keys('test')
        self.client.find_element_by_name('submit').click()
        self.assertTrue(re.search('Hello, \s+Sam', self.client.page_source))

        # Profile
        self.client.find_element_by_link_text('Profile').click()
        self.assertTrue('<h1>Sam</h1>' in self.client.page_source)


