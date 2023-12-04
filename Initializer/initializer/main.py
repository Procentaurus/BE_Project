from prestapyt import PrestaShopWebServiceDict
from pprint import pprint
from category import CategoryInitializer
from product import ProductInitializer

WEBSERVICE_KEY = 'GBZJQQCCAVF9LFINX6L778KPV7PSF6MI'

prestashop = PrestaShopWebServiceDict('https://localhost/api', WEBSERVICE_KEY)

ctg_init = CategoryInitializer(prestashop)
ctg_init.initialize_categories()

prdct_init = ProductInitializer(prestashop)
prdct_init.initialize_products()