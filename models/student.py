from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    registration_number = fields.Char(string='Registration Number', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, tracking=True)
    
    # Contact Information
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    
    # Academic Information
    admission_date = fields.Date(string='Admission Date', default=fields.Date.today)
    class_id = fields.Many2one('school.class', string='Current Class', tracking=True)
    
    # Academic Progress
    grade_ids = fields.One2many('school.student.grade', 'student_id', string='Grades')
    attendance_ids = fields.One2many('school.student.attendance', 'student_id', string='Attendance Records')
    
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('alumni', 'Alumni'),
        ('terminated', 'Terminated')
    ], default='draft', tracking=True)
    
    _sql_constraints = [
        ('unique_registration_number', 'unique(registration_number)', 
         'Registration Number must be unique!')
    ]
    
    @api.model
    def create(self, vals):
        if not vals.get('registration_number'):
            vals['registration_number'] = self.env['ir.sequence'].next_by_code('school.student')
        return super(Student, self).create(vals)