# -*- coding: utf-8 -*-
from odoo import models, api


class AccountBankStatementLine(models.Model):

    _inherit = "account.bank.statement.line"

    def get_reconciliation_proposition(self, excluded_ids=None):
        res = super(AccountBankStatementLine,
                    self).get_reconciliation_proposition(excluded_ids)

        # Try to match via payment reference
        if self.ref:
            # Match invoice
            invoice = self.env('account.invoice').search([
                ('ref_number', '=', self.ref)
            ], limit=1)

            if invoice:
                self.env['account.move.line'].search([
                    # Conditions
                ], limit=1)

        return res
