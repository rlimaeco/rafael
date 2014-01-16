from osv import osv, fields

class partner(osv.Model):
    _name = 'res.partner'
    _inherit= 'res.partner' 
    _columns={
       'is_instructor' : fields.boolean('Instructor'),       
       'session_ids' : fields.many2one('session.session','Materia'),   
       'teacher_level' : fields.integer('Professor', domain=[('|'),('teacher_level','=','1'),('teacher_level','=','2')]),     
    }