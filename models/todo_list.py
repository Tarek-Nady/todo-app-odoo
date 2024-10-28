from odoo import api, fields, models, _

class OwlTodo(models.Model):
    _name = 'todo.list'
    _description = 'Todo List App'

    name = fields.Char(string='Task Name')
    completed = fields.Boolean(string='Task Completed')
    color = fields.Char()