# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class FleetVehicleSeat(models.Model):
    _name = "fleet.vehicle.seat"
    _description = "Vehicle Seat"

    name = fields.Char(
        string="Seat",
        required=True,
    )
    vehicle_id = fields.Many2one(
        string="Vehicle",
        comodel_name="fleet.vehicle",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
    )


class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    @api.one
    @api.depends("seat_ids")
    def _compute_seat(self):
        self.seats = len(self.seat_ids)

    seats = fields.Integer(
        string="# Seats",
        compute="_compute_seat",
        store=True,
        readonly=True,
    )
    seat_ids = fields.One2many(
        string="Seats",
        comodel_name="fleet.vehicle.seat",
        inverse_name="vehicle_id",
    )
