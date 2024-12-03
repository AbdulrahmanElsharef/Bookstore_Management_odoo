from odoo import models, fields

class Category(models.Model):
    _name = 'bookstore.category'
    _description = 'Book Category'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    code = fields.Char(string='Category Code', required=True)
    description = fields.Text(string='Description')
    
    # Relations
    parent_id = fields.Many2one('bookstore.category', string='Parent Category')
    child_ids = fields.One2many('bookstore.category', 'parent_id', string='Child Categories')
    book_ids = fields.One2many('bookstore.book', 'category_id', string='Books')
    
    # Statistics
    book_count = fields.Integer(string='Number of Books', compute='_compute_book_count')
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('unique_category_code', 'unique(code)', 
         'Category Code must be unique!')
    ]
    
    def _compute_book_count(self):
        for record in self:
            record.book_count = len(record.book_ids)