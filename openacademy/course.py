from osv import osv, fields

class course(osv.Model):

    def _check_name (self, cr, uid, ids, context=None):
        record = self.browse(cr, uid, ids, context=context)        
        for data in record:
            if data.name == data.description:
                return False
        return True        


    _name = 'course.course'
    _columns = {
        'name' : fields.char('Name', size=64, required=True, translate=True),
        'description' : fields.text('Description', readonly=False),
        'responsible_id' : fields.many2one('res.users','Responsible'),
        'session_ids' : fields.one2many('session.session','course_id','Semestre'),                    
    }
    _constraints = [[_check_name, 'Erro: Nome e Descricao iguais', ['name']]]
    
    _sql_constraints = [
        ('name', 'UNIQUE (name)', 'O nome do curso deve ser unico')
    ]

    def copy(self, cr, uid, id, default={}, context=None):
         
        data = self.pool.get('course.course').browse(cr, uid, id)     
        nome = 'Copy of [' + data.name + ']'         
        if not default:
            default = {}  

        default.update({ 
            'name': nome,
        })
        return super(course, self).copy(cr, uid, id, default, context=context)