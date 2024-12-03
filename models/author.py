from odoo import models, fields

class Author(models.Model):
    _name = 'bookstore.author'
    _description = 'Author'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    biography = fields.Text(string='Biography')
    birth_date = fields.Date(string='Birth Date')
    nationality = fields.Char(string='Nationality')
    
    # Contact Information
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    website = fields.Char(string='Website')
    
    # Relations
    book_ids = fields.Many2many('bookstore.book', string='Books')
    
    # Statistics
    book_count = fields.Integer(string='Number of Books', compute='_compute_book_count')
    active = fields.Boolean(default=True)
    
    def _compute_book_count(self):
        for record in self:
            record.book_count = len(record.book_ids)