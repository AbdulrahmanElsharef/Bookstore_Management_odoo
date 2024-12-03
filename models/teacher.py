from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    employee_id = fields.Char(string='Employee ID', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True)
    
    # Contact Information
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    
    # Professional Information
    qualification = fields.Char(string='Qualification')
    joining_date = fields.Date(string='Joining Date', default=fields.Date.today)
    department = fields.Char(string='Department')
    
    # Class Relations
    class_ids = fields.One2many('school.class', 'teacher_id', string='Classes')
    subject_ids = fields.Many2many('school.subject', string='Subjects')
    
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('active', 'Active'),
        ('on_leave', 'On Leave'),
        ('terminated', 'Terminated')
    ], default='active', tracking=True)
    
    _sql_constraints = [
        ('unique_employee_id', 'unique(employee_id)', 
         'Employee ID must be unique!')
    ]