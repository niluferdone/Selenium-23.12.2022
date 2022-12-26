# Constant olması için büyük harflerle yazılır
BASE_DOMAIN_URL = "https://www.saucedemo.com/" # domain url 
USERNAME_INFO = "user-name" # id bilgisi
USERNAME = "standard_user"
USERNAME2 = "locked_out_user"
PASSWORD_INFO = "password" # id bilgisi
PASSWORD = "secret_sauce"
LGN_BUTTON = "login-button" # id bilgisi
LOGIN = "https://www.saucedemo.com/inventory.html" # login olduktan sonraki açılan sayfa

ERROR = '//*[@data-test="error"]' # hata ekranı başlığı (xpath)
ERROR_TEXT = "Epic sadface: Username and password do not match any user in this service" # hata mesajı 
ERROR_TEXT2 = "Epic sadface: Sorry, this user has been locked out."
WRONG_PASSWORD = "wrong_password"

MENU = "react-burger-menu-btn" # menü butonu 
MENU_TEXT = "Open Menu" 

PRODUCT_NAMES_LİST= "data/productList.xlsx"
PRODUCTS_ON_BASKET = "data/addBasketFromExcel.xlsx"
SHEET = "Sheet1"
PRODUCT_LIST = '//*[@class="inventory_item"]'  # ürünü açıklayan kısım (xpath)
PRODUCT_NAME = '//*[@class="inventory_item_name"]'
PRODUCT_PRICE ='//*[@class="inventory_item_price"]'

PRODUCT_NAME_1 = "Sauce Labs Bike Light"
PRODUCT_NAME_2 = "Sauce Labs Bolt T-Shirt"
PRODUCT_NAME_3 = "Sauce Labs Onesie"
PRODUCT_NAME_4 = "Test.allTheThings() T-Shirt (Red)"
PRODUCT_NAME_5 = "Sauce Labs Backpack"
PRODUCT_NAME_6 = "Sauce Labs Fleece Jacket"

BIKE = "item_0_title_link"
BOLT = "item_1_title_link"
ONESIE= "item_2_title_link"
TESTALLTHINGS = "item_3_title_link"
BACKPACK = "item_4_title_link"
FLEECE = "item_5_title_link"

ALIGNMENT = "product_sort_container"
SET_DESC_CHAR = '//*[@value="za"]'
SET_ASC_PRICE = '//*[@value="lohi"]'

ADD_TO_CARD = "add-to-cart-sauce-labs-backpack" # add to card butonu için (id bilgisi)
ADD_TO_CARD_PRODUCT_NAME_1 = "add-to-cart-sauce-labs-bike-light"
ADD_TO_CARD_PRODUCT_NAME_2 = "add-to-cart-sauce-labs-bolt-t-shirt"
ADD_TO_CARD_PRODUCT_NAME_3 = "add-to-cart-sauce-labs-onesie"
ADD_TO_CARD_PRODUCT_NAME_4 = "add-to-cart-test.allthethings()-t-shirt-(red)"
ADD_TO_CARD_PRODUCT_NAME_5 = "add-to-cart-sauce-labs-backpack"
ADD_TO_CARD_PRODUCT_NAME_6 = "add-to-cart-sauce-labs-fleece-jacket"

BASKET_ITEM = "shopping_cart_badge" # item butonu için (class name)
ITEM_COUNT = "1"

PRODUCT_REMOVE = "remove-sauce-labs-backpack" # remove butonu için (name bilgisi)
REMOVE_CARD_LABS_BACKPACK_NAME = "remove-sauce-labs-backpack"
REMOVE_TEXT = "REMOVE" # remove butonu için 

BASKET_BUTTON = '//*[@class="shopping_cart_link"]'
BASKET_CHECK = '//*[@class="shopping_cart_badge"]'
BASKET_REMOVE = "/html/body/div/div/div/div[2]/div/div[1]/div[3]"


FIRST_PRODUCT = "Sauce Labs Bike Light"
SECOND_PRODUCT = "Sauce Labs Onesie"
FIRST_PRODUCT_ID = "add-to-cart-sauce-labs-bike-light"
SECOND_PRODUCT_ID = "add-to-cart-sauce-labs-onesie"
BASKET_LINK = "shopping_cart_link"