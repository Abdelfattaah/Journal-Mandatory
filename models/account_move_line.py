# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountAccount(models.Model):
    _inherit = 'account.account'

    mandatory_analytic_account = fields.Boolean(string="Mandatory Analytic Account")
    mandatory_partner = fields.Boolean(string="Mandatory Partner")
    bypass_users_ids = fields.Many2many('res.users', string="Bypass Users")


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.constrains('analytic_account_id', 'partner_id')
    def _check_mandatory_fields(self):
        for line in self:
            account = line.account_id
            user = self.env.user

            if user in account.bypass_users_ids:
                continue

            if account.mandatory_analytic_account and not line.analytic_distribution:
                raise ValidationError(f"Analytic account is required for the account '{account.name}'.")

            if account.mandatory_partner and not line.partner_id:
                raise ValidationError(f"Partner is required for the account '{account.name}'.")
