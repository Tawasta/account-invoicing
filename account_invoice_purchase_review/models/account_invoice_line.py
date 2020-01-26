from odoo import api, fields, models, _


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    purchase_line_name = fields.Text(
        related='purchase_line_id.name',
        readonly=True,
        string='PO name',
    )

    purchase_line_quantity = fields.Float(
        related='purchase_line_id.product_qty',
        readonly=True,
        string='PO Qty',
    )

    purchase_line_price_unit = fields.Float(
        related='purchase_line_id.price_unit',
        readonly=True,
        string='PO Price',
    )
