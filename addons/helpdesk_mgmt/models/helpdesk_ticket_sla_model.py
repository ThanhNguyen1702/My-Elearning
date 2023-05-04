from odoo import fields, models, api


class HelpdeskTicketSLAModel(models.Model):
    _name = "helpdesk.ticket.sla.model"
    _description = "Helpdesk Ticket SLA"
    _order = "sequence, id"


    sequence = fields.Integer(default=10)
    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    description = fields.Html(string="Mô tả")
    timelimit = fields.Float(string="Thời hạn", widget ="float_time" )
    color = fields.Integer(string="Color Index" , default=1)

    


class HelpdeskTicketSLA(models.Model):
    _name = "helpdesk.ticket.sla"
    _description = "Helpdesk Ticket SLA"
    _order = "id"

    name = fields.Char()
    status = fields.Selection([('in_progress', 'In Progress'), ('success', 'Success'), ('fail', 'Failed')], default='in_progress')
    sla_model_id = fields.Many2one(comodel_name="helpdesk.ticket.sla.model", string="Kiến trúc SLA")
    from_stage_id = fields.Many2one(comodel_name="helpdesk.ticket.stage", string="Trạng thái bắt đầu")
    to_stage_id = fields.Many2one(comodel_name="helpdesk.ticket.stage", string="Trạng thái kết thúc")

    ticket_id = fields.Many2one(comodel_name="helpdesk.ticket", string="Yêu cầu")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    ticket_id = fields.Many2one(comodel_name="helpdesk.ticket", string="Yêu cầu", )
    explaination = fields.Text(string="Giải trình")
    sla_time = fields.Float(related = "sla_model_id.timelimit" ,string="Thời hạn", widget ="float_time" )