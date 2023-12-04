def language_wrapper(value):
    return {
        'language': {
                'attrs': {'id': '1'},
                'value': value
                }
    }

def categories_category_wrapper(id):
    return {
        'categories': category_wrapper(id)
    }

def category_wrapper(id):
    return {
        'category': {'id': f'{id}'}
    }

def get_category_id(response):
    return response['categories']['category']['attrs']['id']

def get_stock_available_id(product):
    return product['product']['associations']['stock_availables']['stock_available']['id']