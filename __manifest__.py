# -*- coding: utf-8 -*-
{
    'name': "simple theme",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website','website_theme_install'],

    # always loaded
    'data': [
        'views/acceuil.xml',
        'views/detailMedecine.xml',
        'views/register-doctor.xml',
        'views/register.xml',
        'views/booking-page.xml',
        'views/login-2.xml',
        'views/pharmacie-detail.xml',
        'views/submit-review.xml',
        'views/info.xml',
        'views/index.xml',
        'views/formulaire.xml',
        'views/liste-rechercher.xml',
        'views/register-doctor-working.xml',
        'views/liste_docteur_connecter.xml',
        'views/profil_docteur_patient.xml',
        'views/confirmation.xml',
        'views/confirmer_dorcteur.xml',
        'views/videoconferance.xml',
        'security/ir.model.access.csv',

        #Adminstrateur
        'admin/indexUser.xml',
        'admin/signe.xml',
        'admin/consulter.xml',
        'admin/user_profile.xml',
        'admin/table.xml',
        'admin/charts.xml',
        'admin/annonce.xml',
        'admin/message.xml',
        'admin/reservation.xml',
        'admin/ordonnance.xml',
        'admin/commentaire.xml',
        #Qweb
        # 'qweb/users.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}