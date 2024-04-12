# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    _inherit = ['product.product']

    rate_product = fields.Selection(selection=[('1', '1'),
                                               ('2', '2'),
                                               ('3', '3'),
                                               ('4', '4'),
                                               ('5', '5')],
                                    string='Rate Product')
