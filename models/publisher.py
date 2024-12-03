from odoo import models, fields

class Publisher(models.Model):
    _name = 'bookstore.publisher'
    _description = 'Publisher'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    code = fields.Char(string='Publisher Code', required=True)
    
    # Contact Information
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    website = fields.Char(string='Website')
    address = fields.Text(string='Address')
    
    # Relations
    book_ids = fields.One2many('bookstore.book', 'publisher_id', string='Books')
    
    # Statistics
    book_count = fields.Integer(string='Number of Books', compute='_compute_book_count')
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('unique_publisher_code', 'unique(code)', 
         'Publisher Code must be unique!')
    ]
    
    def _compute_book_count(self):
        for record in self:
            record.book_count = len(record.book_ids)