from odoo import models, fields, api

class StudentGrade(models.Model):
    _name = 'school.student.grade'
    _description = 'Student Grade Record'
    
    student_id = fields.Many2one('school.student', string='Student', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    class_id = fields.Many2one('school.class', string='Class', required=True)
    
    exam_date = fields.Date(string='Exam Date')
    grade = fields.Float(string='Grade')
    remarks = fields.Text(string='Remarks')
    
    @api.constrains('grade')
    def _check_grade(self):
        for record in self:
            if record.grade < 0 or record.grade > 100:
                raise ValidationError('Grade must be between 0 and 100')