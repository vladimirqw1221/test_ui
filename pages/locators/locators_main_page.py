from selenium.webdriver.common.by import By


class LocatorsMainPage:
    ALL_BUTTONS_ADD_TO_CART = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
    COUNT_ITEMS = (By.XPATH, "//span[@class='shopping_cart_badge']")
    BACKPACK_ITEM_BTN = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    BACKPACK_ITEM_REMOVE_BTN = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    SELECT_FILTER = (By.XPATH, "//select[@class='product_sort_container']")
    PRICE_LIST = (By.XPATH, "//div[@class='inventory_item_price']")
    NAME_ALL_ITEMS_LIST = (By.XPATH, "//div[@class='inventory_item_name ']")
    ADD_TO_CARD_BUTTON_PDP = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
    BACK_TO_PRODUCT_BTN = (By.XPATH, "//button[@id='back-to-products']")
    REMOVE_BTN_IN_PDP = (By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory']")
    IMAGE_IN_PDP = (By.XPATH, "//img[@class='inventory_details_img']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
