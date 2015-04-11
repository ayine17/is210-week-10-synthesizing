#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 11:01:19 2015

@author: aayeta
"""


def sum_orders(customers, orders):
    """a function to combine the two datasets into a single dictionary keyed by
       customer_id

    Args:
        customers (dict): A dictionary of customers keyed by customer_id
        orders (dict): A dictionary of orders keyed by order id
    Return:
        Return the combined dictionary of the two args by customer_id.

    Examples:

    >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
    >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
    >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
    {2: {'name': 'Person One',
         'email': 'email@one.com',
         'orders': 2,
         'total': 20}
     3: {'name': 'Person Two',
         'email': 'email@two.com',
         'orders': 1,
         'total': 15}}
    >>> import data
    >>> sum_orders(data.CUSTOMERS, data.ORDERS)
    {1: {'total': 1287, 'email': 'evorsoisson@komarr.net',
         'name': 'Ekaterin Vorsoisson', 'orders': 3}, 2: {'total': 2778,
         'email': 'cordelia@beta.com', 'name': 'Cordelia Naismith',
         'orders': 5}, 3: {'total': 358, 'email': 'iv398@barrayar.net',
         'name': 'Ivan Vorpatril', 'orders': 3}, 4: {'total': 1207,
         'email': 'viceroy@sergyar.net', 'name': 'Aral Vorkosigan',
         'orders': 5}, 5: {'total': 451, 'email': 'admiral@dendarii.com',
         'name': 'Eli Quinn', 'orders': 3}, 6: {'total': 1198,
         'email': 'portmaster@graf.net', 'name': 'Bel Thorne',
         'orders': 3}, 7: {'total': 1897, 'email': 'impsec@barrayar.net',
         'name': 'Simon Illyan', 'orders': 3}, 8: {'total': 204,
         'email': 'dg1367@barrayar.net', 'name': 'Duv Galeni', 'orders': 1},
         9: {'total': 1704, 'email': 'impsec@barrayar.net',
         'name': 'Gregor Vorbarra', 'orders': 2}}
    """
    new_dict = {}

    total = 0

    for order in orders.itervalues():

        email = customers[order['customer_id']]['email']
        name = customers[order['customer_id']]['name']
        customerid = order['customer_id']

        if order['customer_id'] in customers.keys():
            if order['customer_id'] in new_dict:

                total = order['total'] + new_dict[customerid]['total']

                orders = new_dict[customerid]['orders'] + 1

            else:

                total = order['total']
                orders = 1
        new_dict1 = dict(email=email, name=name, total=total, orders=orders)
        new_dict.update({customerid: new_dict1})
    return new_dict
