# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CapemedicalMaster(models.Model):
    file = models.TextField(db_column='File', blank=True, null=True)  # Field name made lowercase.
    sheet = models.TextField(db_column='Sheet', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    salesordernumber = models.BigAutoField(db_column='SalesOrderNumber', primary_key=True)  # Field name made lowercase.
    salesorderdatecreated = models.TextField(db_column='SalesOrderDateCreated', blank=True, null=True)  # Field name made lowercase.
    salesordercreatedby = models.TextField(db_column='SalesOrderCreatedby', blank=True, null=True)  # Field name made lowercase.
    salesorderbranchoffice = models.TextField(db_column='SalesOrderBranchOffice', blank=True, null=True)  # Field name made lowercase.
    salesorderstatus = models.TextField(db_column='SalesOrderStatus', blank=True, null=True)  # Field name made lowercase.
    salesordermanualhold = models.TextField(db_column='SalesOrderManualHold', blank=True, null=True)  # Field name made lowercase.
    salesorderlocation = models.TextField(db_column='SalesOrderLocation', blank=True, null=True)  # Field name made lowercase.
    salesorderdiscountpct = models.TextField(db_column='SalesOrderDiscountPct', blank=True, null=True)  # Field name made lowercase.
    salesorderponumber = models.TextField(db_column='SalesOrderPONumber', blank=True, null=True)  # Field name made lowercase.
    salesorderreference = models.TextField(db_column='SalesOrderReference', blank=True, null=True)  # Field name made lowercase.
    salesorderpreviousbilling = models.TextField(db_column='SalesOrderPreviousBilling', blank=True, null=True)  # Field name made lowercase.
    salesordernextbilling = models.TextField(db_column='SalesOrderNextBilling', blank=True, null=True)  # Field name made lowercase.
    salesorderdeliverynote = models.TextField(db_column='SalesOrderDeliveryNote', blank=True, null=True)  # Field name made lowercase.
    salesordernote = models.TextField(db_column='SalesOrderNote', blank=True, null=True)  # Field name made lowercase.
    salesorderconfirmdate = models.TextField(db_column='SalesOrderConfirmDate', blank=True, null=True)  # Field name made lowercase.
    salesorderconfirmedby = models.TextField(db_column='SalesOrderConfirmedBy', blank=True, null=True)  # Field name made lowercase.
    salesorderlastprintdate = models.TextField(db_column='SalesOrderLastPrintDate', blank=True, null=True)  # Field name made lowercase.
    salesorderstopdate = models.TextField(db_column='SalesOrderStopDate', blank=True, null=True)  # Field name made lowercase.
    salesorderbranchgroup = models.TextField(db_column='SalesOrderBranchGroup', blank=True, null=True)  # Field name made lowercase.
    salesorderclassification = models.TextField(db_column='SalesOrderClassification', blank=True, null=True)  # Field name made lowercase.
    salesordertype = models.TextField(db_column='SalesOrderType', blank=True, null=True)  # Field name made lowercase.
    salesorderpodorderstatus = models.TextField(db_column='SalesOrderPODOrderStatus', blank=True, null=True)  # Field name made lowercase.
    salesordermanualholdreason = models.TextField(db_column='SalesOrderManualHoldReason', blank=True, null=True)  # Field name made lowercase.
    salesorderretailposorder = models.TextField(db_column='SalesOrderRetailPOSOrder', blank=True, null=True)  # Field name made lowercase.
    salesorderholdcmnnotlogged = models.TextField(db_column='SalesOrderHoldCMNNotLogged', blank=True, null=True)  # Field name made lowercase.
    salesorderholdcmnexpired = models.TextField(db_column='SalesOrderHoldCMNExpired', blank=True, null=True)  # Field name made lowercase.
    salesorderholdparnotlogged = models.TextField(db_column='SalesOrderHoldPARNotLogged', blank=True, null=True)  # Field name made lowercase.
    salesorderholdparexpired = models.TextField(db_column='SalesOrderHoldPARExpired', blank=True, null=True)  # Field name made lowercase.
    salesorderholdmanualhold = models.TextField(db_column='SalesOrderHoldManualHold', blank=True, null=True)  # Field name made lowercase.
    salesorderstoptype = models.TextField(db_column='SalesOrderStopType', blank=True, null=True)  # Field name made lowercase.
    salesorderstoppendingpickup = models.TextField(db_column='SalesOrderStopPendingPickup', blank=True, null=True)  # Field name made lowercase.
    salesorderstopmultiplepricingoptions = models.TextField(db_column='SalesOrderStopMultiplePricingOptions', blank=True, null=True)  # Field name made lowercase.
    salesorderstoppolicyexpired = models.TextField(db_column='SalesOrderStopPolicyExpired', blank=True, null=True)  # Field name made lowercase.
    salesorderstopnopricingfound = models.TextField(db_column='SalesOrderStopNoPricingFound', blank=True, null=True)  # Field name made lowercase.
    salesorderstoppolicychanged = models.TextField(db_column='SalesOrderStopPolicyChanged', blank=True, null=True)  # Field name made lowercase.
    salesorderstopmanualstopdate = models.TextField(db_column='SalesOrderStopManualStopDate', blank=True, null=True)  # Field name made lowercase.
    workinprogresswipstate = models.TextField(db_column='WorkInProgressWIPState', blank=True, null=True)  # Field name made lowercase.
    workinprogressassignedto = models.TextField(db_column='WorkInProgressAssignedTo', blank=True, null=True)  # Field name made lowercase.
    workinprogressdateneeded = models.TextField(db_column='WorkInProgressDateNeeded', blank=True, null=True)  # Field name made lowercase.
    workinprogresscompleted = models.TextField(db_column='WorkInProgressCompleted', blank=True, null=True)  # Field name made lowercase.
    workinprogresswipdaysinstate = models.TextField(db_column='WorkInProgressWIPDaysInState', blank=True, null=True)  # Field name made lowercase.
    deliveryscheduleddate = models.TextField(db_column='DeliveryScheduleddate', blank=True, null=True)  # Field name made lowercase.
    deliveryscheduledtime = models.TextField(db_column='DeliveryScheduledtime', blank=True, null=True)  # Field name made lowercase.
    deliveryactualdate = models.TextField(db_column='DeliveryActualdate', blank=True, null=True)  # Field name made lowercase.
    deliveryactualtime = models.TextField(db_column='DeliveryActualtime', blank=True, null=True)  # Field name made lowercase.
    deliveryaddress1 = models.TextField(db_column='DeliveryAddress1', blank=True, null=True)  # Field name made lowercase.
    deliveryaddress2 = models.TextField(db_column='DeliveryAddress2', blank=True, null=True)  # Field name made lowercase.
    deliverycity = models.TextField(db_column='DeliveryCity', blank=True, null=True)  # Field name made lowercase.
    deliverystate = models.TextField(db_column='DeliveryState', blank=True, null=True)  # Field name made lowercase.
    deliverycounty = models.TextField(db_column='DeliveryCounty', blank=True, null=True)  # Field name made lowercase.
    deliverycountry = models.TextField(db_column='DeliveryCountry', blank=True, null=True)  # Field name made lowercase.
    deliverypostalcode = models.TextField(db_column='DeliveryPostalCode', blank=True, null=True)  # Field name made lowercase.
    deliveryphone = models.TextField(db_column='DeliveryPhone', blank=True, null=True)  # Field name made lowercase.
    deliveryfax = models.TextField(db_column='DeliveryFax', blank=True, null=True)  # Field name made lowercase.
    deliverytaxzone = models.TextField(db_column='DeliveryTaxZone', blank=True, null=True)  # Field name made lowercase.
    deliverytaxrate = models.TextField(db_column='DeliveryTaxRate', blank=True, null=True)  # Field name made lowercase.
    deliverytechnician = models.TextField(db_column='DeliveryTechnician', blank=True, null=True)  # Field name made lowercase.
    deliverybrightshipstatus = models.TextField(db_column='DeliveryBrightSHIPStatus', blank=True, null=True)  # Field name made lowercase.
    deliverybrightshipcarrier = models.TextField(db_column='DeliveryBrightSHIPCarrier', blank=True, null=True)  # Field name made lowercase.
    deliverybrightshipmethod = models.TextField(db_column='DeliveryBrightSHIPMethod', blank=True, null=True)  # Field name made lowercase.
    deliveryfulfillmentvendor = models.TextField(db_column='DeliveryFulfillmentVendor', blank=True, null=True)  # Field name made lowercase.
    deliveryaccountnumber = models.TextField(db_column='DeliveryAccountNumber', blank=True, null=True)  # Field name made lowercase.
    deliveryshipby = models.TextField(db_column='DeliveryShipBy', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.TextField(db_column='DeliveryStatus', blank=True, null=True)  # Field name made lowercase.
    deliverystatusdate = models.TextField(db_column='DeliveryStatusDate', blank=True, null=True)  # Field name made lowercase.
    placeofservicepos = models.TextField(db_column='PlaceofServicePOS', blank=True, null=True)  # Field name made lowercase.
    placeofservicedateofadmission = models.TextField(db_column='PlaceofServiceDateofAdmission', blank=True, null=True)  # Field name made lowercase.
    placeofservicedateofdischarge = models.TextField(db_column='PlaceofServiceDateofDischarge', blank=True, null=True)  # Field name made lowercase.
    patientid = models.TextField(db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    sleeptherapysolution = models.TextField(db_column='SleepTherapySolution', blank=True, null=True)  # Field name made lowercase.
    sleeptherapysetupdate = models.TextField(db_column='SleepTherapySetupDate', blank=True, null=True)  # Field name made lowercase.
    sleeptherapyregistrationstatus = models.TextField(db_column='SleepTherapyRegistrationStatus', blank=True, null=True)  # Field name made lowercase.
    sleeptherapycompliancedate = models.TextField(db_column='SleepTherapyComplianceDate', blank=True, null=True)  # Field name made lowercase.
    sleeptherapycompliancestatus = models.TextField(db_column='SleepTherapyComplianceStatus', blank=True, null=True)  # Field name made lowercase.
    sleeptherapyexternalpatientid = models.TextField(db_column='SleepTherapyExternalPatientID', blank=True, null=True)  # Field name made lowercase.
    salesorderdiagnosiscodesdxicd_9code_01 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Code#01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9description_01 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Description#01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9code_02 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Code#02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9description_02 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Description#02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9code_03 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Code#03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9description_03 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Description#03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9code_04 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Code#04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9description_04 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Description#04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9code_05 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Code#05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salesorderdiagnosiscodesdxicd_9description_05 = models.TextField(db_column='SalesOrderDiagnosisCodesDxICD-9Description#05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workerscompensationinjuryrelatedtoemployment = models.TextField(db_column='WorkersCompensationInjuryRelatedtoEmployment', blank=True, null=True)  # Field name made lowercase.
    workerscompensationinjuryrelatedtoautoaccident = models.TextField(db_column='WorkersCompensationInjuryRelatedtoAutoAccident', blank=True, null=True)  # Field name made lowercase.
    workerscompensationstateofautoaccident = models.TextField(db_column='WorkersCompensationStateofAutoAccident', blank=True, null=True)  # Field name made lowercase.
    workerscompensationinjuryrelatedtootheraccident = models.TextField(db_column='WorkersCompensationInjuryRelatedtoOtherAccident', blank=True, null=True)  # Field name made lowercase.
    workerscompensationonsetdate = models.TextField(db_column='WorkersCompensationOnsetDate', blank=True, null=True)  # Field name made lowercase.
    insurancepripayor = models.TextField(db_column='InsurancePriPayor', blank=True, null=True)  # Field name made lowercase.
    insurancepripayorid = models.TextField(db_column='InsurancePriPayorID', blank=True, null=True)  # Field name made lowercase.
    insurancepriinsurancename = models.TextField(db_column='InsurancePriInsuranceName', blank=True, null=True)  # Field name made lowercase.
    insurancepripolicy_field = models.TextField(db_column='InsurancePriPolicy#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insuranceprigroup_field = models.TextField(db_column='InsurancePriGroup#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurancepripolicyeffectivedate = models.TextField(db_column='InsurancePriPolicyEffectiveDate', blank=True, null=True)  # Field name made lowercase.
    insurancepripolicyverified = models.TextField(db_column='InsurancePriPolicyVerified', blank=True, null=True)  # Field name made lowercase.
    insurancepripaypct = models.TextField(db_column='InsurancePriPayPct', blank=True, null=True)  # Field name made lowercase.
    insurancepriincludethispayorlevelonso = models.TextField(db_column='InsurancePriIncludethispayorlevelonSO', blank=True, null=True)  # Field name made lowercase.
    insurancepriwaitforpreviouspayorbeforebilling = models.TextField(db_column='InsurancePriWaitforpreviouspayorbeforebilling', blank=True, null=True)  # Field name made lowercase.
    insurancepriautomaticallygenerateclaims = models.TextField(db_column='InsurancePriAutomaticallygenerateclaims', blank=True, null=True)  # Field name made lowercase.
    insurancepribox10d = models.TextField(db_column='InsurancePriBox10D', blank=True, null=True)  # Field name made lowercase.
    insurancepribox19 = models.TextField(db_column='InsurancePriBox19', blank=True, null=True)  # Field name made lowercase.
    insurancepribox24ia = models.TextField(db_column='InsurancePriBox24Ia', blank=True, null=True)  # Field name made lowercase.
    insurancepribox24ja = models.TextField(db_column='InsurancePriBox24Ja', blank=True, null=True)  # Field name made lowercase.
    insurancepribox24jb = models.TextField(db_column='InsurancePriBox24Jb', blank=True, null=True)  # Field name made lowercase.
    insurancepriincludebox24jb = models.TextField(db_column='InsurancePriIncludeBox24Jb', blank=True, null=True)  # Field name made lowercase.
    insurancepriplantype = models.TextField(db_column='InsurancePriPlanType', blank=True, null=True)  # Field name made lowercase.
    insurancesecpayor = models.TextField(db_column='InsuranceSecPayor', blank=True, null=True)  # Field name made lowercase.
    insurancesecpayorid = models.TextField(db_column='InsuranceSecPayorID', blank=True, null=True)  # Field name made lowercase.
    insurancesecinsurancename = models.TextField(db_column='InsuranceSecInsuranceName', blank=True, null=True)  # Field name made lowercase.
    insurancesecpolicy_field = models.TextField(db_column='InsuranceSecPolicy#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurancesecgroup_field = models.TextField(db_column='InsuranceSecGroup#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurancesecpolicyeffectivedate = models.TextField(db_column='InsuranceSecPolicyEffectiveDate', blank=True, null=True)  # Field name made lowercase.
    insurancesecpolicyverified = models.TextField(db_column='InsuranceSecPolicyVerified', blank=True, null=True)  # Field name made lowercase.
    insurancesecpaypct = models.TextField(db_column='InsuranceSecPayPct', blank=True, null=True)  # Field name made lowercase.
    insurancesecincludethispayorlevelonso = models.TextField(db_column='InsuranceSecIncludethispayorlevelonSO', blank=True, null=True)  # Field name made lowercase.
    insurancesecwaitforpreviouspayorbeforebilling = models.TextField(db_column='InsuranceSecWaitforpreviouspayorbeforebilling', blank=True, null=True)  # Field name made lowercase.
    insurancesecautomaticallygenerateclaims = models.TextField(db_column='InsuranceSecAutomaticallygenerateclaims', blank=True, null=True)  # Field name made lowercase.
    insurancesecbox10d = models.TextField(db_column='InsuranceSecBox10D', blank=True, null=True)  # Field name made lowercase.
    insurancesecbox19 = models.TextField(db_column='InsuranceSecBox19', blank=True, null=True)  # Field name made lowercase.
    insurancesecbox24ia = models.TextField(db_column='InsuranceSecBox24Ia', blank=True, null=True)  # Field name made lowercase.
    insurancesecbox24ja = models.TextField(db_column='InsuranceSecBox24Ja', blank=True, null=True)  # Field name made lowercase.
    insurancesecbox24jb = models.TextField(db_column='InsuranceSecBox24Jb', blank=True, null=True)  # Field name made lowercase.
    insurancesecincludebox24jb = models.TextField(db_column='InsuranceSecIncludeBox24Jb', blank=True, null=True)  # Field name made lowercase.
    insurancesecplantype = models.TextField(db_column='InsuranceSecPlanType', blank=True, null=True)  # Field name made lowercase.
    insuranceterpayor = models.TextField(db_column='InsuranceTerPayor', blank=True, null=True)  # Field name made lowercase.
    insuranceterpayorid = models.TextField(db_column='InsuranceTerPayorID', blank=True, null=True)  # Field name made lowercase.
    insuranceterinsurancename = models.TextField(db_column='InsuranceTerInsuranceName', blank=True, null=True)  # Field name made lowercase.
    insuranceterpolicy_field = models.TextField(db_column='InsuranceTerPolicy#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurancetergroup_field = models.TextField(db_column='InsuranceTerGroup#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insuranceterpolicyeffectivedate = models.TextField(db_column='InsuranceTerPolicyEffectiveDate', blank=True, null=True)  # Field name made lowercase.
    insuranceterpolicyverified = models.TextField(db_column='InsuranceTerPolicyVerified', blank=True, null=True)  # Field name made lowercase.
    insuranceterpaypct = models.TextField(db_column='InsuranceTerPayPct', blank=True, null=True)  # Field name made lowercase.
    insuranceterincludethispayorlevelonso = models.TextField(db_column='InsuranceTerIncludethispayorlevelonSO', blank=True, null=True)  # Field name made lowercase.
    insuranceterwaitforpreviouspayorbeforebilling = models.TextField(db_column='InsuranceTerWaitforpreviouspayorbeforebilling', blank=True, null=True)  # Field name made lowercase.
    insuranceterautomaticallygenerateclaims = models.TextField(db_column='InsuranceTerAutomaticallygenerateclaims', blank=True, null=True)  # Field name made lowercase.
    insuranceterbox10d = models.TextField(db_column='InsuranceTerBox10D', blank=True, null=True)  # Field name made lowercase.
    insuranceterbox19 = models.TextField(db_column='InsuranceTerBox19', blank=True, null=True)  # Field name made lowercase.
    insuranceterbox24ia = models.TextField(db_column='InsuranceTerBox24Ia', blank=True, null=True)  # Field name made lowercase.
    insuranceterbox24ja = models.TextField(db_column='InsuranceTerBox24Ja', blank=True, null=True)  # Field name made lowercase.
    insuranceterbox24jb = models.TextField(db_column='InsuranceTerBox24Jb', blank=True, null=True)  # Field name made lowercase.
    insuranceterincludebox24jb = models.TextField(db_column='InsuranceTerIncludeBox24Jb', blank=True, null=True)  # Field name made lowercase.
    insuranceterplantype = models.TextField(db_column='InsuranceTerPlanType', blank=True, null=True)  # Field name made lowercase.
    insuranceinsuranceverified = models.TextField(db_column='InsuranceInsuranceVerified', blank=True, null=True)  # Field name made lowercase.
    insuranceinsurancecoverageverified = models.TextField(db_column='InsuranceInsuranceCoverageVerified', blank=True, null=True)  # Field name made lowercase.
    insurancepri = models.TextField(db_column='InsurancePri', blank=True, null=True)  # Field name made lowercase.
    insurancesec = models.TextField(db_column='InsuranceSec', blank=True, null=True)  # Field name made lowercase.
    insuranceter = models.TextField(db_column='InsuranceTer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CapeMedical_Master'


class CapemedicalTeamsettings(models.Model):
    file = models.TextField(db_column='File', blank=True, null=True)  # Field name made lowercase.
    sharewith = models.TextField(db_column='Sharewith', blank=True, null=True)  # Field name made lowercase.
    sheet = models.TextField(db_column='Sheet', blank=True, null=True)  # Field name made lowercase.
    columnsinclusions = models.TextField(db_column='ColumnsInclusions', blank=True, null=True)  # Field name made lowercase.
    statusvalidation = models.TextField(db_column='StatusValidation', blank=True, null=True)  # Field name made lowercase.
    salesorderclassification = models.TextField(db_column='SalesOrderClassification', blank=True, null=True)  # Field name made lowercase.
    workinprogresswipstate = models.TextField(db_column='WorkInProgressWIPState', blank=True, null=True)  # Field name made lowercase.
    workinprogresswipdaysinstate = models.TextField(db_column='WorkInProgressWIPDaysInState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CapeMedical_TeamSettings'


class Patientnotedetails(models.Model):
    note_note_id = models.TextField(db_column='Note Note Id', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_type = models.TextField(db_column='Note Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_note_reason = models.TextField(db_column='Note Note Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_status = models.TextField(db_column='Note Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_severity = models.TextField(db_column='Note Severity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_assigned_to = models.TextField(db_column='Note Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_date_created = models.TextField(db_column='Note Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_actual_date = models.TextField(db_column='Note Actual Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_date_needed = models.TextField(db_column='Note Date Needed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_date_complete = models.TextField(db_column='Note Date Complete', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_created_by = models.TextField(db_column='Note Created By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_user1 = models.TextField(db_column='Note User1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_user2 = models.TextField(db_column='Note User2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_state = models.TextField(db_column='Note State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_note_deactivated = models.TextField(db_column='Note Note Deactivated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_subject = models.TextField(db_column='Note Subject', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_description = models.TextField(db_column='Note Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_acknowledgement_required = models.TextField(db_column='Note Acknowledgement Required', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_comment_created_by = models.TextField(db_column='Note Comment Created By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_comment_date_created = models.TextField(db_column='Note Comment Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_comment_actual_date = models.TextField(db_column='Note Comment Actual Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_comment_comment_text = models.TextField(db_column='Note Comment Comment Text', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.TextField(db_column='Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'PatientNoteDetails'


class Reportstodownload(models.Model):
    reportname = models.TextField(db_column='ReportName', blank=True, null=True)  # Field name made lowercase.
    filterby = models.TextField(db_column='FilterBy', blank=True, null=True)  # Field name made lowercase.
    pythondateformat = models.TextField(db_column='PythonDateFormat', blank=True, null=True)  # Field name made lowercase.
    importtodb = models.TextField(db_column='ImportToDB', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    maindatecolumn = models.TextField(db_column='MainDateColumn', blank=True, null=True)  # Field name made lowercase.
    mappingtable = models.TextField(db_column='MappingTable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportsToDownload'


class Salesordercustomfieldmapping(models.Model):
    brightree_column_name = models.TextField(db_column='Brightree_Column_Name', blank=True, null=True)  # Field name made lowercase.
    database_column_name = models.TextField(db_column='Database_Column_Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesOrderCustomFieldMapping'


class Salesorderdetails(models.Model):
    sales_order_number = models.TextField(db_column='Sales Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_date_created = models.TextField(db_column='Sales Order Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_created_by = models.TextField(db_column='Sales Order Created by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_branch_office = models.TextField(db_column='Sales Order Branch Office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_status = models.TextField(db_column='Sales Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_manual_hold = models.TextField(db_column='Sales Order Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_location = models.TextField(db_column='Sales Order Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_discount_pct = models.TextField(db_column='Sales Order Discount Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_po_number = models.TextField(db_column='Sales Order PO Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_reference = models.TextField(db_column='Sales Order Reference', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_previous_billing = models.TextField(db_column='Sales Order Previous Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_next_billing = models.TextField(db_column='Sales Order Next Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_delivery_note = models.TextField(db_column='Sales Order Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_note = models.TextField(db_column='Sales Order Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_confirm_date = models.TextField(db_column='Sales Order Confirm Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_confirmed_by = models.TextField(db_column='Sales Order Confirmed By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_last_print_date = models.TextField(db_column='Sales Order Last Print Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_date = models.TextField(db_column='Sales Order Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_branch_group = models.TextField(db_column='Sales Order Branch Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_classification = models.TextField(db_column='Sales Order Classification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_type = models.TextField(db_column='Sales Order Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_pod_order_status = models.TextField(db_column='Sales Order POD Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_manual_hold_reason = models.TextField(db_column='Sales Order Manual Hold Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_retail_pos_order = models.TextField(db_column='Sales Order Retail POS Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field1 = models.TextField(db_column='Sales Order Custom Fields Field1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field2 = models.TextField(db_column='Sales Order Custom Fields Field2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field3 = models.TextField(db_column='Sales Order Custom Fields Field3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field4 = models.TextField(db_column='Sales Order Custom Fields Field4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field5 = models.TextField(db_column='Sales Order Custom Fields Field5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field6 = models.TextField(db_column='Sales Order Custom Fields Field6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field7 = models.TextField(db_column='Sales Order Custom Fields Field7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field8 = models.TextField(db_column='Sales Order Custom Fields Field8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field9 = models.TextField(db_column='Sales Order Custom Fields Field9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field10 = models.TextField(db_column='Sales Order Custom Fields Field10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field11 = models.TextField(db_column='Sales Order Custom Fields Field11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field12 = models.TextField(db_column='Sales Order Custom Fields Field12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field13 = models.TextField(db_column='Sales Order Custom Fields Field13', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field14 = models.TextField(db_column='Sales Order Custom Fields Field14', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field15 = models.TextField(db_column='Sales Order Custom Fields Field15', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field16 = models.TextField(db_column='Sales Order Custom Fields Field16', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field17 = models.TextField(db_column='Sales Order Custom Fields Field17', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field18 = models.TextField(db_column='Sales Order Custom Fields Field18', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field19 = models.TextField(db_column='Sales Order Custom Fields Field19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field20 = models.TextField(db_column='Sales Order Custom Fields Field20', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field21 = models.TextField(db_column='Sales Order Custom Fields Field21', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field22 = models.TextField(db_column='Sales Order Custom Fields Field22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field23 = models.TextField(db_column='Sales Order Custom Fields Field23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field24 = models.TextField(db_column='Sales Order Custom Fields Field24', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field25 = models.TextField(db_column='Sales Order Custom Fields Field25', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_cmn_not_logged = models.TextField(db_column='Sales Order Hold CMN Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_cmn_expired = models.TextField(db_column='Sales Order Hold CMN Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_par_not_logged = models.TextField(db_column='Sales Order Hold PAR Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_par_expired = models.TextField(db_column='Sales Order Hold PAR Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_manual_hold = models.TextField(db_column='Sales Order Hold Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_type = models.TextField(db_column='Sales Order Stop Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_pending_pickup = models.TextField(db_column='Sales Order Stop Pending Pickup', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_multiple_pricing_options = models.TextField(db_column='Sales Order Stop Multiple Pricing Options', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_policy_expired = models.TextField(db_column='Sales Order Stop Policy Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_no_pricing_found = models.TextField(db_column='Sales Order Stop No Pricing Found', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_policy_changed = models.TextField(db_column='Sales Order Stop Policy Changed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_manual_stop_date = models.TextField(db_column='Sales Order Stop Manual Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_wip_state = models.TextField(db_column='Work In Progress WIP State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_assigned_to = models.TextField(db_column='Work In Progress Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_date_needed = models.TextField(db_column='Work In Progress Date Needed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_completed = models.TextField(db_column='Work In Progress Completed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_wip_days_in_state = models.TextField(db_column='Work In Progress WIP Days In State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_scheduled_date = models.TextField(db_column='Delivery Scheduled date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_scheduled_time = models.TextField(db_column='Delivery Scheduled time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_actual_date = models.TextField(db_column='Delivery Actual date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_actual_time = models.TextField(db_column='Delivery Actual time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_1 = models.TextField(db_column='Delivery Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_2 = models.TextField(db_column='Delivery Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_city = models.TextField(db_column='Delivery City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_state = models.TextField(db_column='Delivery State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_county = models.TextField(db_column='Delivery County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_country = models.TextField(db_column='Delivery Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_postal_code = models.TextField(db_column='Delivery Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_phone = models.TextField(db_column='Delivery Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_fax = models.TextField(db_column='Delivery Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_tax_zone = models.TextField(db_column='Delivery Tax Zone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_tax_rate = models.TextField(db_column='Delivery Tax Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_technician = models.TextField(db_column='Delivery Technician', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_status = models.TextField(db_column='Delivery Bright SHIP Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_carrier = models.TextField(db_column='Delivery Bright SHIP Carrier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_method = models.TextField(db_column='Delivery Bright SHIP Method', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_fulfillment_vendor = models.TextField(db_column='Delivery Fulfillment Vendor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_account_number = models.TextField(db_column='Delivery Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_ship_by = models.TextField(db_column='Delivery Ship By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_status = models.TextField(db_column='Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_status_date = models.TextField(db_column='Delivery Status Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_pos = models.TextField(db_column='Place of Service POS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_date_of_admission = models.TextField(db_column='Place of Service Date of Admission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_date_of_discharge = models.TextField(db_column='Place of Service Date of Discharge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.TextField(db_column='Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.TextField(db_column='Patient Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.TextField(db_column='Patient First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_mobile = models.TextField(db_column='Patient Mobile', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_key = models.TextField(db_column='Patient Key', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_full_name = models.TextField(db_column='Ordering Doctor Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_facility = models.TextField(db_column='Ordering Doctor Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_solution = models.TextField(db_column='Sleep Therapy Solution', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_setup_date = models.TextField(db_column='Sleep Therapy Setup Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_registration_status = models.TextField(db_column='Sleep Therapy Registration Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_compliance_date = models.TextField(db_column='Sleep Therapy Compliance Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_compliance_status = models.TextField(db_column='Sleep Therapy Compliance Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_external_patient_id = models.TextField(db_column='Sleep Therapy External Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_employment = models.TextField(db_column='Workers Compensation Injury Related to Employment', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_auto_accident = models.TextField(db_column='Workers Compensation Injury Related to Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_state_of_auto_accident = models.TextField(db_column='Workers Compensation State of Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_other_accident = models.TextField(db_column='Workers Compensation Injury Related to Other Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_onset_date = models.TextField(db_column='Workers Compensation Onset Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_payor = models.TextField(db_column='Insurance Pri Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_payor_id = models.TextField(db_column='Insurance Pri Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_insurance_name = models.TextField(db_column='Insurance Pri Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_policy_field = models.TextField(db_column='Insurance Pri Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_pri_group_field = models.TextField(db_column='Insurance Pri Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_pri_policy_effective_date = models.TextField(db_column='Insurance Pri Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_policy_verified = models.TextField(db_column='Insurance Pri Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_pay_pct = models.TextField(db_column='Insurance Pri Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_include_this_payor_level_on_so = models.TextField(db_column='Insurance Pri Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Pri Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_automatically_generate_claims = models.TextField(db_column='Insurance Pri Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_10d = models.TextField(db_column='Insurance Pri Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_19 = models.TextField(db_column='Insurance Pri Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24ia = models.TextField(db_column='Insurance Pri Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24ja = models.TextField(db_column='Insurance Pri Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24jb = models.TextField(db_column='Insurance Pri Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_include_box_24jb = models.TextField(db_column='Insurance Pri Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_plan_type = models.TextField(db_column='Insurance Pri Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_payor = models.TextField(db_column='Insurance Sec Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_payor_id = models.TextField(db_column='Insurance Sec Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_insurance_name = models.TextField(db_column='Insurance Sec Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_policy_field = models.TextField(db_column='Insurance Sec Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_sec_group_field = models.TextField(db_column='Insurance Sec Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_sec_policy_effective_date = models.TextField(db_column='Insurance Sec Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_policy_verified = models.TextField(db_column='Insurance Sec Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_pay_pct = models.TextField(db_column='Insurance Sec Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_include_this_payor_level_on_so = models.TextField(db_column='Insurance Sec Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Sec Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_automatically_generate_claims = models.TextField(db_column='Insurance Sec Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_10d = models.TextField(db_column='Insurance Sec Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_19 = models.TextField(db_column='Insurance Sec Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24ia = models.TextField(db_column='Insurance Sec Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24ja = models.TextField(db_column='Insurance Sec Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24jb = models.TextField(db_column='Insurance Sec Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_include_box_24jb = models.TextField(db_column='Insurance Sec Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_plan_type = models.TextField(db_column='Insurance Sec Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_payor = models.TextField(db_column='Insurance Ter Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_payor_id = models.TextField(db_column='Insurance Ter Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_insurance_name = models.TextField(db_column='Insurance Ter Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_policy_field = models.TextField(db_column='Insurance Ter Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_ter_group_field = models.TextField(db_column='Insurance Ter Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_ter_policy_effective_date = models.TextField(db_column='Insurance Ter Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_policy_verified = models.TextField(db_column='Insurance Ter Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_pay_pct = models.TextField(db_column='Insurance Ter Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_include_this_payor_level_on_so = models.TextField(db_column='Insurance Ter Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Ter Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_automatically_generate_claims = models.TextField(db_column='Insurance Ter Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_10d = models.TextField(db_column='Insurance Ter Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_19 = models.TextField(db_column='Insurance Ter Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24ia = models.TextField(db_column='Insurance Ter Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24ja = models.TextField(db_column='Insurance Ter Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24jb = models.TextField(db_column='Insurance Ter Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_include_box_24jb = models.TextField(db_column='Insurance Ter Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_plan_type = models.TextField(db_column='Insurance Ter Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_insurance_verified = models.TextField(db_column='Insurance Insurance Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_insurance_coverage_verified = models.TextField(db_column='Insurance Insurance Coverage Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri = models.TextField(db_column='Insurance Pri', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec = models.TextField(db_column='Insurance Sec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter = models.TextField(db_column='Insurance Ter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SalesOrderDetails'


class Salesorderitemdetails(models.Model):
    sales_order_number = models.TextField(db_column='Sales Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.TextField(db_column='Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_id = models.TextField(db_column='Sales Order Detail Item Id', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_name = models.TextField(db_column='Sales Order Detail Item Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_stocking_uom = models.TextField(db_column='Sales Order Detail Stocking UOM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_stocking_uom_name = models.TextField(db_column='Sales Order Detail Stocking UOM Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_description = models.TextField(db_column='Sales Order Detail Item Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_default_vendor = models.TextField(db_column='Sales Order Detail Default Vendor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_original_dos = models.TextField(db_column='Sales Order Detail Original DOS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_previous_billing_date = models.TextField(db_column='Sales Order Detail Previous Billing Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_next_billing_date = models.TextField(db_column='Sales Order Detail Next Billing Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_dos_to = models.TextField(db_column='Sales Order Detail DOS To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_next_period = models.TextField(db_column='Sales Order Detail Next Period', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_special_pricing = models.TextField(db_column='Sales Order Detail Special Pricing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_price_override = models.TextField(db_column='Sales Order Detail Price Override', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_special_tax_rate = models.TextField(db_column='Sales Order Detail Special Tax Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_qty = models.TextField(db_column='Sales Order Detail Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_bqty = models.TextField(db_column='Sales Order Detail Bqty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_line_qty = models.TextField(db_column='Sales Order Detail Line Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_proc_code = models.TextField(db_column='Sales Order Detail Proc Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_price_option = models.TextField(db_column='Sales Order Detail Price Option', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_modifier_1 = models.TextField(db_column='Sales Order Detail Modifier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_modifier_2 = models.TextField(db_column='Sales Order Detail Modifier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_modifier_3 = models.TextField(db_column='Sales Order Detail Modifier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_modifier_4 = models.TextField(db_column='Sales Order Detail Modifier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_charge = models.TextField(db_column='Sales Order Detail Charge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_allow = models.TextField(db_column='Sales Order Detail Allow', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_taxable = models.TextField(db_column='Sales Order Detail Taxable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn = models.TextField(db_column='Sales Order Detail ABN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_upgrade = models.TextField(db_column='Sales Order Detail ABN Upgrade', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_print_date = models.TextField(db_column='Sales Order Detail ABN Print Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_reason = models.TextField(db_column='Sales Order Detail ABN Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_item = models.TextField(db_column='Sales Order Detail ABN Item', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_proc_code = models.TextField(db_column='Sales Order Detail ABN Proc Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_allow = models.TextField(db_column='Sales Order Detail ABN Allow', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_charge = models.TextField(db_column='Sales Order Detail ABN Charge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_modifier_1 = models.TextField(db_column='Sales Order Detail ABN Modifier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_abn_modifier_2 = models.TextField(db_column='Sales Order Detail ABN Modifier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_tax_rate = models.TextField(db_column='Sales Order Detail Tax Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_tax_zone = models.TextField(db_column='Sales Order Detail Tax Zone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_non_tax_reason = models.TextField(db_column='Sales Order Detail Non Tax Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_note = models.TextField(db_column='Sales Order Detail Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_sale_type = models.TextField(db_column='Sales Order Detail Sale Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_group = models.TextField(db_column='Sales Order Detail Item Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_user_1 = models.TextField(db_column='Sales Order Detail Item User 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_user_2 = models.TextField(db_column='Sales Order Detail Item User 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_user_3 = models.TextField(db_column='Sales Order Detail Item User 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_user_4 = models.TextField(db_column='Sales Order Detail Item User 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_converted_to_purchase = models.TextField(db_column='Sales Order Detail Converted to purchase', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_manual_convert_to_purchase_mctp_field = models.TextField(db_column='Sales Order Detail Manual Convert To Purchase (MCTP)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sales_order_detail_mctp_charge = models.TextField(db_column='Sales Order Detail MCTP Charge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_mctp_allow = models.TextField(db_column='Sales Order Detail MCTP Allow', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_mctp_modifier_1 = models.TextField(db_column='Sales Order Detail MCTP Modifier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_mctp_modifier_2 = models.TextField(db_column='Sales Order Detail MCTP Modifier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_mctp_modifier_3 = models.TextField(db_column='Sales Order Detail MCTP Modifier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_mctp_modifier_4 = models.TextField(db_column='Sales Order Detail MCTP Modifier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_mctp_period = models.TextField(db_column='Sales Order Detail MCTP Period', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_addtl_modifier_1 = models.TextField(db_column='Sales Order Detail Addtl Modifier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_addtl_modifier_2 = models.TextField(db_column='Sales Order Detail Addtl Modifier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_addtl_modifier_3 = models.TextField(db_column='Sales Order Detail Addtl Modifier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_addtl_modifier_4 = models.TextField(db_column='Sales Order Detail Addtl Modifier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_next_date_of_service = models.TextField(db_column='Sales Order Detail Next Date Of Service', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_price_table = models.TextField(db_column='Sales Order Detail Price Table', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_price_option_name = models.TextField(db_column='Sales Order Detail Price Option Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_extended_charge_amount = models.TextField(db_column='Sales Order Detail Extended Charge Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_extended_allowance_amount = models.TextField(db_column='Sales Order Detail Extended Allowance Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_item_ndc_code = models.TextField(db_column='Sales Order Detail Item NDC Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_manufacturer = models.TextField(db_column='Sales Order Detail Manufacturer', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_manufacturer_item_id = models.TextField(db_column='Sales Order Detail Manufacturer Item ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_cb_pricing_field = models.TextField(db_column='Sales Order Detail CB Pricing ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sales_order_detail_cb_price_table_override = models.TextField(db_column='Sales Order Detail CB Price Table Override', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_cb_override = models.TextField(db_column='Sales Order Detail CB Override', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_messages = models.TextField(db_column='Sales Order Detail Messages', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_location = models.TextField(db_column='Sales Order Detail Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_calories_per_day = models.TextField(db_column='Sales Order Detail Calories Per Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_procudure_code = models.TextField(db_column='Sales Order Detail Secondary Billing Procudure Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_price_option = models.TextField(db_column='Sales Order Detail Secondary Billing Price Option', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_price_option_name = models.TextField(db_column='Sales Order Detail Secondary Billing Price Option Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_modifier_1 = models.TextField(db_column='Sales Order Detail Secondary Billing Modifier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_modifier_2 = models.TextField(db_column='Sales Order Detail Secondary Billing Modifier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_modifier_3 = models.TextField(db_column='Sales Order Detail Secondary Billing Modifier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_modifier_4 = models.TextField(db_column='Sales Order Detail Secondary Billing Modifier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_additional_modifier_1 = models.TextField(db_column='Sales Order Detail Secondary Billing Additional Modifier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_additional_modifier_2 = models.TextField(db_column='Sales Order Detail Secondary Billing Additional Modifier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_additional_modifier_3 = models.TextField(db_column='Sales Order Detail Secondary Billing Additional Modifier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_additional_modifier_4 = models.TextField(db_column='Sales Order Detail Secondary Billing Additional Modifier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_billing_ignore = models.TextField(db_column='Sales Order Detail Secondary Billing Ignore', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_detail_secondary_special_billing = models.TextField(db_column='Sales Order Detail Secondary Special Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serial_numbers_serial_number = models.TextField(db_column='Serial Numbers Serial Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serial_numbers_cost_amount = models.TextField(db_column='Serial Numbers Cost Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serial_numbers_current_value = models.TextField(db_column='Serial Numbers Current Value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serial_numbers_asset_number = models.TextField(db_column='Serial Numbers Asset Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lot_numbers_lot_number = models.TextField(db_column='Lot Numbers Lot Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lot_numbers_expiration_date = models.TextField(db_column='Lot Numbers Expiration Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_gl_account_group = models.TextField(db_column='Item Location GL Account Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_most_recent_cost = models.TextField(db_column='Item Location Most Recent Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_average_cost = models.TextField(db_column='Item Location Average Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_last_sale_date = models.TextField(db_column='Item Location Last Sale Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_on_rent_qty = models.TextField(db_column='Item Location On Rent Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_on_hand_qty = models.TextField(db_column='Item Location On Hand Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_on_order_qty = models.TextField(db_column='Item Location On Order Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_available_qty = models.TextField(db_column='Item Location Available Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_committed_qty = models.TextField(db_column='Item Location Committed Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_bin = models.TextField(db_column='Item Location Bin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_location_alternate_bin = models.TextField(db_column='Item Location Alternate Bin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SalesOrderItemDetails'


class Salesorders(models.Model):
    sales_order_number = models.TextField(db_column='Sales Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_date_created = models.TextField(db_column='Sales Order Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_created_by = models.TextField(db_column='Sales Order Created by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_branch_office = models.TextField(db_column='Sales Order Branch Office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_status = models.TextField(db_column='Sales Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_manual_hold = models.TextField(db_column='Sales Order Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_location = models.TextField(db_column='Sales Order Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_discount_pct = models.TextField(db_column='Sales Order Discount Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_po_number = models.TextField(db_column='Sales Order PO Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_purchase_order_number = models.TextField(db_column='Sales Order Purchase Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_reference = models.TextField(db_column='Sales Order Reference', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_previous_billing = models.TextField(db_column='Sales Order Previous Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_next_billing = models.TextField(db_column='Sales Order Next Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_1 = models.TextField(db_column='Sales Order User 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_2 = models.TextField(db_column='Sales Order User 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_3 = models.TextField(db_column='Sales Order User 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_4 = models.TextField(db_column='Sales Order User 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_confirm_date = models.TextField(db_column='Sales Order Confirm Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_confirmed_by = models.TextField(db_column='Sales Order Confirmed By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_last_printed = models.TextField(db_column='Sales Order Last Printed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_date = models.TextField(db_column='Sales Order Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_branch_group = models.TextField(db_column='Sales Order Branch Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_delivery_note = models.TextField(db_column='Sales Order Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_note = models.TextField(db_column='Sales Order Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_classification = models.TextField(db_column='Sales Order Classification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_type = models.TextField(db_column='Sales Order Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_pod_order_status = models.TextField(db_column='Sales Order POD Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_manual_hold_reason = models.TextField(db_column='Sales Order Manual Hold Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_facility = models.TextField(db_column='Sales Order Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_facility_group = models.TextField(db_column='Sales Order Facility Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_retail_pos_order = models.TextField(db_column='Sales Order Retail POS Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_prior_system_key = models.TextField(db_column='Sales Order Prior System Key', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_height = models.TextField(db_column='Sales Order Height', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_weight = models.TextField(db_column='Sales Order Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field1 = models.TextField(db_column='Sales Order Custom Fields Field1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field2 = models.TextField(db_column='Sales Order Custom Fields Field2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field3 = models.TextField(db_column='Sales Order Custom Fields Field3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field4 = models.TextField(db_column='Sales Order Custom Fields Field4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field5 = models.TextField(db_column='Sales Order Custom Fields Field5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field6 = models.TextField(db_column='Sales Order Custom Fields Field6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field7 = models.TextField(db_column='Sales Order Custom Fields Field7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field8 = models.TextField(db_column='Sales Order Custom Fields Field8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field9 = models.TextField(db_column='Sales Order Custom Fields Field9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field10 = models.TextField(db_column='Sales Order Custom Fields Field10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field11 = models.TextField(db_column='Sales Order Custom Fields Field11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field12 = models.TextField(db_column='Sales Order Custom Fields Field12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field13 = models.TextField(db_column='Sales Order Custom Fields Field13', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field14 = models.TextField(db_column='Sales Order Custom Fields Field14', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field15 = models.TextField(db_column='Sales Order Custom Fields Field15', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field16 = models.TextField(db_column='Sales Order Custom Fields Field16', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field17 = models.TextField(db_column='Sales Order Custom Fields Field17', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field18 = models.TextField(db_column='Sales Order Custom Fields Field18', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field19 = models.TextField(db_column='Sales Order Custom Fields Field19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field20 = models.TextField(db_column='Sales Order Custom Fields Field20', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field21 = models.TextField(db_column='Sales Order Custom Fields Field21', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field22 = models.TextField(db_column='Sales Order Custom Fields Field22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field23 = models.TextField(db_column='Sales Order Custom Fields Field23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field24 = models.TextField(db_column='Sales Order Custom Fields Field24', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field25 = models.TextField(db_column='Sales Order Custom Fields Field25', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_cmn_not_logged = models.TextField(db_column='Sales Order Hold CMN Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_cmn_expired = models.TextField(db_column='Sales Order Hold CMN Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_par_not_logged = models.TextField(db_column='Sales Order Hold PAR Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_par_expired = models.TextField(db_column='Sales Order Hold PAR Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_manual_hold = models.TextField(db_column='Sales Order Hold Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_type = models.TextField(db_column='Sales Order Stop Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_pending_pickup = models.TextField(db_column='Sales Order Stop Pending Pickup', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_multiple_pricing_options = models.TextField(db_column='Sales Order Stop Multiple Pricing Options', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_policy_expired = models.TextField(db_column='Sales Order Stop Policy Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_no_pricing_found = models.TextField(db_column='Sales Order Stop No Pricing Found', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_policy_changed = models.TextField(db_column='Sales Order Stop Policy Changed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_manual_stop_date = models.TextField(db_column='Sales Order Stop Manual Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_automatic_eligibility_check = models.TextField(db_column='Sales Order Stop Automatic Eligibility Check', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_ineligible_policy = models.TextField(db_column='Sales Order Stop Ineligible Policy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_wip_state = models.TextField(db_column='Work In Progress WIP State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_assigned_to = models.TextField(db_column='Work In Progress Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_date_needed = models.TextField(db_column='Work In Progress Date Needed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_completed = models.TextField(db_column='Work In Progress Completed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_wip_days_in_state = models.TextField(db_column='Work In Progress WIP Days In State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_scheduled_date = models.TextField(db_column='Delivery Scheduled date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_scheduled_time = models.TextField(db_column='Delivery Scheduled time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_actual_date = models.TextField(db_column='Delivery Actual date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_actual_time = models.TextField(db_column='Delivery Actual time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_1 = models.TextField(db_column='Delivery Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_2 = models.TextField(db_column='Delivery Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_3 = models.TextField(db_column='Delivery Address 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_city = models.TextField(db_column='Delivery City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_state = models.TextField(db_column='Delivery State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_county = models.TextField(db_column='Delivery County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_country = models.TextField(db_column='Delivery Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_postal_code = models.TextField(db_column='Delivery Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_phone = models.TextField(db_column='Delivery Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_fax = models.TextField(db_column='Delivery Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_tax_zone = models.TextField(db_column='Delivery Tax Zone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_tax_rate = models.TextField(db_column='Delivery Tax Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_technician = models.TextField(db_column='Delivery Technician', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_status = models.TextField(db_column='Delivery Bright Ship Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_carrier = models.TextField(db_column='Delivery Bright Ship Carrier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_method = models.TextField(db_column='Delivery Bright Ship Method', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_tracking_numbers = models.TextField(db_column='Delivery Bright Ship Tracking Numbers', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_fulfillment_vendor = models.TextField(db_column='Delivery Fulfillment Vendor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_account_number = models.TextField(db_column='Delivery Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_ship_by = models.TextField(db_column='Delivery Ship By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_status = models.TextField(db_column='Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_status_date = models.TextField(db_column='Delivery Status Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_pos = models.TextField(db_column='Place of Service POS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_date_of_admission = models.TextField(db_column='Place of Service Date of Admission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_date_of_discharge = models.TextField(db_column='Place of Service Date of Discharge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.TextField(db_column='Patient Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.TextField(db_column='Patient First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_middle_name = models.TextField(db_column='Patient Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_email_address = models.TextField(db_column='Patient Email Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_address_1 = models.TextField(db_column='Patient Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_address_2 = models.TextField(db_column='Patient Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_city = models.TextField(db_column='Patient City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_state = models.TextField(db_column='Patient State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_postal_code = models.TextField(db_column='Patient Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_phone = models.TextField(db_column='Patient Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_mobile = models.TextField(db_column='Patient Mobile', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_fax = models.TextField(db_column='Patient Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.TextField(db_column='Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_account_number = models.TextField(db_column='Patient Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_date_created = models.TextField(db_column='Patient Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_dob = models.TextField(db_column='Patient DOB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_dod = models.TextField(db_column='Patient DOD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_ssn = models.TextField(db_column='Patient SSN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_delivery_note = models.TextField(db_column='Patient Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_branch = models.TextField(db_column='Patient Branch', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_full_name = models.TextField(db_column='Patient Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_gender = models.TextField(db_column='Patient Gender', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_customer_type = models.TextField(db_column='Patient Customer Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_facility = models.TextField(db_column='Patient Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_security_group = models.TextField(db_column='Patient Security Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_restricted_access = models.TextField(db_column='Patient Restricted Access', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_auto_pay_status = models.TextField(db_column='Patient BPC Auto PAY Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_e_delivery_status = models.TextField(db_column='Patient BPC e Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_payment_plan = models.TextField(db_column='Patient BPC Payment Plan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_information = models.TextField(db_column='Patient BPC Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_patient_hub_status = models.TextField(db_column='Patient Patient Hub Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_last_name = models.TextField(db_column='Ordering Doctor Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_first_name = models.TextField(db_column='Ordering Doctor First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_address_1 = models.TextField(db_column='Ordering Doctor Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_address_2 = models.TextField(db_column='Ordering Doctor Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_city = models.TextField(db_column='Ordering Doctor City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_state = models.TextField(db_column='Ordering Doctor State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_postal_code = models.TextField(db_column='Ordering Doctor Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_phone = models.TextField(db_column='Ordering Doctor Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_fax = models.TextField(db_column='Ordering Doctor Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_fax_to = models.TextField(db_column='Ordering Doctor Fax To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_pecos_certify_status = models.TextField(db_column='Ordering Doctor PECOS Certify Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_full_name = models.TextField(db_column='Ordering Doctor Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_group = models.TextField(db_column='Ordering Doctor Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_npi = models.TextField(db_column='Ordering Doctor NPI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_solution = models.TextField(db_column='Sleep Therapy Solution', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_setup_date = models.TextField(db_column='Sleep Therapy Setup Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_registration_status = models.TextField(db_column='Sleep Therapy Registration Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_compliance_date = models.TextField(db_column='Sleep Therapy Compliance Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_compliance_status = models.TextField(db_column='Sleep Therapy Compliance Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_external_patient_id = models.TextField(db_column='Sleep Therapy External Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_employment = models.TextField(db_column='Workers Compensation Injury Related to Employment', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_auto_accident = models.TextField(db_column='Workers Compensation Injury Related to Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_state_of_auto_accident = models.TextField(db_column='Workers Compensation State of Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_other_accident = models.TextField(db_column='Workers Compensation Injury Related to Other Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_onset_date = models.TextField(db_column='Workers Compensation Onset Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_type = models.TextField(db_column='Referral Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_name = models.TextField(db_column='Referral Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_address_1 = models.TextField(db_column='Referral Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_address_2 = models.TextField(db_column='Referral Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_city = models.TextField(db_column='Referral City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_state = models.TextField(db_column='Referral State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_zip = models.TextField(db_column='Referral Zip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_phone = models.TextField(db_column='Referral Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_fax = models.TextField(db_column='Referral Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_contact_name = models.TextField(db_column='Referral Contact Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_doctor_group = models.TextField(db_column='Referral Doctor Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_facility_group = models.TextField(db_column='Referral Facility Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_type = models.TextField(db_column='Referring Provider Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_name = models.TextField(db_column='Referring Provider Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_address_1 = models.TextField(db_column='Referring Provider Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_address_2 = models.TextField(db_column='Referring Provider Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_city = models.TextField(db_column='Referring Provider City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_state = models.TextField(db_column='Referring Provider State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_zip = models.TextField(db_column='Referring Provider Zip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_phone = models.TextField(db_column='Referring Provider Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_fax = models.TextField(db_column='Referring Provider Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_npi = models.TextField(db_column='Referring Provider NPI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_payor = models.TextField(db_column='Insurance Pri Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_payor_id = models.TextField(db_column='Insurance Pri Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_insurance_name = models.TextField(db_column='Insurance Pri Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_policy_field = models.TextField(db_column='Insurance Pri Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_pri_group_field = models.TextField(db_column='Insurance Pri Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_pri_policy_effective_date = models.TextField(db_column='Insurance Pri Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_policy_verified = models.TextField(db_column='Insurance Pri Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_pay_pct = models.TextField(db_column='Insurance Pri Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_include_this_payor_level_on_so = models.TextField(db_column='Insurance Pri Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Pri Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_automatically_generate_claims = models.TextField(db_column='Insurance Pri Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_10d = models.TextField(db_column='Insurance Pri Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_19 = models.TextField(db_column='Insurance Pri Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24ia = models.TextField(db_column='Insurance Pri Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24ja = models.TextField(db_column='Insurance Pri Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24jb = models.TextField(db_column='Insurance Pri Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_include_box_24jb = models.TextField(db_column='Insurance Pri Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_plan_type = models.TextField(db_column='Insurance Pri Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_payor = models.TextField(db_column='Insurance Sec Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_payor_id = models.TextField(db_column='Insurance Sec Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_insurance_name = models.TextField(db_column='Insurance Sec Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_policy_field = models.TextField(db_column='Insurance Sec Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_sec_group_field = models.TextField(db_column='Insurance Sec Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_sec_policy_effective_date = models.TextField(db_column='Insurance Sec Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_policy_verified = models.TextField(db_column='Insurance Sec Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_pay_pct = models.TextField(db_column='Insurance Sec Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_include_this_payor_level_on_so = models.TextField(db_column='Insurance Sec Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Sec Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_automatically_generate_claims = models.TextField(db_column='Insurance Sec Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_10d = models.TextField(db_column='Insurance Sec Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_19 = models.TextField(db_column='Insurance Sec Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24ia = models.TextField(db_column='Insurance Sec Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24ja = models.TextField(db_column='Insurance Sec Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24jb = models.TextField(db_column='Insurance Sec Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_plan_type = models.TextField(db_column='Insurance Sec Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_include_box_24jb = models.TextField(db_column='Insurance Sec Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_payor = models.TextField(db_column='Insurance Ter Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_payor_id = models.TextField(db_column='Insurance Ter Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_insurance_name = models.TextField(db_column='Insurance Ter Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_policy_field = models.TextField(db_column='Insurance Ter Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_ter_group_field = models.TextField(db_column='Insurance Ter Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_ter_policy_effective_date = models.TextField(db_column='Insurance Ter Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_policy_verified = models.TextField(db_column='Insurance Ter Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_pay_pct = models.TextField(db_column='Insurance Ter Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_include_this_payor_level_on_so = models.TextField(db_column='Insurance Ter Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Ter Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_automatically_generate_claims = models.TextField(db_column='Insurance Ter Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_10d = models.TextField(db_column='Insurance Ter Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_19 = models.TextField(db_column='Insurance Ter Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24ia = models.TextField(db_column='Insurance Ter Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24ja = models.TextField(db_column='Insurance Ter Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24jb = models.TextField(db_column='Insurance Ter Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_include_box_24jb = models.TextField(db_column='Insurance Ter Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_plan_type = models.TextField(db_column='Insurance Ter Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_insurance_verified = models.TextField(db_column='Insurance Insurance Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_insurance_coverage_verified = models.TextField(db_column='Insurance Insurance Coverage Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri = models.TextField(db_column='Insurance Pri', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec = models.TextField(db_column='Insurance Sec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter = models.TextField(db_column='Insurance Ter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_claim_note_type = models.TextField(db_column='Insurance Claim Note Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_claim_note = models.TextField(db_column='Insurance Claim Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marketing_rep_last_name = models.TextField(db_column='Marketing Rep Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marketing_rep_first_name = models.TextField(db_column='Marketing Rep First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marketing_rep_full_name = models.TextField(db_column='Marketing Rep Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    practitioner_last_name = models.TextField(db_column='Practitioner Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    practitioner_first_name = models.TextField(db_column='Practitioner First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    practitioner_middle_name = models.TextField(db_column='Practitioner Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rendering_provider_type = models.TextField(db_column='Rendering Provider Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rendering_provider_doctor = models.TextField(db_column='Rendering Provider Doctor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rendering_provider_facility = models.TextField(db_column='Rendering Provider Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_id = models.TextField(db_column='Diagnostic Testing Testing ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_date_ordered = models.TextField(db_column='Diagnostic Testing Date Ordered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_test_group = models.TextField(db_column='Diagnostic Testing Test Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_test_name = models.TextField(db_column='Diagnostic Testing Test Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_partner = models.TextField(db_column='Diagnostic Testing Testing Partner', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_status = models.TextField(db_column='Diagnostic Testing Testing Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_completed_dated = models.TextField(db_column='Diagnostic Testing Testing Completed Dated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rule = models.ForeignKey(CapemedicalTeamsettings, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SalesOrders'


class SalesordersTemp(models.Model):
    sales_order_number = models.TextField(db_column='Sales Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_date_created = models.TextField(db_column='Sales Order Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_created_by = models.TextField(db_column='Sales Order Created by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_branch_office = models.TextField(db_column='Sales Order Branch Office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_status = models.TextField(db_column='Sales Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_manual_hold = models.TextField(db_column='Sales Order Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_location = models.TextField(db_column='Sales Order Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_discount_pct = models.TextField(db_column='Sales Order Discount Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_po_number = models.TextField(db_column='Sales Order PO Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_purchase_order_number = models.TextField(db_column='Sales Order Purchase Order Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_reference = models.TextField(db_column='Sales Order Reference', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_previous_billing = models.TextField(db_column='Sales Order Previous Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_next_billing = models.TextField(db_column='Sales Order Next Billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_1 = models.TextField(db_column='Sales Order User 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_2 = models.TextField(db_column='Sales Order User 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_3 = models.TextField(db_column='Sales Order User 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_user_4 = models.TextField(db_column='Sales Order User 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_confirm_date = models.TextField(db_column='Sales Order Confirm Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_confirmed_by = models.TextField(db_column='Sales Order Confirmed By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_last_printed = models.TextField(db_column='Sales Order Last Printed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_date = models.TextField(db_column='Sales Order Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_branch_group = models.TextField(db_column='Sales Order Branch Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_delivery_note = models.TextField(db_column='Sales Order Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_note = models.TextField(db_column='Sales Order Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_classification = models.TextField(db_column='Sales Order Classification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_type = models.TextField(db_column='Sales Order Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_pod_order_status = models.TextField(db_column='Sales Order POD Order Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_manual_hold_reason = models.TextField(db_column='Sales Order Manual Hold Reason', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_facility = models.TextField(db_column='Sales Order Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_facility_group = models.TextField(db_column='Sales Order Facility Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_retail_pos_order = models.TextField(db_column='Sales Order Retail POS Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_prior_system_key = models.TextField(db_column='Sales Order Prior System Key', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_height = models.TextField(db_column='Sales Order Height', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_weight = models.TextField(db_column='Sales Order Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field1 = models.TextField(db_column='Sales Order Custom Fields Field1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field2 = models.TextField(db_column='Sales Order Custom Fields Field2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field3 = models.TextField(db_column='Sales Order Custom Fields Field3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field4 = models.TextField(db_column='Sales Order Custom Fields Field4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field5 = models.TextField(db_column='Sales Order Custom Fields Field5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field6 = models.TextField(db_column='Sales Order Custom Fields Field6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field7 = models.TextField(db_column='Sales Order Custom Fields Field7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field8 = models.TextField(db_column='Sales Order Custom Fields Field8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field9 = models.TextField(db_column='Sales Order Custom Fields Field9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field10 = models.TextField(db_column='Sales Order Custom Fields Field10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field11 = models.TextField(db_column='Sales Order Custom Fields Field11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field12 = models.TextField(db_column='Sales Order Custom Fields Field12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field13 = models.TextField(db_column='Sales Order Custom Fields Field13', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field14 = models.TextField(db_column='Sales Order Custom Fields Field14', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field15 = models.TextField(db_column='Sales Order Custom Fields Field15', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field16 = models.TextField(db_column='Sales Order Custom Fields Field16', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field17 = models.TextField(db_column='Sales Order Custom Fields Field17', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field18 = models.TextField(db_column='Sales Order Custom Fields Field18', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field19 = models.TextField(db_column='Sales Order Custom Fields Field19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field20 = models.TextField(db_column='Sales Order Custom Fields Field20', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field21 = models.TextField(db_column='Sales Order Custom Fields Field21', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field22 = models.TextField(db_column='Sales Order Custom Fields Field22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field23 = models.TextField(db_column='Sales Order Custom Fields Field23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field24 = models.TextField(db_column='Sales Order Custom Fields Field24', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_custom_fields_field25 = models.TextField(db_column='Sales Order Custom Fields Field25', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_cmn_not_logged = models.TextField(db_column='Sales Order Hold CMN Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_cmn_expired = models.TextField(db_column='Sales Order Hold CMN Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_par_not_logged = models.TextField(db_column='Sales Order Hold PAR Not Logged', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_par_expired = models.TextField(db_column='Sales Order Hold PAR Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_hold_manual_hold = models.TextField(db_column='Sales Order Hold Manual Hold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_type = models.TextField(db_column='Sales Order Stop Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_pending_pickup = models.TextField(db_column='Sales Order Stop Pending Pickup', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_multiple_pricing_options = models.TextField(db_column='Sales Order Stop Multiple Pricing Options', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_policy_expired = models.TextField(db_column='Sales Order Stop Policy Expired', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_no_pricing_found = models.TextField(db_column='Sales Order Stop No Pricing Found', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_policy_changed = models.TextField(db_column='Sales Order Stop Policy Changed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_manual_stop_date = models.TextField(db_column='Sales Order Stop Manual Stop Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_automatic_eligibility_check = models.TextField(db_column='Sales Order Stop Automatic Eligibility Check', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_stop_ineligible_policy = models.TextField(db_column='Sales Order Stop Ineligible Policy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_wip_state = models.TextField(db_column='Work In Progress WIP State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_assigned_to = models.TextField(db_column='Work In Progress Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_date_needed = models.TextField(db_column='Work In Progress Date Needed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_completed = models.TextField(db_column='Work In Progress Completed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_in_progress_wip_days_in_state = models.TextField(db_column='Work In Progress WIP Days In State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_scheduled_date = models.TextField(db_column='Delivery Scheduled date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_scheduled_time = models.TextField(db_column='Delivery Scheduled time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_actual_date = models.TextField(db_column='Delivery Actual date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_actual_time = models.TextField(db_column='Delivery Actual time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_1 = models.TextField(db_column='Delivery Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_2 = models.TextField(db_column='Delivery Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_address_3 = models.TextField(db_column='Delivery Address 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_city = models.TextField(db_column='Delivery City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_state = models.TextField(db_column='Delivery State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_county = models.TextField(db_column='Delivery County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_country = models.TextField(db_column='Delivery Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_postal_code = models.TextField(db_column='Delivery Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_phone = models.TextField(db_column='Delivery Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_fax = models.TextField(db_column='Delivery Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_tax_zone = models.TextField(db_column='Delivery Tax Zone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_tax_rate = models.TextField(db_column='Delivery Tax Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_technician = models.TextField(db_column='Delivery Technician', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_status = models.TextField(db_column='Delivery Bright Ship Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_carrier = models.TextField(db_column='Delivery Bright Ship Carrier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_method = models.TextField(db_column='Delivery Bright Ship Method', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_bright_ship_tracking_numbers = models.TextField(db_column='Delivery Bright Ship Tracking Numbers', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_fulfillment_vendor = models.TextField(db_column='Delivery Fulfillment Vendor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_account_number = models.TextField(db_column='Delivery Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_ship_by = models.TextField(db_column='Delivery Ship By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_status = models.TextField(db_column='Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_status_date = models.TextField(db_column='Delivery Status Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_pos = models.TextField(db_column='Place of Service POS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_date_of_admission = models.TextField(db_column='Place of Service Date of Admission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_service_date_of_discharge = models.TextField(db_column='Place of Service Date of Discharge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_last_name = models.TextField(db_column='Patient Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_first_name = models.TextField(db_column='Patient First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_middle_name = models.TextField(db_column='Patient Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_email_address = models.TextField(db_column='Patient Email Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_address_1 = models.TextField(db_column='Patient Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_address_2 = models.TextField(db_column='Patient Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_city = models.TextField(db_column='Patient City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_state = models.TextField(db_column='Patient State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_postal_code = models.TextField(db_column='Patient Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_phone = models.TextField(db_column='Patient Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_mobile = models.TextField(db_column='Patient Mobile', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_fax = models.TextField(db_column='Patient Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.TextField(db_column='Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_account_number = models.TextField(db_column='Patient Account Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_date_created = models.TextField(db_column='Patient Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_dob = models.TextField(db_column='Patient DOB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_dod = models.TextField(db_column='Patient DOD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_ssn = models.TextField(db_column='Patient SSN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_delivery_note = models.TextField(db_column='Patient Delivery Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_branch = models.TextField(db_column='Patient Branch', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_full_name = models.TextField(db_column='Patient Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_gender = models.TextField(db_column='Patient Gender', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_customer_type = models.TextField(db_column='Patient Customer Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_facility = models.TextField(db_column='Patient Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_security_group = models.TextField(db_column='Patient Security Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_restricted_access = models.TextField(db_column='Patient Restricted Access', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_auto_pay_status = models.TextField(db_column='Patient BPC Auto PAY Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_e_delivery_status = models.TextField(db_column='Patient BPC e Delivery Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_payment_plan = models.TextField(db_column='Patient BPC Payment Plan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_bpc_information = models.TextField(db_column='Patient BPC Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_patient_hub_status = models.TextField(db_column='Patient Patient Hub Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_last_name = models.TextField(db_column='Ordering Doctor Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_first_name = models.TextField(db_column='Ordering Doctor First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_address_1 = models.TextField(db_column='Ordering Doctor Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_address_2 = models.TextField(db_column='Ordering Doctor Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_city = models.TextField(db_column='Ordering Doctor City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_state = models.TextField(db_column='Ordering Doctor State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_postal_code = models.TextField(db_column='Ordering Doctor Postal Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_phone = models.TextField(db_column='Ordering Doctor Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_fax = models.TextField(db_column='Ordering Doctor Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_fax_to = models.TextField(db_column='Ordering Doctor Fax To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_pecos_certify_status = models.TextField(db_column='Ordering Doctor PECOS Certify Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_full_name = models.TextField(db_column='Ordering Doctor Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_group = models.TextField(db_column='Ordering Doctor Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_doctor_npi = models.TextField(db_column='Ordering Doctor NPI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_solution = models.TextField(db_column='Sleep Therapy Solution', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_setup_date = models.TextField(db_column='Sleep Therapy Setup Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_registration_status = models.TextField(db_column='Sleep Therapy Registration Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_compliance_date = models.TextField(db_column='Sleep Therapy Compliance Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_compliance_status = models.TextField(db_column='Sleep Therapy Compliance Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleep_therapy_external_patient_id = models.TextField(db_column='Sleep Therapy External Patient ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_code_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Code #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_9_description_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-9 Description #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_01 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #01', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_02 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #02', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_03 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #03', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_04 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #04', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_05 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #05', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_06 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #06', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_07 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #07', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_08 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #08', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_09 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #09', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_10 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_11 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #11', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_code_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Code #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order_diagnosis_codes_dx_icd_10_description_12 = models.TextField(db_column='Sales Order Diagnosis Codes Dx ICD-10 Description #12', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_employment = models.TextField(db_column='Workers Compensation Injury Related to Employment', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_auto_accident = models.TextField(db_column='Workers Compensation Injury Related to Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_state_of_auto_accident = models.TextField(db_column='Workers Compensation State of Auto Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_injury_related_to_other_accident = models.TextField(db_column='Workers Compensation Injury Related to Other Accident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workers_compensation_onset_date = models.TextField(db_column='Workers Compensation Onset Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_type = models.TextField(db_column='Referral Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_name = models.TextField(db_column='Referral Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_address_1 = models.TextField(db_column='Referral Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_address_2 = models.TextField(db_column='Referral Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_city = models.TextField(db_column='Referral City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_state = models.TextField(db_column='Referral State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_zip = models.TextField(db_column='Referral Zip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_phone = models.TextField(db_column='Referral Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_fax = models.TextField(db_column='Referral Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_contact_name = models.TextField(db_column='Referral Contact Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_doctor_group = models.TextField(db_column='Referral Doctor Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral_facility_group = models.TextField(db_column='Referral Facility Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_type = models.TextField(db_column='Referring Provider Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_name = models.TextField(db_column='Referring Provider Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_address_1 = models.TextField(db_column='Referring Provider Address 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_address_2 = models.TextField(db_column='Referring Provider Address 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_city = models.TextField(db_column='Referring Provider City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_state = models.TextField(db_column='Referring Provider State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_zip = models.TextField(db_column='Referring Provider Zip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_phone = models.TextField(db_column='Referring Provider Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_fax = models.TextField(db_column='Referring Provider Fax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referring_provider_npi = models.TextField(db_column='Referring Provider NPI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_payor = models.TextField(db_column='Insurance Pri Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_payor_id = models.TextField(db_column='Insurance Pri Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_insurance_name = models.TextField(db_column='Insurance Pri Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_policy_field = models.TextField(db_column='Insurance Pri Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_pri_group_field = models.TextField(db_column='Insurance Pri Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_pri_policy_effective_date = models.TextField(db_column='Insurance Pri Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_policy_verified = models.TextField(db_column='Insurance Pri Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_pay_pct = models.TextField(db_column='Insurance Pri Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_include_this_payor_level_on_so = models.TextField(db_column='Insurance Pri Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Pri Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_automatically_generate_claims = models.TextField(db_column='Insurance Pri Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_10d = models.TextField(db_column='Insurance Pri Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_19 = models.TextField(db_column='Insurance Pri Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24ia = models.TextField(db_column='Insurance Pri Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24ja = models.TextField(db_column='Insurance Pri Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_box_24jb = models.TextField(db_column='Insurance Pri Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_include_box_24jb = models.TextField(db_column='Insurance Pri Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri_plan_type = models.TextField(db_column='Insurance Pri Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_payor = models.TextField(db_column='Insurance Sec Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_payor_id = models.TextField(db_column='Insurance Sec Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_insurance_name = models.TextField(db_column='Insurance Sec Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_policy_field = models.TextField(db_column='Insurance Sec Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_sec_group_field = models.TextField(db_column='Insurance Sec Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_sec_policy_effective_date = models.TextField(db_column='Insurance Sec Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_policy_verified = models.TextField(db_column='Insurance Sec Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_pay_pct = models.TextField(db_column='Insurance Sec Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_include_this_payor_level_on_so = models.TextField(db_column='Insurance Sec Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Sec Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_automatically_generate_claims = models.TextField(db_column='Insurance Sec Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_10d = models.TextField(db_column='Insurance Sec Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_19 = models.TextField(db_column='Insurance Sec Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24ia = models.TextField(db_column='Insurance Sec Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24ja = models.TextField(db_column='Insurance Sec Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_box_24jb = models.TextField(db_column='Insurance Sec Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_plan_type = models.TextField(db_column='Insurance Sec Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec_include_box_24jb = models.TextField(db_column='Insurance Sec Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_payor = models.TextField(db_column='Insurance Ter Payor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_payor_id = models.TextField(db_column='Insurance Ter Payor ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_insurance_name = models.TextField(db_column='Insurance Ter Insurance Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_policy_field = models.TextField(db_column='Insurance Ter Policy #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_ter_group_field = models.TextField(db_column='Insurance Ter Group #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insurance_ter_policy_effective_date = models.TextField(db_column='Insurance Ter Policy Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_policy_verified = models.TextField(db_column='Insurance Ter Policy Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_pay_pct = models.TextField(db_column='Insurance Ter Pay Pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_include_this_payor_level_on_so = models.TextField(db_column='Insurance Ter Include this payor level on SO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_wait_for_previous_payor_before_billing = models.TextField(db_column='Insurance Ter Wait for previous payor before billing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_automatically_generate_claims = models.TextField(db_column='Insurance Ter Automatically generate claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_10d = models.TextField(db_column='Insurance Ter Box 10D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_19 = models.TextField(db_column='Insurance Ter Box 19', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24ia = models.TextField(db_column='Insurance Ter Box 24Ia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24ja = models.TextField(db_column='Insurance Ter Box 24Ja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_box_24jb = models.TextField(db_column='Insurance Ter Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_include_box_24jb = models.TextField(db_column='Insurance Ter Include Box 24Jb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter_plan_type = models.TextField(db_column='Insurance Ter Plan Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_insurance_verified = models.TextField(db_column='Insurance Insurance Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_insurance_coverage_verified = models.TextField(db_column='Insurance Insurance Coverage Verified', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_pri = models.TextField(db_column='Insurance Pri', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_sec = models.TextField(db_column='Insurance Sec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_ter = models.TextField(db_column='Insurance Ter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_claim_note_type = models.TextField(db_column='Insurance Claim Note Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_claim_note = models.TextField(db_column='Insurance Claim Note', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marketing_rep_last_name = models.TextField(db_column='Marketing Rep Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marketing_rep_first_name = models.TextField(db_column='Marketing Rep First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marketing_rep_full_name = models.TextField(db_column='Marketing Rep Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    practitioner_last_name = models.TextField(db_column='Practitioner Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    practitioner_first_name = models.TextField(db_column='Practitioner First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    practitioner_middle_name = models.TextField(db_column='Practitioner Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rendering_provider_type = models.TextField(db_column='Rendering Provider Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rendering_provider_doctor = models.TextField(db_column='Rendering Provider Doctor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rendering_provider_facility = models.TextField(db_column='Rendering Provider Facility', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_id = models.TextField(db_column='Diagnostic Testing Testing ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_date_ordered = models.TextField(db_column='Diagnostic Testing Date Ordered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_test_group = models.TextField(db_column='Diagnostic Testing Test Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_test_name = models.TextField(db_column='Diagnostic Testing Test Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_partner = models.TextField(db_column='Diagnostic Testing Testing Partner', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_status = models.TextField(db_column='Diagnostic Testing Testing Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diagnostic_testing_testing_completed_dated = models.TextField(db_column='Diagnostic Testing Testing Completed Dated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rule_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SalesOrders_temp'


class Wipstatesmapping(models.Model):
    brightree_wip_states = models.TextField(db_column='Brightree WIP States', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wip_states_group = models.TextField(db_column='WIP States Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    order = models.IntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WIPStatesMapping'


class AccountsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    active = models.BooleanField()
    staff = models.BooleanField()
    admin = models.BooleanField()
    full_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
