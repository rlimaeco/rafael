# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2011  Rafael Lima - Kmee                                      #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU Affero General Public License for more details.                          #
#                                                                             #
#You should have received a copy of the GNU Affero General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

{
    'name': 'Account payment extension with Webkit report',
    'description': 'Extension of account_payment_extension with an additional report webkit',
    'category': 'Localisation',
    'license': 'AGPL-3',
    'author': 'Kmee, OpenERP Brasil',
    'website': 'http://openerpbrasil.org',
    'version': '0.1',
    'depends': [
        'l10n_br_account',
        'l10n_br_account_payment',
        'account_payment_extension',
    ],
    'data': [
        'account_move_line_view.xml',

    ],
    'installable': True
}
