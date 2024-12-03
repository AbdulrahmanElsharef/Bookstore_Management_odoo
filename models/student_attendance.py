from odoo import models, fields, api

class StudentAttendance(models.Model):
    _name = 'school.student.attendance'
    _description = 'Student Attendance Record'
    
    student_id = fields.Many2one('school.student', string='Student', required=True)
    class_id = fields.Many2one('school.class', string='Class', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused')
    ], string='Attendance Status', required=True)
    
    remarks = fields.Text(string='Remarks')
    
    _sql_constraints = [
        ('unique_attendance', 'unique(student_id, class_id, date)', 
         'Attendance record already exists for this student on this date!')
    ]