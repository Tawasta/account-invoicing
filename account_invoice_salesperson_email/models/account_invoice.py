
from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    salesperson_email = fields.Char()

    @api.onchange('user_id')
    def user_id_onchange_phone_and_email(self):
        email = self.user_id.partner_id.email or ''

        if self.salesperson_email:
            self.comment = self.comment.replace(
                '\n' + _("Handler: ") + self.salesperson_email, '')
            self.comment = self.comment.replace(
                 _("Handler: ") + self.salesperson_email, '')

        if self._origin.user_id:
            old_email = self._origin.user_id.partner_id.email or ''
            self._origin.comment = self._origin.comment.replace('\n' + _("Handler: ") + old_email, '')

        email_line = '\n' if self.comment else ''

        if email:
            self.comment += '{}{}{}'.format(email_line, _("Handler: "), email)

        self.salesperson_email = self.user_id.partner_id.email
