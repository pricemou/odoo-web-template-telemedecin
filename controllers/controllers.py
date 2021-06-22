# -*- coding: utf-8 -*-
from odoo import http
import logging
_logger = logging.getLogger(__name__) 

class OpenMedecin(http.Controller):
    @http.route('/detail-medecin/<int:medecin_id>', auth='public' ,website=True)
    def index(self, medecin_id):
        medecin_detail = http.request.env['medical.physician'].browse([medecin_id])
        return http.request.render('webtemplate.detailMedecine', { 'medecin_detail': medecin_detail})

    @http.route('/booking-page', auth='public')
    def booking(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.booking')

    @http.route('/docteur_patient/<int:medecin_id>', auth='public')
    def docteur_patient(self, medecin_id):
        userConnect = http.request.session.uid

        if userConnect:
            userConnectSatus = True
        else :
            userConnectSatus = False


        medecin_detail = http.request.env['medical.physician'].sudo().browse([medecin_id])
        return http.request.render('webtemplate.docteur_patient',
         {
            'medecin_detail': medecin_detail,
            'userConnect': userConnectSatus,
         }
        )
    
    @http.route('/videoconferance', auth='public')
    def videoconferance(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.videoconferance')

    @http.route('/medecin_connect', auth='public')
    def medecin_connect(self, **kw):
        medecin = http.request.env['medical.physician'].sudo()
        userConect = http.request.session.uid
        userUconnect = http.request.env['res.users'].sudo().browse([userConect])

        return http.request.render('webtemplate.medecin_connect', {'medecin': medecin.search([]), "user_id": userUconnect})

    # @http.route('/index', auth='public' ,website=True)
    # def booking(self, **kw):
    #     return http.request.render('webtemplate.index')
     
    @http.route('/register', auth='public')
    def register(self, **kw):
        
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.register')

    @http.route('/register-doctor-working', auth='public',website=True)
    def registerDoctorWorking(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.registerWorking')
    
    @http.route('/login', auth='public' ,website=True)
    def login(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.login')
    
    @http.route('/lsteRechercher', auth='public' ,website=True)
    def lsteRechercher(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.listeRechercher')
    
    @http.route('/info', auth='public')
    def info(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.info')

    @http.route('/confirmation', auth='public')
    def confirmation(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.confirmation')

    @http.route('/sumbitReviews', auth='public',website=True)
    def sumbitReviews(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.sumbitReviews')
    
    @http.route('/pharmacie-detail', auth='public',website=True)
    def pharmacie(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.pharmacieDetail')

    @http.route('/formulaire', auth='public', website=True)
    def formulaire(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.formulaire')


    @http.route('/aller/vers', auth='public', website=True)
    def function_test(self, **kw):
        nom = kw["nom"]
         # add logging
        _logger.info('------------------------')
        _logger.info(nom)
        _logger.info('------------------------')
        # add logging
        vals = {
            'name' : nom,
        }
        creation =  http.request.env['webtemplate.categorie'].sudo().create(vals)
        return http.request.render('webtemplate.confirmation',{'nom': nom })


class Docteur_partien(http.Controller):

    @http.route('/register-doctor', auth='public',website=True)
    def registerDoctor(self, **kw):
        # Teachers = http.request.env['academy.teachers']
        return http.request.render('webtemplate.docteurRegister')

    #-------------------------------------------
    #Enregistrement de docteur
    #-------------------------------------------
    @http.route('/enregister/docteur', auth='public', website=True)
    def function_enregister(self, **kw):
        nom = kw['nom']
        prenom = kw['prenom']
        specialisations = kw['specialisations']
        ville = kw['ville']
        phone = kw['phone']
        tel = kw['tel']
        email = kw['email']
        is_doctor = False
        is_person =True
        
        if specialisations == 'docteur':
            is_doctor = True
        
        name = prenom + ' '+ nom
        
        vals = { 
        'name' : name,
        'phone' : phone,
        'mobile' : tel,
        'city': ville,
        'email': email,
        'is_doctor':is_doctor,
        'is_person': is_person,
        }

        specialist = {
            'name':specialisations
        }

        contact_id =  http.request.env['res.partner'].sudo().create(vals)
        speciali_id = http.request.env['medical.speciality'].sudo().create(specialist)

        cpt = {
            'partner_id':contact_id.id,
            'speciality_id': speciali_id.id,
        }
        creation =  http.request.env['medical.physician'].sudo().create(cpt)
        return http.request.render('webtemplate.indexUser',{'nom': nom })

    #-------------------------------------------
    #Enregistrement de docteur
    #-------------------------------------------
    @http.route('/enregister/partien/', auth='public', website=True)
    def function_partien(self, **kw):
        userConnect = http.request.session.uid
        users = http.request.env['res.users'].sudo().browse([userConnect])
        
        """
            déclaration de variable
            medecin_id : recuperation du médécin connecter
            medecin_detail : rechercher le médecin connecter
            message: message provenant des patient
            
        """
        medecinConnecterId = kw['medecin_id']
        medecin_detail = http.request.env['medical.physician'].sudo().browse([medecinConnecterId])
        status =    kw['status']
        message =   kw['message']
        data =      kw['date']
        date = data + ' ' + "17:57:02"
        
        if userConnect:
            userParnert = http.request.env['res.partner'].sudo().search([('email','=',str(users.login))],limit=1)

            cpt = {
                        'patient_id': userParnert.id,
                        'sex': status,
                        'critical_info': message
            }

            crationPatient =  http.request.env['medical.patient'].sudo().create(cpt)

            # add logging
            _logger.info('------------------------')
            _logger.info(userParnert.name)    
            _logger.info('------------------------')
            # add logging

            priseRendeVous = {
                            'patient_id': crationPatient.id,
                            'appointment_date': "2021-05-28 08:00:00",
                            'appointment_end': date,
                            'doctor_id': medecin_detail.id,
                        }
            rendezVous = http.request.env['medical.appointment'].sudo().create(priseRendeVous)

            return http.request.render('webtemplate.confirmation')

        else:
            nom =       kw['nom']
            prenom =    kw['prenom']
            email =     kw['email']
            
            heurs =     kw['heurs']
            phone =     kw ['phone']

            name = prenom + ' '+ nom
            is_patient = True  
            is_person = False
            
            vals = { 
                        'name' : name,
                        'phone' : phone,
                        'email': email,
                        'is_person': is_person,
                        'is_patient': is_patient,
                }

            
            
            partients_id =  http.request.env['res.partner'].sudo().create(vals)
            cpt = {
                        'patient_id': partients_id.id,
                        'sex': status,
                        'critical_info': message
            }

            medecin_detail = http.request.env['medical.physician'].sudo().browse([medecinConnecterId])
            confime =  http.request.env['medical.patient'].sudo().create(cpt)
            cpts = {
                            'patient_id': confime.id,
                            'appointment_date': "2021-05-28 08:00:00",
                            'appointment_end': date ,
                            'doctor_id': medecin_detail.id,
                        }
            rendezVous = http.request.env['medical.appointment'].sudo().create(cpts)
            return http.request.render('webtemplate.confirmation')
        

    
class academacadem(http.Controller):
    @http.route('/OpenMedecine', auth='public',website=True)
    def OpenMedecine(self, **kw):
        medecin = http.request.env['medical.physician']
        pharmacie = http.request.env['medical.pharmacie']
        pharmacies = http.request.env['medical.pharmacie']
    
        return http.request.render('webtemplate.index', {
            'medecin': medecin.sudo().search([],limit=6),
            'pharmacie': pharmacie.sudo().search([],limit=6),
        })