from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string='Subject Code', required=True)
    description = fields.Text(string='Description')
    credits = fields.Integer(string='Credits')
    
    teacher_ids = fields.Many2many('school.teacher', string='Teachers')
    class_ids = fields.Many2many('school.class', string='Classes')
    
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('unique_subject_code', 'unique(code)', 
         'Subject Code must be unique!')
    ]