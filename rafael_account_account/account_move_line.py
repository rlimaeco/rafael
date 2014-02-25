# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2011  Rafael Lima - Kmee                                  	  #
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

from osv import orm, fields


class account_move_line(orm.Model):
    _inherit = 'account.account'
    _columns = {
        # 'revenue_expense': fields.related(
        #     'journal_id', 'revenue_expense', type='boolean',
        #     relation='account.journal', string='Revenue Expense',
        #     store=False, readonly=True),
         'due_date_from':fields.function(lambda *a,**k:{}, method=True, type='date',string="Vencido desde"),
         'due_date_to':fields.function(lambda *a,**k:{}, method=True, type='date',string="Vence ate"),
    }
