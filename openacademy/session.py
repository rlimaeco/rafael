# coding: utf-8
from osv import osv, fields
#from openerp import netsvc 

from datetime import datetime, timedelta


class session(osv.Model):
    _name = 'session.session'

    def test_seats(self, cr, uid, ids, context=None):
        i= self.browse(cr, uid, ids, context=context)
        if not i:
            return False        
        if i.taken_seats > 50 and state == 'draft':
            return True

    def action_draft(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'draft'}, context=context)
        # wf_service = netsvc.LocalService("workflow")
        # for inv_id in ids:
        #     wf_service.trg_delete(uid, 'session.session', inv_id, cr)
        #     wf_service.trg_create(uid, 'session.session', inv_id, cr)
        # return True
        

    def action_confirm(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state':'confirmed'}, context=context)

    def action_done(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state':'done'}, context=context)

    def _get_attendee_count(self, cr, uid, ids, name, args, context=None):
        res = {}
        for session in self.browse(cr, uid, ids, context=context):
            res[session.id] = len(session.attendee_ids)
            print res[session.id], 'ATTENDEE aquiiiiiiIIIIIIIIIIIIIIIIIIIIII'
        return res
        

    def _determin_hours_from_days_elapsed(self, cr, uid, ids, field, arg, context=None):
        result = {}
        sessions = self.browse(cr, uid, ids, context=context)
        for session in sessions:
            result[session.id] = (session.days_elapsed * 24 if session.days_elapsed else 0)
        return result
        print "DETERMIN HOURSSSS      <<<<<<<<<<"

    def _set_hours(self, cr, uid, id, field, value, arg, context=None):
        if value:
            self.write(cr, uid, id,
                       {'days_elapsed' : (value / 24) },
                       context=context)
            print "SET HOURSSSSS      <<<<<<<<<<"


    def _determin_end_date(self, cr, uid, ids, field, arg, context=None):
        result = {}
        for data in self.browse(cr, uid, ids, context=context):
            if data.start_date and data.days_elapsed:
                start_date = datetime.strptime(data.start_date, "%Y-%m-%d")
                days_elapsed = timedelta(days=(data.days_elapsed - 1))
                end_date = start_date + days_elapsed
                #print "Dataaaaaaaa" + end_date
                result[data.id] = end_date.strftime("%Y-%m-%d")
            else:
                result[data.id] = data.start_date
        return result

    def _set_end_date(self, cr, uid, id, field, value, arg, context=None):
        data = self.browse(cr, uid, id, context=context)
        if data.start_date and value:
            start_date = datetime.strptime(data.start_date, "%Y-%m-%d")
            end_date = datetime.strptime(value[:10], "%Y-%m-%d")            
            days_elapsed = end_date - start_date
            self.write(cr, uid, id, {'days_elapsed' : (days_elapsed.days +1)}, context=context)

            # Até aqui o comentario

    def _amount_vacancy(self, cr, uid, ids, field_name, arg, context):
        res = {}
        if context is None:
            context = {}
        try:
            for i in self.browse(cr, uid, ids, context=None):            
                res[i.id]=100*(float(len(i.attendee_ids))/i.n_seats)                                
            return res
        except ZeroDivisionError:
            return 0.0

    
        

    
    _columns = {
        'name' : fields.char('Nome', size=64, required=True, translate=True),
        'start_date' : fields.date('Inicio'),
        'days_elapsed' : fields.integer('Duracao'),
        'n_seats' : fields.integer('Vagas', domain=['!',('n_seats', '=', '0')]),
        'active' : fields.boolean('Ativo'),   
        'color' : fields.integer('Color'),
        'state' : fields.selection([('draft','Draft'),('confirmed','Confirmed'),('done','Done')], string="State"),
        'instructor_id' : fields.many2one('res.partner','Professor',
            domain=[('|'),('|'),('is_instructor','=','True'),
            ('teacher_level','=','1'),('teacher_level','=','2')]), 
        'course_id' : fields.many2one('course.course','Materia'),
        'attendee_ids' : fields.one2many('attendee.attendee','session_id','Alunos'),
        'taken_seats': fields.function(_amount_vacancy, string='Percentual Vaga', type="float"),
        'end_date' : fields.function(_determin_end_date, fnct_inv=_set_end_date, store=True, type='date', string="Data Final"),
        'hours' : fields.function(_determin_hours_from_days_elapsed, fnct_inv=_set_hours, type='float', string='Hours'),
        'attendee_count' : fields.function(_get_attendee_count, type='integer', string='Attendee Count', store=True),               
    }
    _defaults = {
        'active' : True, 
        'state' : 'draft', 
        'start_date' : fields.date.context_today,   
    }

    def onchange_vagas(self, cr, uid, ids, attendee_ids, n_seats, context=None):        
        #print "MUDEIIII ===============DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD AHA"
        data2 = self.pool.get('session.session').browse(cr, uid, id)
        print 'Ativo: ', data2.active 
        if n_seats <= 0:             
            raise osv.except_osv(_('Atencao!'), ('numero de vagas invalido'))
        print "NUMERO DE VAGAS:: ", n_seats
        res=100*(float(len(attendee_ids))/n_seats) 
        if res > 100:
            raise osv.except_osv(_('Atencao!'), ('numero de vagas invalido'))
        return { 'value' : {'taken_seats' : res } }

   
    