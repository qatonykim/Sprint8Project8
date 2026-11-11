from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(., 'Call a taxi')]")
    SUPPORTIVE_PLAN_CARD = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Supportive']]")
    PHONE_NUMBER_OPTION = (By.XPATH, "//div[text()='Phone number']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@id='phone']")
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Next']")
    TEXT_CODE_FIELD = (By.XPATH, "//label[text()='Enter the code']")
    TEXT_CODE_CONFIRM_FIELD = (By.XPATH, "//button[text()='Confirm']")
    PHONE_NUMBER_DISPLAY_TEXT = (By.XPATH, "//div[@class='np-text']")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[text()='Payment method']")
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='1234 0000 4321']")
    CARD_CODE_FIELD = (By.XPATH, "//input[@placeholder='12']")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    COMMENT_LOCATOR = (By.XPATH, "//input[@placeholder='Get some whiskey']")
    BLANKET_AND_HANDKERCHIEFS_SLIDER = (By.XPATH, "//div[text()='Blanket and handkerchiefs']/following-sibling::div//span[@class='slider round']")
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, "//div[@class='counter-plus' and text()='+']")
    ICE_CREAM_COUNTER_VALUE = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-value']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='smart-button']")
    CAR_SEARCH_MODAL = (By.XPATH, "//div[@class='order-body']")



    def __init__ (self, browser):
        self.driver = browser

    #define an action for each element
    def write_address_from(self, from_address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)
    def write_address_to(self, to_address):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)
    def click_call_taxi_button(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON))
        button.click()
    def click_supportive_plan(self):
        wait = WebDriverWait(self.driver, 10)
        plan_btn = wait.until(EC.element_to_be_clickable(self.SUPPORTIVE_PLAN_CARD))
        plan_btn.click()
    def click_phone_number_option(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_OPTION).click()
    def write_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()
    def enter_text_verification_code(self, text_code):
        self.driver.find_element(*self.TEXT_CODE_FIELD).send_keys(text_code)
    def click_confirm_button(self):
        self.driver.find_element(*self.TEXT_CODE_CONFIRM_FIELD).click()
    def get_phone_number_text(self):
        element = self.driver.find_element(*self.PHONE_NUMBER_DISPLAY_TEXT)
        return element.text
    def click_payment_method_button(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()
    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()
    def enter_card_details(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_number)
    def press_tab_on_card_code(self):
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(Keys.TAB)
    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON).click()
    def verify_link_button(self):
        wait = WebDriverWait(self.driver, 10)
        link_button = wait.until(EC.element_to_be_clickable(self.LINK_BUTTON))
        link_button.click()
    def get_address_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')
    def get_address_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')
    def enter_comment(self, comment):
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(comment)
    def click_blanket_and_handkerchiefs(self):
        wait = WebDriverWait(self.driver, 10)
        slider = wait.until(EC.element_to_be_clickable(self.BLANKET_AND_HANDKERCHIEFS_SLIDER))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", slider)
        slider.click()
    def get_blanket_and_handkerchiefs_state(self):
        checkbox = self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_SLIDER)  # or your checkbox/slider element
        return checkbox.is_selected()
    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON).click()
    def write_message_driver(self, comment):
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(comment)
    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()
    def is_car_search_modal_displayed(self):
        modal = self.driver.find_element(*self.CAR_SEARCH_MODAL)
        return modal.is_displayed()