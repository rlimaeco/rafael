from osv import osv, fields

class attendee(osv.Model):
    _name = 'attendee.attendee'
    _columns = {
        'name' : fields.char('Name', size=64, required=False, translate=True),
        'partner_id' : fields.many2one('res.partner','Aluno'),
        'session_id' : fields.many2one('session.session','Turma'),                
    }