# -*- coding: utf-8 -*-
from odoo import models, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        """ Auto-add partner_bank_id if it is not given """
        res = super(AccountInvoice, self).create(vals)

        if not res.partner_bank_id and res.type in \
                ('out_invoice', 'out_refund'):
            res.partner_bank_id = res._get_partner_bank_id()

        return res

    def _get_partner_bank_id(self):
        """ Get partner bank id with lowest sequence number """

        partner_bank = self.env['res.partner.bank']

        partner_bank_id = partner_bank.search([
            ('company_id', '=', self.company_id.id),
            ('partner_id', '=', self.company_id.partner_id.id),
        ], limit=1, order='sequence')

        if partner_bank_id:
            return partner_bank_id.id

