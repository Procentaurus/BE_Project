from telnetlib import EC

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import random as r
import time

# Zmienne
fake = Faker()
usermail = fake.email()
userpassword = 'userpassword'
userfirstname = fake.first_name()
userlastname = fake.last_name()
useraddress = 'Wocha Szwocha 69'
userzipcode = '42-000'
usercity = 'Dziubiszewo'

# Inicjalizacja
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://localhost/")
driver.maximize_window()


def click_link_on_current_page(link_text):
    links = driver.find_elements("xpath", "//a[@href]")
    for link in links:
        print(link.get_attribute("innerHTML"))
        if link_text in link.get_attribute("innerHTML"):
            link.click()
            break


def choose_available_product():
    product_elements = driver.find_elements(By.CLASS_NAME, 'js-product')
    for random_product in product_elements:
        availability_flags = random_product.find_elements(By.CLASS_NAME, 'product-flag.out_of_stock')
        if not availability_flags:
            random_product.click()
            break


def add_5_of_category_to_cart(category_var):
    url = f"https://localhost/{category_var}"
    link = driver.find_element(By.XPATH, f'//a[@href="{url}"]')
    link.click()

    for x in range(5):
        choose_available_product()
        szczegoly_produktu_link = driver.find_element(By.XPATH, '//a[contains(text(), "Szczegóły produktu")]')
        szczegoly_produktu_link.click()
        product_quantities = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-quantities"))
        )
        data_stock_value = product_quantities.find_element(By.CSS_SELECTOR, "span[data-stock]").get_attribute(
            "data-stock")
        quantity_input = driver.find_element(By.ID, 'quantity_wanted')
        quantity_input.send_keys(Keys.CONTROL + "a")  # Select all text in the input field
        quantity_input.send_keys(Keys.BACKSPACE)  # Delete the selected text
        quantity_input.send_keys(data_stock_value)  # Type the new value
        click_button_by_class('add-to-cart')
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(@aria-hidden, "true")]/i[@class="material-icons" and text()="close"]')))
        element.click()
        time.sleep(2)
        url = f"https://localhost/{category_var}"
        link = driver.find_element(By.XPATH, f'//a[@href="{url}"]')
        link.click()
    time.sleep(2)


def click_button_by_class(class_name):
    driver.find_element(By.CLASS_NAME, class_name).click()

# d. Rejeastracja nowego konta
login_button = driver.find_element(By.CSS_SELECTOR, 'a[title="Zaloguj się do swojego konta klienta"]')
login_button.click()
signup_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Nie masz konta? Załóż je tutaj')]")
signup_button.click()
radio_button = driver.find_element(By.ID, 'field-id_gender-1')
firstname_input = driver.find_element(By.NAME, 'firstname')
firstname_input.send_keys(userfirstname)
lastname_input = driver.find_element(By.NAME, 'lastname')
lastname_input.send_keys(userlastname)
usermail_input = driver.find_element(By.NAME, 'email')
usermail_input.send_keys(usermail)
userpassword_input = driver.find_element(By.NAME, 'password')
userpassword_input.send_keys(userpassword)
customer_privacy_checkbox = driver.find_element(By.NAME, 'customer_privacy')
customer_privacy_checkbox.click()
required_acceptance_checkbox = driver.find_element(By.NAME, 'psgdpr')
required_acceptance_checkbox.click()
save_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
save_button.click()
time.sleep(2)

# a. Dodanie do koszyka 10 produktów (w różnych ilościach) z dwóch różnych kategorii
# kategoria 'części'
add_5_of_category_to_cart("5-czesci")

# kategoria 'odzież rowerowa'
add_5_of_category_to_cart("6-odziez-rowerowa")

# c. Usunięcie z koszyka 3 produktów
koszyk_link = driver.find_element(By.XPATH, '//a[contains(@href, "/koszyk?action=show")]')
koszyk_link.click()
remove_links = driver.find_elements(By.CSS_SELECTOR, '.remove-from-cart')
items_to_remove = r.sample(remove_links, 3)
for item in items_to_remove:
    try:
        item.click()
    except StaleElementReferenceException:
        # If the element is stale, find it again
        remove_links = driver.find_elements(By.CSS_SELECTOR, '.remove-from-cart')
        items_to_remove = r.sample(remove_links, 3)
        item = items_to_remove[0]  # You may need to adjust this based on your logic
        item.click()

remove_links = driver.find_elements(By.CSS_SELECTOR, '.remove-from-cart')
for link in remove_links:
    try:
        link.click()
    except StaleElementReferenceException:
        # If the element is stale, find it again
        remove_links = driver.find_elements(By.CSS_SELECTOR, '.remove-from-cart')
        link = remove_links[0]  # You may need to adjust this based on your logic
        link.click()

# b. Wyszukanie produktu po nazwie i dodanie do koszyka losowego produktu spośród znalezionych
search_input = driver.find_element(By.NAME, 's')
search_input.clear()
search_input.send_keys('bluza')
search_input.submit()
product_elements = driver.find_elements(By.CLASS_NAME, 'js-product')

while True:
    random_product = r.choice(product_elements)
    random_product.click()
    availability_element = driver.find_element(By.ID, 'product-availability')
    availability_text = availability_element.text.strip()
    if "Obecnie brak na stanie" not in availability_text:
        break
    else:
        driver.back()

click_button_by_class('add-to-cart')
time.sleep(2)

checkout_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Przejdź do realizacji zamówienia')]")
checkout_button.click()
checkout_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Przejdź do realizacji zamówienia')]")
checkout_button.click()

# e. Wykonanie zamówienia zawartości koszyka
useraddress_input = driver.find_element(By.NAME, 'address1')
useraddress_input.send_keys(useraddress)
userzipcode_input = driver.find_element(By.NAME, 'postcode')
userzipcode_input.send_keys(userzipcode)
usercity_input = driver.find_element(By.NAME, 'city')
usercity_input.send_keys(usercity)
continue_button = driver.find_element(By.NAME, 'confirm-addresses')
continue_button.click()
time.sleep(2)

# g. Wybór jednego z dwóch przewoźników
radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
random_index = r.randint(0, len(radio_buttons) - 1)
time.sleep(2)
radio_buttons[random_index].click()
dalej_button = driver.find_element(By.NAME, 'confirmDeliveryOption')
dalej_button.click()


# f. Wybór metody płatności: przy odbiorze
cash_on_delivery_radio = driver.find_element(By.ID, 'payment-option-2')
cash_on_delivery_radio.click()
terms_checkbox = driver.find_element(By.ID, 'conditions_to_approve[terms-and-conditions]')
terms_checkbox.click()
order_button = driver.find_element(By.XPATH, '//button[contains(text(), "Złóż zamówienie")]')
order_button.click()


account_link = driver.find_element(By.CLASS_NAME, 'account')
account_link.click()
history_link = driver.find_element(By.ID, 'history-link')
history_link.click()
szczegoly_link = driver.find_element(By.LINK_TEXT, 'Szczegóły')
szczegoly_link.click()
download_link = driver.find_element(By.LINK_TEXT, 'Pobierz fakturę proforma w pliku PDF')
download_link.click()

print("Success!")
