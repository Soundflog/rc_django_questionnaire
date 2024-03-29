# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = '_role'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = '_user'


class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    variant = models.ForeignKey('Variant', models.DO_NOTHING, blank=True, null=True)
    answered_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'answer'


class Block(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'block'


class Doctor(models.Model):
    id = models.BigAutoField(primary_key=True)
    doctor_code = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=18)
    field_user = models.ForeignKey(User, models.DO_NOTHING, db_column='_user_id')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'doctor'


class DoctorPosition(models.Model):
    doctor = models.OneToOneField(Doctor, models.DO_NOTHING, primary_key=True)  # The composite primary key (doctor_id, job_position_id) found, that is not supported. The first column is selected.
    job_position = models.ForeignKey('JobPosition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'doctor_position'
        unique_together = (('doctor', 'job_position'),)


class DoctorSpecialization(models.Model):
    job_specialization = models.OneToOneField('JobSpecialization', models.DO_NOTHING, primary_key=True)  # The composite primary key (job_specialization_id, doctor_id) found, that is not supported. The first column is selected.
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'doctor_specialization'
        unique_together = (('job_specialization', 'doctor'),)


class Exercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    video_url = models.CharField(max_length=2083)
    description = models.TextField(blank=True, null=True)
    exercise_type = models.ForeignKey('ExerciseType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercise'


class ExerciseType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'exercise_type'


class Form(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    scale = models.ForeignKey('Scale', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form'


class FormQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_question = models.ForeignKey('Question', models.DO_NOTHING, db_column='id_question')
    id_form = models.ForeignKey(Form, models.DO_NOTHING, db_column='id_form')
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_question'


class FormResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    form = models.ForeignKey(Form, models.DO_NOTHING)
    score = models.DecimalField(max_digits=100, decimal_places=2)
    creation_date = models.DateField()
    patient = models.ForeignKey('Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_result'


class Interpretation(models.Model):
    id = models.BigAutoField(primary_key=True)
    min_value = models.DecimalField(max_digits=100, decimal_places=2)
    max_value = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    scale = models.ForeignKey('Scale', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'interpretation'


class JobPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'job_position'


class JobSpecialization(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'job_specialization'


class Module(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    rehab_program = models.ForeignKey('RehabProgram', models.DO_NOTHING)
    finished_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module'


class ModuleExercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.ForeignKey(Module, models.DO_NOTHING)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING)
    block = models.ForeignKey(Block, models.DO_NOTHING)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_exercise'


class ModuleForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.ForeignKey(Module, models.DO_NOTHING)
    form = models.ForeignKey(Form, models.DO_NOTHING)
    block = models.ForeignKey(Block, models.DO_NOTHING)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_form'


class Passport(models.Model):
    id = models.BigAutoField(primary_key=True)
    series = models.CharField(max_length=4)
    number = models.CharField(max_length=6)
    issued = models.TextField()
    issued_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'passport'


class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_code = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=18)
    work_place_data = models.TextField()
    bookmark = models.TextField(blank=True, null=True)
    snils = models.CharField(max_length=11)
    polis = models.CharField(max_length=16)
    patient_status = models.ForeignKey('PatientStatus', models.DO_NOTHING)
    passport = models.OneToOneField(Passport, models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    field_user = models.ForeignKey(User, models.DO_NOTHING, db_column='_user_id')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'patient'


class PatientStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'patient_status'


class Protocol(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_final = models.BooleanField()
    rehab_result = models.TextField()
    recommendations = models.TextField()
    rehab_diagnosis = models.TextField()
    creation_date = models.DateField()
    rehab_program = models.ForeignKey('RehabProgram', models.DO_NOTHING)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'protocol'


class ProtocolFormResult(models.Model):
    protocol = models.OneToOneField(Protocol, models.DO_NOTHING, primary_key=True)  # The composite primary key (protocol_id, form_result_id) found, that is not supported. The first column is selected.
    form_result = models.ForeignKey(FormResult, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'protocol_form_result'
        unique_together = (('protocol', 'form_result'),)


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'question'


class RehabProgram(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    is_current = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_form = models.ForeignKey(Form, models.DO_NOTHING)
    end_form = models.ForeignKey(Form, models.DO_NOTHING, related_name='rehabprogram_end_form_set')

    class Meta:
        managed = False
        db_table = 'rehab_program'


class RehabProgramLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    rehab_program = models.ForeignKey(RehabProgram, models.DO_NOTHING)
    who_changed = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='who_changed')
    change_date = models.DateField()
    change = models.TextField()
    operation = models.TextField()

    class Meta:
        managed = False
        db_table = 'rehab_program_log'


class Scale(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scale'


class UserRole(models.Model):
    field_user = models.OneToOneField(User, models.DO_NOTHING, db_column='_user_id', primary_key=True)  # Field renamed because it started with '_'. The composite primary key (_user_id, _role_id) found, that is not supported. The first column is selected.
    field_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='_role_id')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('field_user', 'field_role'),)


class Variant(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    score = models.DecimalField(max_digits=100, decimal_places=2)
    question = models.ForeignKey(Question, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'variant'
