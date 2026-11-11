from selenium import webdriver

import data
import helpers
import pages
from helpers import retrieve_phone_code


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        assert (page.get_address_from(), page.get_address_to()) == (data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_supportive_plan()
        assert 'active' in page.get_supportive_plan_class()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_supportive_plan()
        page.click_phone_number_option()
        page.write_phone_number(data.PHONE_NUMBER)
        page.click_next_button()
        page.enter_text_verification_code(retrieve_phone_code(self.driver))
        assert page.get_phone_number_text() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_supportive_plan()
        page.click_payment_method_button()
        page.click_add_card_button()
        page.enter_card_details(data.CARD_NUMBER, data.CARD_CODE)
        page.press_tab_on_card_code()
        page.verify_link_button()
        page.click_link_button()
        assert self.driver.find_element(*page.CARD_NUMBER_FIELD).get_attribute('value') == data.CARD_NUMBER

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_supportive_plan()
        page.enter_comment(data.MESSAGE_FOR_DRIVER)
        assert self.driver.find_element(*page.COMMENT_LOCATOR).get_attribute('value') == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_blanket_and_handkerchiefs()
        assert page.get_blanket_and_handkerchiefs_state() == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)

        for _ in range(2):
            page.click_ice_cream_plus()
        assert page.ICE_CREAM_COUNTER_VALUE() == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.write_address_from(data.ADDRESS_FROM)
        page.write_address_to(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_supportive_plan()
        page.click_phone_number_option()
        page.write_phone_number(data.PHONE_NUMBER)
        page.click_next_button()
        page.enter_text_verification_code(retrieve_phone_code(self.driver))
        page.write_message_driver(data.MESSAGE_FOR_DRIVER)
        page.click_order_button()
        assert page.is_car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
