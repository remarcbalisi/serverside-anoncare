import json
from app import *
from models import DBconn
from flask.ext.httpauth import HTTPBasicAuth
from flask import request
import re
import hashlib
from flask import jsonify
from spcalls import SPcalls

spcalls = SPcalls()


def store_patient(school_id, data):

    school_id_exists = spcalls.spcall('school_id_exists', (school_id,), True)

    def names_empty(fname, mname, lname):
        if fname is '' or mname is '' or lname is '':
            return True
        else:
            return False

    def bio_empty(age, sex, height, weight, date_of_birth):
        if age is None or sex is '' or height is '' or weight is None or date_of_birth is '':
            return True
        else:
            return False

    def extra_info_empty(dept_id, ptnt_id, civil_status, name_of_guardian, home_addr):
        if dept_id is None or ptnt_id is None or civil_status is '' or name_of_guardian is '' or home_addr is '':
            return True
        else:
            return False

    def valid_patient_info(patient):
        fname = patient['fname']
        mname = patient['mname']
        lname = patient['lname']
        age = patient['age']
        sex = patient['sex']
        dept_id = patient['department_id']
        ptnt_id = patient['patient_type_id']
        height = patient['height']
        weight = patient['weight']
        date_of_birth = patient['date_of_birth']
        civil_status = patient['civil_status']
        guardian = patient['name_of_guardian']
        home_addr = patient['home_address']

        empty_names = names_empty(fname, mname, lname)
        empty_bio = bio_empty(age, sex, height, weight, date_of_birth)
        empty_extra_info = extra_info_empty(dept_id, ptnt_id, civil_status, guardian, home_addr)

        empty_fields = empty_names and empty_bio and empty_extra_info
        print "empty_fields", empty_fields

        if empty_fields is False:

            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def valid_patient_history(history):

        smoking = history['smoking']
        allergies = history['allergies']
        alcohol = history['alcohol']
        medications_taken = history['medications_taken']
        drugs = history['drugs']

        empty_fields = smoking is '' or allergies is '' or alcohol is '' or medications_taken is '' or drugs is ''

        if empty_fields is False:

            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def valid_pulmonary(pulmonary):
        cough = pulmonary['cough']
        dyspnea = pulmonary['dyspnea']
        hemoptysis = pulmonary['hemoptysis']
        tb_exposure = pulmonary['tb_exposure']

        empty_fields = cough is '' or dyspnea is '' or hemoptysis is '' or tb_exposure is ''

        if empty_fields is False:
            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def valid_gut(gut):
        frequency = gut['frequency']
        flank_plan = gut['flank_plan']
        discharge = gut['discharge']
        dysuria = gut['dysuria']
        nocturia = gut['nocturia']
        dec_urine_amount = gut['dec_urine_amount']

        empty_fields = frequency is '' or flank_plan is '' or discharge is '' or dysuria is '' or nocturia is '' or dec_urine_amount is ''

        if empty_fields is False:
            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def valid_illness(illness):

        asthma = illness['asthma']
        ptb = illness['ptb']
        heart_problem = illness['heart_problem']
        hepa_a_b = illness['hepatitis_a_b']
        chicken_pox = illness['chicken_pox']
        mumps = illness['mumps']
        typhoid_fever = illness['typhoid_fever']

        empty_fields = asthma is '' or ptb is '' or heart_problem is '' or hepa_a_b is '' or \
                       chicken_pox is '' or mumps is '' or typhoid_fever is ''

        if empty_fields is False:
            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def valid_cardiac(cardiac):

        chest_pain = cardiac['chest_pain']
        palpitations = cardiac['palpitations']
        pedal_edema = cardiac['pedal_edema']
        orthopnea = cardiac['orthopnea']
        nocturnal_dyspnea = cardiac['nocturnal_dyspnea']

        empty_fields = chest_pain is '' or palpitations is '' or pedal_edema is '' or orthopnea is '' or nocturnal_dyspnea is ''

        if empty_fields is False:
            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def valid_neurologic(neurologic):
        
        headache = neurologic['headache']
        seizure = neurologic['seizure']
        dizziness = neurologic['dizziness']
        loss_of_consciousness = neurologic['loss_of_consciousness']

        empty_fields = headache is '' or seizure is '' or dizziness is '' or loss_of_consciousness is ''

        if empty_fields is False:
            if school_id_exists[0][0] is 'true':
                return False
            else:
                return True

        else:
            return True

    def store_patient_info():

        store_new_patient = spcalls.spcall('new_store_patient',
                                            (school_id,data['fname'], data['mname'], data['lname'],
                                             data['age'], data['sex'], data['department_id'], data['patient_type_id'],
                                                data['height'], data['weight'], data['date_of_birth'],
                                                data['civil_status'], data['name_of_guardian'], data['home_address']), True)

        return store_new_patient[0][0]

    def store_patient_history():

        store_new_history = spcalls.spcall('new_patient_history',
                                           (school_id, data['smoking'], data['allergies'],
                                            data['alcohol'], data['medications_taken'],
                                            data['drugs']), True)

        return store_new_history[0][0]

    def store_pulmonary():

        store_new_pulmonary = spcalls.spcall('new_pulmonary',
                                             (school_id, data['cough'], data['dyspnea'],
                                              data['hemoptysis'], data['tb_exposure']), True)

        return store_new_pulmonary[0][0]


    def store_gut():

        store_new_gut = spcalls.spcall('new_gut',
                                      (school_id, data['frequency'], data['flank_plan'], data['discharge'],
                                        data['dysuria'], data['nocturia'], data['dec_urine_amount']), True)

        return store_new_gut[0][0]


    def store_illness():

        store_new_illness = spcalls.spcall('new_illness',
                                           (school_id, data['asthma'], data['ptb'], data['heart_problem'],
                                            data['hepatitis_a_b'], data['chicken_pox'],
                                            data['mumps'], data['typhoid_fever']), True)

        return store_new_illness[0][0]


    def store_cardiac():

        store_new_cardiac = spcalls.spcall('new_cardiac',
                                           (school_id, data['chest_pain'], data['palpitations'], data['pedal_edema'],
                                            data['orthopnea'], data['nocturnal_dyspnea']), True)

        return store_new_cardiac[0][0]


    def store_neurologic():

        store_new_neurologic = spcalls.spcall('new_neurologic',
                                              (school_id, data['headache'], data['seizure'],
                                               data['dizziness'], data['loss_of_consciousness']), True)

        return store_new_neurologic[0][0]


    valid_data = valid_patient_info(data) and valid_patient_history(data) and valid_pulmonary(data) and valid_gut(data) and \
                 valid_illness(data) and valid_cardiac(data) and valid_neurologic(data)


    print "valid_data", valid_data

    if valid_data is True:

        store_patient_info()
        store_patient_history()
        store_pulmonary()
        store_gut()
        store_illness()
        store_cardiac()
        store_neurologic()

        return jsonify({'status': 'OK', 'message': 'Successfully added new patient'})

    else:

        return jsonify({'status': 'FAILED', 'message': 'Failed to add gut'})

