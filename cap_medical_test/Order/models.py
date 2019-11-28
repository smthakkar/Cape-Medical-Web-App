# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import date
from datetime import datetime
from django.db import models
from django.contrib.auth.models import Group,User
from myauth.models import SubGroup

class Teamsettings1(models.Model):
    main_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sub_group = models.OneToOneField(SubGroup, on_delete=models.CASCADE)
    sharewith = models.ManyToManyField(User,
                                       verbose_name='Assign To',
                                       limit_choices_to={'is_active': True, 'is_staff': False},
                                       related_name='share_withs'
                                       )
    columnsinclusions = models.TextField(blank=False, null=False, default='sales_order_number')
    description = models.TextField(max_length=255,blank=True, null=True, default=None)
    statusvalidation = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)

    def _get_status(self):
        pass


# class Salesorders(models.Model):
#     sales_order_number = models.TextField(db_column='Sales Order Number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_date_created = models.TextField(db_column='Sales Order Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_created_by = models.TextField(db_column='Sales Order Created by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_branch_office = models.TextField(db_column='Sales Order Branch Office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_status = models.TextField(db_column='Sales Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_manual_hold = models.TextField(db_column='Sales Order Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_location = models.TextField(db_column='Sales Order Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_discount_pct = models.TextField(db_column='Sales Order Discount Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_po_number = models.TextField(db_column='Sales Order PO Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_purchase_order_number = models.TextField(db_column='Sales Order Purchase Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_reference = models.TextField(db_column='Sales Order Reference', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_previous_billing = models.TextField(db_column='Sales Order Previous Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_next_billing = models.TextField(db_column='Sales Order Next Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_user_1 = models.TextField(db_column='Sales Order User 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_user_2 = models.TextField(db_column='Sales Order User 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_user_3 = models.TextField(db_column='Sales Order User 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_user_4 = models.TextField(db_column='Sales Order User 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_confirm_date = models.TextField(db_column='Sales Order Confirm Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_confirmed_by = models.TextField(db_column='Sales Order Confirmed By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_last_printed = models.TextField(db_column='Sales Order Last Printed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_date = models.TextField(db_column='Sales Order Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_branch_group = models.TextField(db_column='Sales Order Branch Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_delivery_note = models.TextField(db_column='Sales Order Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_note = models.TextField(db_column='Sales Order Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_classification = models.TextField(db_column='Sales Order Classification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_type = models.TextField(db_column='Sales Order Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_pod_order_status = models.TextField(db_column='Sales Order POD Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_manual_hold_reason = models.TextField(db_column='Sales Order Manual Hold Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_facility = models.TextField(db_column='Sales Order Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_facility_group = models.TextField(db_column='Sales Order Facility Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_retail_pos_order = models.TextField(db_column='Sales Order Retail POS Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_prior_system_key = models.TextField(db_column='Sales Order Prior System Key', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_height = models.TextField(db_column='Sales Order Height', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_weight = models.TextField(db_column='Sales Order Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field1 = models.TextField(db_column='Sales Order Custom Fields Field1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field2 = models.TextField(db_column='Sales Order Custom Fields Field2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field3 = models.TextField(db_column='Sales Order Custom Fields Field3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field4 = models.TextField(db_column='Sales Order Custom Fields Field4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field5 = models.TextField(db_column='Sales Order Custom Fields Field5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field6 = models.TextField(db_column='Sales Order Custom Fields Field6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field7 = models.TextField(db_column='Sales Order Custom Fields Field7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field8 = models.TextField(db_column='Sales Order Custom Fields Field8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field9 = models.TextField(db_column='Sales Order Custom Fields Field9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field10 = models.TextField(db_column='Sales Order Custom Fields Field10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field11 = models.TextField(db_column='Sales Order Custom Fields Field11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field12 = models.TextField(db_column='Sales Order Custom Fields Field12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field13 = models.TextField(db_column='Sales Order Custom Fields Field13', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field14 = models.TextField(db_column='Sales Order Custom Fields Field14', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field15 = models.TextField(db_column='Sales Order Custom Fields Field15', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field16 = models.TextField(db_column='Sales Order Custom Fields Field16', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field17 = models.TextField(db_column='Sales Order Custom Fields Field17', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field18 = models.TextField(db_column='Sales Order Custom Fields Field18', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field19 = models.TextField(db_column='Sales Order Custom Fields Field19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field20 = models.TextField(db_column='Sales Order Custom Fields Field20', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field21 = models.TextField(db_column='Sales Order Custom Fields Field21', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field22 = models.TextField(db_column='Sales Order Custom Fields Field22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field23 = models.TextField(db_column='Sales Order Custom Fields Field23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field24 = models.TextField(db_column='Sales Order Custom Fields Field24', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_custom_fields_field25 = models.TextField(db_column='Sales Order Custom Fields Field25', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_hold_cmn_not_logged = models.TextField(db_column='Sales Order Hold CMN Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_hold_cmn_expired = models.TextField(db_column='Sales Order Hold CMN Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_hold_par_not_logged = models.TextField(db_column='Sales Order Hold PAR Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_hold_par_expired = models.TextField(db_column='Sales Order Hold PAR Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_hold_manual_hold = models.TextField(db_column='Sales Order Hold Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_type = models.TextField(db_column='Sales Order Stop Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_pending_pickup = models.TextField(db_column='Sales Order Stop Pending Pickup', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_multiple_pricing_options = models.TextField(db_column='Sales Order Stop Multiple Pricing Options', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_policy_expired = models.TextField(db_column='Sales Order Stop Policy Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_no_pricing_found = models.TextField(db_column='Sales Order Stop No Pricing Found', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_policy_changed = models.TextField(db_column='Sales Order Stop Policy Changed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_manual_stop_date = models.TextField(db_column='Sales Order Stop Manual Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_automatic_eligibility_check = models.TextField(db_column='Sales Order Stop Automatic Eligibility Check', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_stop_ineligible_policy = models.TextField(db_column='Sales Order Stop Ineligible Policy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     work_in_progress_wip_state = models.TextField(db_column='Work In Progress WIP State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     work_in_progress_assigned_to = models.TextField(db_column='Work In Progress Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     work_in_progress_date_needed = models.TextField(db_column='Work In Progress Date Needed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     work_in_progress_completed = models.TextField(db_column='Work In Progress Completed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     work_in_progress_wip_days_in_state = models.TextField(db_column='Work In Progress WIP Days In State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_scheduled_date = models.TextField(db_column='Delivery Scheduled date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_scheduled_time = models.TextField(db_column='Delivery Scheduled time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_actual_date = models.TextField(db_column='Delivery Actual date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_actual_time = models.TextField(db_column='Delivery Actual time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_address_1 = models.TextField(db_column='Delivery Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_address_2 = models.TextField(db_column='Delivery Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_address_3 = models.TextField(db_column='Delivery Address 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_city = models.TextField(db_column='Delivery City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_state = models.TextField(db_column='Delivery State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_county = models.TextField(db_column='Delivery County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_country = models.TextField(db_column='Delivery Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_postal_code = models.TextField(db_column='Delivery Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_phone = models.TextField(db_column='Delivery Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_fax = models.TextField(db_column='Delivery Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_tax_zone = models.TextField(db_column='Delivery Tax Zone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_tax_rate = models.TextField(db_column='Delivery Tax Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_technician = models.TextField(db_column='Delivery Technician', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_bright_ship_status = models.TextField(db_column='Delivery Bright Ship Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_bright_ship_carrier = models.TextField(db_column='Delivery Bright Ship Carrier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_bright_ship_method = models.TextField(db_column='Delivery Bright Ship Method', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_bright_ship_tracking_numbers = models.TextField(db_column='Delivery Bright Ship Tracking Numbers', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_fulfillment_vendor = models.TextField(db_column='Delivery Fulfillment Vendor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_account_number = models.TextField(db_column='Delivery Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_ship_by = models.TextField(db_column='Delivery Ship By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_status = models.TextField(db_column='Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     delivery_status_date = models.TextField(db_column='Delivery Status Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     place_of_service_pos = models.TextField(db_column='Place of Service POS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     place_of_service_date_of_admission = models.TextField(db_column='Place of Service Date of Admission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     place_of_service_date_of_discharge = models.TextField(db_column='Place of Service Date of Discharge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_last_name = models.TextField(db_column='Patient Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_first_name = models.TextField(db_column='Patient First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_middle_name = models.TextField(db_column='Patient Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_email_address = models.TextField(db_column='Patient Email Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_address_1 = models.TextField(db_column='Patient Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_address_2 = models.TextField(db_column='Patient Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_city = models.TextField(db_column='Patient City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_state = models.TextField(db_column='Patient State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_postal_code = models.TextField(db_column='Patient Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_phone = models.TextField(db_column='Patient Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_mobile = models.TextField(db_column='Patient Mobile', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_fax = models.TextField(db_column='Patient Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_id = models.TextField(db_column='Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_account_number = models.TextField(db_column='Patient Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_date_created = models.TextField(db_column='Patient Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_dob = models.TextField(db_column='Patient DOB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_dod = models.TextField(db_column='Patient DOD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_ssn = models.TextField(db_column='Patient SSN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_delivery_note = models.TextField(db_column='Patient Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_branch = models.TextField(db_column='Patient Branch', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_full_name = models.TextField(db_column='Patient Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_gender = models.TextField(db_column='Patient Gender', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_customer_type = models.TextField(db_column='Patient Customer Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_facility = models.TextField(db_column='Patient Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_security_group = models.TextField(db_column='Patient Security Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_restricted_access = models.TextField(db_column='Patient Restricted Access', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_bpc_auto_pay_status = models.TextField(db_column='Patient BPC Auto PAY Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_bpc_e_delivery_status = models.TextField(db_column='Patient BPC e Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_bpc_payment_plan = models.TextField(db_column='Patient BPC Payment Plan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_bpc_information = models.TextField(db_column='Patient BPC Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     patient_patient_hub_status = models.TextField(db_column='Patient Patient Hub Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_last_name = models.TextField(db_column='Ordering Doctor Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_first_name = models.TextField(db_column='Ordering Doctor First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_address_1 = models.TextField(db_column='Ordering Doctor Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_address_2 = models.TextField(db_column='Ordering Doctor Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_city = models.TextField(db_column='Ordering Doctor City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_state = models.TextField(db_column='Ordering Doctor State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_postal_code = models.TextField(db_column='Ordering Doctor Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_phone = models.TextField(db_column='Ordering Doctor Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_fax = models.TextField(db_column='Ordering Doctor Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_fax_to = models.TextField(db_column='Ordering Doctor Fax To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_pecos_certify_status = models.TextField(db_column='Ordering Doctor PECOS Certify Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_full_name = models.TextField(db_column='Ordering Doctor Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_group = models.TextField(db_column='Ordering Doctor Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ordering_doctor_npi = models.TextField(db_column='Ordering Doctor NPI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sleep_therapy_solution = models.TextField(db_column='Sleep Therapy Solution', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sleep_therapy_setup_date = models.TextField(db_column='Sleep Therapy Setup Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sleep_therapy_registration_status = models.TextField(db_column='Sleep Therapy Registration Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sleep_therapy_compliance_date = models.TextField(db_column='Sleep Therapy Compliance Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sleep_therapy_compliance_status = models.TextField(db_column='Sleep Therapy Compliance Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sleep_therapy_external_patient_id = models.TextField(db_column='Sleep Therapy External Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_code_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_9_description_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_code_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sales_order_diagnosis_codes_dx_icd_10_description_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     workers_compensation_injury_related_to_employment = models.TextField(db_column='Workers Compensation Injury Related to Employment', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     workers_compensation_injury_related_to_auto_accident = models.TextField(db_column='Workers Compensation Injury Related to Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     workers_compensation_state_of_auto_accident = models.TextField(db_column='Workers Compensation State of Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     workers_compensation_injury_related_to_other_accident = models.TextField(db_column='Workers Compensation Injury Related to Other Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     workers_compensation_onset_date = models.TextField(db_column='Workers Compensation Onset Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_type = models.TextField(db_column='Referral Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_name = models.TextField(db_column='Referral Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_address_1 = models.TextField(db_column='Referral Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_address_2 = models.TextField(db_column='Referral Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_city = models.TextField(db_column='Referral City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_state = models.TextField(db_column='Referral State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_zip = models.TextField(db_column='Referral Zip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_phone = models.TextField(db_column='Referral Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_fax = models.TextField(db_column='Referral Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_contact_name = models.TextField(db_column='Referral Contact Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_doctor_group = models.TextField(db_column='Referral Doctor Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referral_facility_group = models.TextField(db_column='Referral Facility Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_type = models.TextField(db_column='Referring Provider Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_name = models.TextField(db_column='Referring Provider Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_address_1 = models.TextField(db_column='Referring Provider Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_address_2 = models.TextField(db_column='Referring Provider Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_city = models.TextField(db_column='Referring Provider City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_state = models.TextField(db_column='Referring Provider State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_zip = models.TextField(db_column='Referring Provider Zip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_phone = models.TextField(db_column='Referring Provider Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_fax = models.TextField(db_column='Referring Provider Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     referring_provider_npi = models.TextField(db_column='Referring Provider NPI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_payor = models.TextField(db_column='Insurance Pri Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_payor_id = models.TextField(db_column='Insurance Pri Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_insurance_name = models.TextField(db_column='Insurance Pri Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_policy_field = models.TextField(db_column='Insurance Pri Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     insurance_pri_group_field = models.TextField(db_column='Insurance Pri Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     insurance_pri_policy_effective_date = models.TextField(db_column='Insurance Pri Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_policy_verified = models.TextField(db_column='Insurance Pri Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_pay_pct = models.TextField(db_column='Insurance Pri Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_include_this_payor_level_on_so = models.TextField(db_column='Insurance Pri Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Pri Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_automatically_generate_claims = models.TextField(db_column='Insurance Pri Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_box_10d = models.TextField(db_column='Insurance Pri Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_box_19 = models.TextField(db_column='Insurance Pri Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_box_24ia = models.TextField(db_column='Insurance Pri Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_box_24ja = models.TextField(db_column='Insurance Pri Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_box_24jb = models.TextField(db_column='Insurance Pri Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_include_box_24jb = models.TextField(db_column='Insurance Pri Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri_plan_type = models.TextField(db_column='Insurance Pri Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_payor = models.TextField(db_column='Insurance Sec Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_payor_id = models.TextField(db_column='Insurance Sec Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_insurance_name = models.TextField(db_column='Insurance Sec Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_policy_field = models.TextField(db_column='Insurance Sec Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     insurance_sec_group_field = models.TextField(db_column='Insurance Sec Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     insurance_sec_policy_effective_date = models.TextField(db_column='Insurance Sec Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_policy_verified = models.TextField(db_column='Insurance Sec Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_pay_pct = models.TextField(db_column='Insurance Sec Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_include_this_payor_level_on_so = models.TextField(db_column='Insurance Sec Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Sec Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_automatically_generate_claims = models.TextField(db_column='Insurance Sec Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_box_10d = models.TextField(db_column='Insurance Sec Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_box_19 = models.TextField(db_column='Insurance Sec Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_box_24ia = models.TextField(db_column='Insurance Sec Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_box_24ja = models.TextField(db_column='Insurance Sec Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_box_24jb = models.TextField(db_column='Insurance Sec Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_plan_type = models.TextField(db_column='Insurance Sec Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec_include_box_24jb = models.TextField(db_column='Insurance Sec Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_payor = models.TextField(db_column='Insurance Ter Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_payor_id = models.TextField(db_column='Insurance Ter Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_insurance_name = models.TextField(db_column='Insurance Ter Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_policy_field = models.TextField(db_column='Insurance Ter Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     insurance_ter_group_field = models.TextField(db_column='Insurance Ter Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     insurance_ter_policy_effective_date = models.TextField(db_column='Insurance Ter Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_policy_verified = models.TextField(db_column='Insurance Ter Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_pay_pct = models.TextField(db_column='Insurance Ter Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_include_this_payor_level_on_so = models.TextField(db_column='Insurance Ter Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Ter Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_automatically_generate_claims = models.TextField(db_column='Insurance Ter Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_box_10d = models.TextField(db_column='Insurance Ter Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_box_19 = models.TextField(db_column='Insurance Ter Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_box_24ia = models.TextField(db_column='Insurance Ter Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_box_24ja = models.TextField(db_column='Insurance Ter Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_box_24jb = models.TextField(db_column='Insurance Ter Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_include_box_24jb = models.TextField(db_column='Insurance Ter Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter_plan_type = models.TextField(db_column='Insurance Ter Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_insurance_verified = models.TextField(db_column='Insurance Insurance Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_insurance_coverage_verified = models.TextField(db_column='Insurance Insurance Coverage Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_pri = models.TextField(db_column='Insurance Pri', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_sec = models.TextField(db_column='Insurance Sec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_ter = models.TextField(db_column='Insurance Ter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_claim_note_type = models.TextField(db_column='Insurance Claim Note Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     insurance_claim_note = models.TextField(db_column='Insurance Claim Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     marketing_rep_last_name = models.TextField(db_column='Marketing Rep Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     marketing_rep_first_name = models.TextField(db_column='Marketing Rep First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     marketing_rep_full_name = models.TextField(db_column='Marketing Rep Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     practitioner_last_name = models.TextField(db_column='Practitioner Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     practitioner_first_name = models.TextField(db_column='Practitioner First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     practitioner_middle_name = models.TextField(db_column='Practitioner Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rendering_provider_type = models.TextField(db_column='Rendering Provider Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rendering_provider_doctor = models.TextField(db_column='Rendering Provider Doctor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rendering_provider_facility = models.TextField(db_column='Rendering Provider Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_testing_id = models.TextField(db_column='Diagnostic Testing Testing ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_date_ordered = models.TextField(db_column='Diagnostic Testing Date Ordered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_test_group = models.TextField(db_column='Diagnostic Testing Test Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_test_name = models.TextField(db_column='Diagnostic Testing Test Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_testing_partner = models.TextField(db_column='Diagnostic Testing Testing Partner', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_testing_status = models.TextField(db_column='Diagnostic Testing Testing Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     diagnostic_testing_testing_completed_dated = models.TextField(db_column='Diagnostic Testing Testing Completed Dated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rule = models.ForeignKey(CapemedicalTeamsettings, on_delete=models.CASCADE, blank=True, null=True)
#
#     class Meta:
#         # managed = False
#         db_table = 'SalesOrders'


