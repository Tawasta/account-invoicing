from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def action_invoice_open(self):

        for record in self:
            if record.origin:
                record.comment += '{}\nOrigin: {}'.format(
                    record.comment,
                    record.origin,
                )
        return super(AccountInvoice, self).action_invoice_open()