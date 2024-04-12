{
    'name': 'POS Rating',
    'version': '17.0.1.0.0',
    'description': 'Rating of Product in POS',
    'category': 'Point of Sale/POS Rating',
    'summary': 'POS Rating of Products',
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'point_of_sale',
        'product',
        ],
    'data': [
        'views/product_views.xml',
    ],
    'assets':{
        'point_of_sale._assets_pos':[
            'pos_rating/static/src/js/product_rate.js',
            'pos_rating/static/src/xml/product_receipt.xml',
            'pos_rating/static/src/xml/product_rate.xml',
            'pos_rating/static/src/xml/product_card.xml',

        ]
    }
}
