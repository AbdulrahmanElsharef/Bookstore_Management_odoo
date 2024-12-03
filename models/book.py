from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = 'bookstore.book'
    _description = 'Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True, tracking=True)
    isbn = fields.Char(string='ISBN', required=True, tracking=True)
    description = fields.Text(string='Description')
    pages = fields.Integer(string='Number of Pages')
    edition = fields.Char(string='Edition')
    published_date = fields.Date(string='Publication Date')
    
    # Price and Stock Information
    list_price = fields.Float(string='List Price', required=True)
    cost_price = fields.Float(string='Cost Price')
    stock_quantity = fields.Integer(string='Stock Quantity', default=0)
    
    # Relations
    author_ids = fields.Many2many('bookstore.author', string='Authors')
    publisher_id = fields.Many2one('bookstore.publisher', string='Publisher', required=True)
    category_id = fields.Many2one('bookstore.category', string='Category', required=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued')
    ], default='draft', tracking=True)
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('unique_isbn', 'unique(isbn)', 'ISBN must be unique!')
    ]
    
    @api.constrains('list_price', 'cost_price')
    def _check_prices(self):
        for record in self:
            if record.list_price < 0:
                raise ValidationError('List price cannot be negative')
            if record.cost_price < 0:
                raise ValidationError('Cost price cannot be negative')