Feature: View Assessment
  

########
# SUNNY CASES
########
  Scenario: Retrieve assessment of patient
    Given the patient assessment with school id '20130000'
    And the patient assessment with an assessment id '4'
    When the doctor click view assessment with an id '4'
    Then it should have a '200' response
    And it should have a field 'status' containing 'OK'
    And it should have a field 'message' containing 'OK'
    And the following details will be returned
    |assessment_id|assessment_date|school_id|age|vital_signid|temperature|pulse_rate|respiration_rate|blood_pressure|weight|chief_complaint|history_of_present_illness|medications_taken|diagnosis|recommendation|attending_physician|
    |	1		  | 2015-07-02 00:00:00  |20131288 |18 |     1		 |    37.2	 |    120   |      100		 |  120//80      | 60   | none	  |         none			 |		none	   |	none |	none		| muhammad puting	|