class SalesOrder_new(models.Model):
    sales_order_number = models.IntegerField(default=None, primary_key=True)
    sales_order_date_created = models.DateTimeField(blank=True, null=True)
    sales_order_created_by = models.TextField(blank=True,max_length=70, null=True)
    sales_order_branch_office = models.TextField(max_length=60, blank=True, null=True)
    sales_order_status = models.TextField(blank=True, null=True)
    sales_order_manual_hold = models.BooleanField(blank=True, null=True)
    sales_order_location = models.TextField(max_length=50, blank=True, null=True)
    sales_order_discount_pct = models.IntegerField(blank=True, null=True)
    sales_order_po_number = models.TextField(max_length=20, blank=True, null=True)
    sales_order_purchase_order_number = models.TextField(max_length=10, blank=True, null=True)
    sales_order_reference = models.TextField(max_length=40, blank=True, null=True)
    sales_order_previous_billing = models.DateTimeField(blank=True, null=True)
    sales_order_next_billing = models.DateTimeField(blank=True, null=True)
    sales_order_user_1 = models.TextField(max_length=30, blank=True, null=True)
    sales_order_user_2 = models.TextField(max_length=30, blank=True,null=True)
    sales_order_user_3 = models.TextField(max_length=30, blank=True, null=True)
    sales_order_user_4 = models.TextField(max_length=30, blank=True, null=True)
    sales_order_confirm_date = models.DateTimeField(blank=True, null=True, default=None)
    sales_order_confirmed_by = models.TextField(max_length=70, blank=True, null=True)
    sales_order_last_printed = models.DateTimeField(blank=True, null=True)
    sales_order_stop_date = models.DateTimeField(blank=True, null=True)
    sales_order_branch_group = models.TextField(max_length=30, blank=True, null=True)
    sales_order_delivery_note = models.TextField(blank=True, null=True)
    sales_order_note = models.TextField(blank=True, null=True)
    sales_order_classification = models.TextField(max_length=40, blank=True, null=True)
    sales_order_type = models.TextField(max_length=20, blank=True, null=True)
    sales_order_pod_order_status = models.TextField(max_length=20, blank=True, null=True)
    sales_order_manual_hold_reason = models.TextField(max_length=20, blank=True, null=True)
    sales_order_facility = models.TextField(max_length=20, blank=True, null=True)
    sales_order_facility_group = models.TextField(max_length=20, blank=True, null=True)
    sales_order_retail_pos_order = models.BooleanField(blank=True, null=True)
    sales_order_prior_system_key = models.TextField(max_length=40, blank=True, null=True)
    sales_order_height = models.TextField(max_length=10, blank=True, null=True)
    sales_order_weight = models.TextField(max_length=10, blank=True, null=True)
    sales_order_custom_fields_field1 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field2 = models.TextField(max_length=255, blank=True,null=True)
    sales_order_custom_fields_field3 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field4 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field5 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field6 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field7 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field8 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field9 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field10 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field11 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field12 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field13 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field14 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field15 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field16 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field17 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field18 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field19 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field20 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field21 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field22 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field23 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field24 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_custom_fields_field25 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_hold_cmn_not_logged = models.BooleanField(blank=True, null=True)
    sales_order_hold_cmn_expired = models.BooleanField(blank=True, null=True)
    sales_order_hold_par_not_logged = models.BooleanField(blank=True, null=True)
    sales_order_hold_par_expired = models.BooleanField(blank=True, null=True)
    sales_order_hold_manual_hold = models.BooleanField(blank=True, null=True)
    sales_order_stop_type = models.TextField(max_length=15, blank=True, null=True)
    sales_order_stop_pending_pickup = models.BooleanField(blank=True, null=True)
    sales_order_stop_multiple_pricing_options = models.BooleanField(blank=True, null=True)
    sales_order_stop_policy_expired = models.BooleanField(blank=True, null=True)
    sales_order_stop_no_pricing_found = models.BooleanField(blank=True, null=True)
    sales_order_stop_policy_changed = models.BooleanField(blank=True, null=True)
    sales_order_stop_manual_stop_date = models.BooleanField(blank=True, null=True)
    sales_order_stop_automatic_eligibility_check = models.BooleanField(blank=True, null=True)
    sales_order_stop_ineligible_policy = models.BooleanField(blank=True, null=True)
    work_in_progress_wip_state = models.TextField(max_length=35, blank=True, null=True)
    work_in_progress_assigned_to = models.TextField(max_length=60, blank=True, null=True)
    work_in_progress_date_needed = models.DateTimeField(blank=True, null=True)
    work_in_progress_completed = models.BooleanField(blank=True, null=True)
    work_in_progress_wip_days_in_state = models.IntegerField(blank=True, null=True)
    delivery_scheduled_date = models.DateTimeField(blank=True, null=True)
    delivery_scheduled_time = models.TimeField(blank=True, null=True)
    delivery_actual_date = models.DateTimeField(blank=True, null=True)
    delivery_actual_time = models.TimeField(blank=True, null=True)
    delivery_address_1 = models.TextField(max_length=255, blank=True, null=True)
    delivery_address_2 = models.TextField(max_length=255, blank=True, null=True)
    delivery_address_3 = models.TextField(max_length=255, blank=True, null=True)
    delivery_city = models.TextField(max_length=30, blank=True, null=True)
    delivery_state = models.TextField(max_length=30, blank=True, null=True)
    delivery_county = models.TextField(max_length=30, blank=True, null=True)
    delivery_country = models.TextField(max_length=30, blank=True, null=True)
    delivery_postal_code = models.TextField(max_length=10, blank=True, null=True)
    delivery_phone = models.TextField(max_length=15, blank=True, null=True)
    delivery_fax = models.TextField(max_length=15, blank=True, null=True)
    delivery_tax_zone = models.TextField(max_length=30, blank=True, null=True)
    delivery_tax_rate = models.TextField(max_length=15, blank=True, null=True)
    delivery_technician = models.TextField(max_length=40, blank=True, null=True)
    delivery_bright_ship_status = models.TextField(max_length=20, blank=True, null=True)
    delivery_bright_ship_carrier = models.TextField(max_length=30, blank=True, null=True)
    delivery_bright_ship_method = models.TextField(max_length=20, blank=True, null=True)
    delivery_bright_ship_tracking_numbers = models.TextField(max_length=50, blank=True, null=True)
    delivery_fulfillment_vendor = models.TextField(max_length=25, blank=True, null=True)
    delivery_account_number = models.TextField(max_length=10, blank=True, null=True)
    delivery_ship_by = models.TextField(max_length=20, blank=True, null=True)
    delivery_status = models.TextField(max_length=30, blank=True, null=True)
    delivery_status_date = models.DateTimeField(blank=True, null=True)
    place_of_service_pos = models.TextField(max_length=30, blank=True, null=True)
    place_of_service_date_of_admission = models.DateTimeField(blank=True, null=True)
    place_of_service_date_of_discharge = models.DateTimeField(blank=True, null=True)
    patient_last_name = models.TextField(max_length=25, blank=True, null=True)
    patient_first_name = models.TextField(max_length=25, blank=True, null=True)
    patient_middle_name = models.TextField(max_length=20, blank=True, null=True)
    patient_email_address = models.TextField(max_length=64, blank=True, null=True)
    patient_address_1 = models.TextField(max_length=255, blank=True, null=True)
    patient_address_2 = models.TextField(max_length=255, blank=True, null=True)
    patient_city = models.TextField(max_length=30, blank=True, null=True)
    patient_state = models.TextField(max_length=20, blank=True, null=True)
    patient_postal_code = models.TextField(max_length=10, blank=True, null=True)
    patient_phone = models.TextField(max_length=20, blank=True, null=True)
    patient_mobile = models.TextField(max_length=20, blank=True, null=True)
    patient_fax = models.TextField(max_length=20, blank=True, null=True)
    patient_id = models.TextField(max_length=12, blank=True, null=True)
    patient_account_number = models.TextField(max_length=12, blank=True, null=True)
    patient_date_created = models.DateTimeField(blank=True, null=True)
    patient_dob = models.DateField(blank=True, null=True)
    patient_dod = models.DateField(blank=True, null=True)
    patient_ssn = models.TextField(max_length=12, blank=True, null=True)
    patient_delivery_note = models.TextField(blank=True, null=True)
    patient_branch = models.TextField(max_length=40, blank=True, null=True)
    patient_full_name = models.TextField(max_length=100, blank=True, null=True)
    patient_gender = models.TextField(max_length=10, blank=True, null=True)
    patient_customer_type = models.TextField(max_length=20, blank=True, null=True)
    patient_facility = models.TextField(max_length=20, blank=True, null=True)
    patient_security_group = models.TextField(max_length=20, blank=True, null=True)
    patient_restricted_access = models.BooleanField(blank=True, null=True)
    patient_bpc_auto_pay_status = models.TextField(max_length=20, blank=True, null=True)
    patient_bpc_e_delivery_status = models.TextField(max_length=20, blank=True, null=True)
    patient_bpc_payment_plan = models.TextField(max_length=20, blank=True, null=True)
    patient_bpc_information = models.TextField(blank=True, null=True)
    patient_patient_hub_status = models.TextField(max_length=20, blank=True, null=True)
    ordering_doctor_last_name = models.TextField(max_length=30, blank=True, null=True)
    ordering_doctor_first_name = models.TextField(max_length=30, blank=True, null=True)
    ordering_doctor_address_1 = models.TextField(max_length=255, blank=True, null=True)
    ordering_doctor_address_2 = models.TextField(max_length=255, blank=True, null=True)
    ordering_doctor_city = models.TextField(max_length=30, blank=True, null=True)
    ordering_doctor_state = models.TextField(max_length=20, blank=True, null=True)
    ordering_doctor_postal_code = models.TextField(max_length=10, blank=True, null=True)
    ordering_doctor_phone = models.TextField(max_length=23, blank=True, null=True)
    ordering_doctor_fax = models.TextField(max_length=25, blank=True, null=True)
    ordering_doctor_fax_to = models.TextField(max_length=25, blank=True, null=True)
    ordering_doctor_pecos_certify_status = models.TextField(max_length=20, blank=True, null=True)
    ordering_doctor_full_name = models.TextField(max_length=40, blank=True, null=True)
    ordering_doctor_group = models.TextField(max_length=20, blank=True, null=True)
    ordering_doctor_npi = models.TextField(max_length=20, blank=True, null=True)
    sleep_therapy_solution = models.TextField(max_length=25, blank=True, null=True)
    sleep_therapy_setup_date = models.DateTimeField(blank=True, null=True)
    sleep_therapy_registration_status = models.TextField(max_length=20, blank=True, null=True)
    sleep_therapy_compliance_date = models.DateTimeField(blank=True, null=True)
    sleep_therapy_compliance_status = models.TextField(max_length=15, blank=True, null=True)
    sleep_therapy_external_patient_id = models.TextField(max_length=50, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field01 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field01 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field02 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field02 = models.TextField(max_length=255, blank=True,null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field03 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field03 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field04 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field04 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field05 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field05 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field06 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field06 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field07 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field07 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field08 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field08 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field09 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field09 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field10 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field10 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field11 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field11 = models.TextField(max_length=255,blank=True,null=True)
    sales_order_diagnosis_codes_dx_icd_9_code_field12 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_9_description_field12 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field01 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field01 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field02 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field02 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field03 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field03 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field04 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field05 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field04 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field05 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field06 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field06 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field07 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field07 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field08 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field08 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field09 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field09 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field10 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field10 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field11 = models.TextField(blank=True,null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field11 = models.TextField(max_length=255, blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_code_field12 = models.TextField(blank=True, null=True)
    sales_order_diagnosis_codes_dx_icd_10_description_field12 = models.TextField(max_length=255, blank=True, null=True)
    workers_compensation_injury_related_to_employment = models.BooleanField(blank=True, null=True)
    workers_compensation_injury_related_to_auto_accident = models.BooleanField(blank=True, null=True)
    workers_compensation_state_of_auto_accident = models.TextField(blank=True, null=True)
    workers_compensation_injury_related_to_other_accident = models.BooleanField(blank=True, null=True)
    workers_compensation_onset_date = models.DateTimeField(blank=True, null=True)
    referral_type = models.TextField(max_length=30, blank=True, null=True)
    referral_name = models.TextField(max_length=40, blank=True, null=True)
    referral_address_1 = models.TextField(max_length=255, blank=True, null=True)
    referral_address_2 = models.TextField(max_length=255, blank=True, null=True)
    referral_city = models.TextField(max_length=25, blank=True, null=True)
    referral_state = models.TextField(max_length=25, blank=True, null=True)
    referral_zip = models.TextField(max_length=10, blank=True, null=True)
    referral_phone = models.TextField(max_length=15, blank=True, null=True)
    referral_fax = models.TextField(max_length=15, blank=True, null=True)
    referral_contact_name = models.TextField(max_length=20, blank=True, null=True)
    referral_doctor_group = models.TextField(max_length=25, blank=True, null=True)
    referral_facility_group = models.TextField(max_length=25,blank=True, null=True)
    referring_provider_type = models.TextField(max_length=25, blank=True, null=True)
    referring_provider_name = models.TextField(max_length=40, blank=True, null=True)
    referring_provider_address_1 = models.TextField(max_length=255, blank=True, null=True)
    referring_provider_address_2 = models.TextField(max_length=255, blank=True, null=True)
    referring_provider_city = models.TextField(max_length=30, blank=True, null=True)
    referring_provider_state = models.TextField(max_length=25, blank=True, null=True)
    referring_provider_zip = models.TextField(max_length=10, blank=True, null=True)
    referring_provider_phone = models.TextField(max_length=25, blank=True, null=True)
    referring_provider_fax = models.TextField(max_length=25, blank=True, null=True)
    referring_provider_npi = models.TextField(max_length=25, blank=True, null=True)
    insurance_pri_payor = models.TextField(max_length=40, blank=True, null=True)
    insurance_pri_payor_id = models.TextField(max_length=12, blank=True, null=True)
    insurance_pri_insurance_name = models.TextField(max_length=30, blank=True, null=True)
    insurance_pri_policy_field = models.TextField(max_length=20, blank=True, null=True)
    insurance_pri_group_field = models.TextField(max_length=35, blank=True, null=True)
    insurance_pri_policy_effective_date = models.DateTimeField(blank=True, null=True)
    insurance_pri_policy_verified = models.BooleanField(blank=True, null=True)
    insurance_pri_pay_pct = models.TextField(max_length=5, blank=True, null=True)
    insurance_pri_include_this_payor_level_on_so = models.BooleanField(blank=True,null=True)
    insurance_pri_wait_for_previous_payor_before_billing = models.BooleanField(blank=True, null=True)
    insurance_pri_automatically_generate_claims = models.BooleanField(blank=True, null=True)
    insurance_pri_box_10d = models.TextField(max_length=255, blank=True, null=True)
    insurance_pri_box_19 = models.TextField(blank=True, null=True)
    insurance_pri_box_24ia = models.TextField(blank=True, null=True)
    insurance_pri_box_24ja = models.TextField(blank=True, null=True)
    insurance_pri_box_24jb = models.TextField(blank=True, null=True)
    insurance_pri_include_box_24jb = models.BooleanField(blank=True, null=True)
    insurance_pri_plan_type = models.TextField(max_length=35, blank=True, null=True)
    insurance_sec_payor = models.TextField(max_length=40, blank=True, null=True)
    insurance_sec_payor_id = models.TextField(max_length=10, blank=True, null=True)
    insurance_sec_insurance_name = models.TextField(max_length=30,blank=True, null=True)
    insurance_sec_policy_field = models.TextField(max_length=30, blank=True, null=True)
    insurance_sec_group_field = models.TextField(max_length=25, blank=True, null=True)
    insurance_sec_policy_effective_date = models.DateTimeField(blank=True, null=True)
    insurance_sec_policy_verified = models.BooleanField(blank=True, null=True)
    insurance_sec_pay_pct = models.TextField(max_length=10, blank=True, null=True)
    insurance_sec_include_this_payor_level_on_so = models.BooleanField(blank=True, null=True)
    insurance_sec_wait_for_previous_payor_before_billing = models.BooleanField(blank=True, null=True)
    insurance_sec_automatically_generate_claims = models.BooleanField(blank=True, null=True)
    insurance_sec_box_10d = models.TextField(blank=True,null=True)
    insurance_sec_box_19 = models.TextField(blank=True, null=True)
    insurance_sec_box_24ia = models.TextField(blank=True,null=True)
    insurance_sec_box_24ja = models.TextField(blank=True, null=True)
    insurance_sec_box_24jb = models.TextField(blank=True, null=True)
    insurance_sec_plan_type = models.TextField(max_length=40, blank=True, null=True)
    insurance_sec_include_box_24jb = models.BooleanField(blank=True, null=True)
    insurance_ter_payor = models.TextField(max_length=30, blank=True, null=True)
    insurance_ter_payor_id = models.TextField(max_length=25, blank=True, null=True)
    insurance_ter_insurance_name = models.TextField(max_length=30, blank=True, null=True)
    insurance_ter_policy_field = models.TextField(max_length=25, blank=True, null=True)
    insurance_ter_group_field = models.TextField(max_length=30, blank=True, null=True)
    insurance_ter_policy_effective_date = models.DateTimeField(blank=True, null=True)
    insurance_ter_policy_verified = models.BooleanField(blank=True, null=True)
    insurance_ter_pay_pct = models.TextField(max_length=10, blank=True, null=True)
    insurance_ter_include_this_payor_level_on_so = models.BooleanField(blank=True, null=True)
    insurance_ter_wait_for_previous_payor_before_billing = models.BooleanField(blank=True, null=True)
    insurance_ter_automatically_generate_claims = models.BooleanField(blank=True,null=True)
    insurance_ter_box_10d = models.TextField(blank=True, null=True)
    insurance_ter_box_19 = models.TextField(blank=True,null=True)
    insurance_ter_box_24ia = models.TextField(blank=True, null=True)
    insurance_ter_box_24ja = models.TextField(blank=True, null=True)
    insurance_ter_box_24jb = models.TextField(blank=True, null=True)
    insurance_ter_include_box_24jb = models.BooleanField(blank=True, null=True)
    insurance_ter_plan_type = models.TextField(max_length=30, blank=True, null=True)
    insurance_insurance_verified = models.BooleanField(blank=True, null=True)
    insurance_insurance_coverage_verified = models.BooleanField(blank=True, null=True)
    insurance_pri = models.TextField(max_length=30, blank=True, null=True)
    insurance_sec = models.TextField(max_length=50, blank=True, null=True)
    insurance_ter = models.TextField(max_length=70, blank=True, null=True)
    insurance_claim_note_type = models.TextField(max_length=30, blank=True, null=True)
    insurance_claim_note = models.TextField(blank=True,null=True)
    marketing_rep_last_name = models.TextField(max_length=30, blank=True, null=True)
    marketing_rep_first_name = models.TextField(max_length=30, blank=True, null=True)
    marketing_rep_full_name = models.TextField(max_length=50, blank=True, null=True)
    practitioner_last_name = models.TextField(max_length=30, blank=True, null=True)
    practitioner_first_name = models.TextField(max_length=30, blank=True, null=True)
    practitioner_middle_name = models.TextField(max_length=30, blank=True, null=True)
    rendering_provider_type = models.TextField(max_length=25, blank=True, null=True)
    rendering_provider_doctor = models.TextField(max_length=50, blank=True, null=True)
    rendering_provider_facility = models.TextField(max_length=255, blank=True, null=True)
    diagnostic_testing_testing_id = models.TextField(blank=True,null=True)
    diagnostic_testing_date_ordered = models.TextField(blank=True, null=True)
    diagnostic_testing_test_group = models.TextField(blank=True, null=True)
    diagnostic_testing_test_name = models.TextField(blank=True, null=True)
    diagnostic_testing_testing_partner = models.TextField(blank=True, null=True)
    diagnostic_testing_testing_status = models.TextField(blank=True,null=True)
    diagnostic_testing_testing_completed_dated = models.DateTimeField(blank=True,null=True)
    rule = models.ForeignKey(Teamsettings1, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_order_numbers')

    class Meta:
        get_latest_by = 'sales_order_date_created'




class sales_order_assign(models.Model):
    STT_CHOICE = [(1,'1'),(2,'2')]
    sales_order_number = models.OneToOneField(SalesOrder_new, on_delete=models.CASCADE, primary_key=True)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(default=None, blank=True, null=True, max_length=30, choices=STT_CHOICE)

    # class Meta:
    #     permissions = (
    #         ('can_change_assign_to', 'Can change assign to'),
    #         ('can_change_status', 'Can change status'),
    #     )


class assign_history(models.Model):
    sales_order = models.IntegerField(default=None, blank=True, null=True)
    assigned_by = models.CharField(max_length=45)
    assigned_to = models.CharField(max_length=45, blank=True, null=True, default=None)
    status = models.CharField(max_length=30, blank=True, null=True, default=None)
    assign_time = models.DateTimeField(auto_now=True)