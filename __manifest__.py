# -*- coding: utf-8 -*-
{
    'name': "journal_mandatory",

    'summary': """
    Modifying the Chart of Accounts in Odoo to introduce restrictions on 
    specific accounts that require an analytic account and a partner.    
    """,

    'author': "Abdelfattah Mohamed",
    'website': "https://abdelfattaah.github.io/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','account','analytic'],

    'data': [
        'views/views.xml',
    ],

}
