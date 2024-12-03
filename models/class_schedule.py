from odoo import models, fields, api

class ClassSchedule(models.Model):
    _name = 'school.class.schedule'
    _description = 'Class Schedule'
    
    class_id = fields.Many2one('school.class', string='Class', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    
    day_of_week = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    ], required=True)
    
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    room = fields.Char(string='Room Number')
    
    @api.constrains('start_time', 'end_time')
    def _check_times(self):
        for record in self:
            if record.start_time >= record.end_time:
                raise ValidationError('End time must be after start time')
            if record.start_time < 0 or record.start_time > 24:
                raise ValidationError('Invalid start time')
            if record.end_time < 0 or record.end_time > 24:
                raise ValidationError('Invalid end time')