# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Change Request Note",
    "version": "16.0.1.0.0",
    "author": "By Ibrahim Ali",
    "website": "",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["base","mail",'hr'],
    "data": [
        "security/ir.model.access.csv",
        "reports/report.xml",
        "reports/tempale.xml",
        "views/view.xml",
    ],
    "installable": True,
}
