# HospitalComp-Finance
##Objectives: predict hospital performance based on finance
This is a preliminary prediction analysis of hospital performance (county-wise) based on regional financial status.  Data is obtained from [data.gov](http://www.data.gov/).

#### Data contained in folder, *data* 
*Finance Related*
* **COG_2012_LGF002.csv**: local government finances by type of government and state (found in folder, COG_2012_LGF002)
* **cbp12co.txt**: county business pattern (available [here](https://www.census.gov/econ/cbp/download/))
* **allpovu_copy.csv**: Estimated population in poverty universe
* **est13ALL_copy.csv**: Poverty and Median Household Income Estimates

*Hospital Related*
* **Outcome of Care Measures.csv**: outcome of care measure per hospital (found in folder, HOSArchive_Revised_Flatfiles_20131001)

*Supplimentray*
* **state_abb.txt**: abbrebiation table for state name
* **national_county_code.txt**:  FIPS (Federal Information Processing Standard) code

# Make Prediction 
Based on financial data, expected hospital performance can be predicted using module <code>Prediction.py</code>
Expected performance is categorized in:

1. Better: better than national average
2. Nominal: national average
3. Worse: worse than national average

# How to Use <code>Prediction.py</code>
**Warning**: Please obtain API key from me to use the module. 

1. obtain API key
2. edit Prediction.py as noted in the file.
3. import Prediction.py
4. intiate with Prediction( ) with the inputs listed in **Input to Predictor**. The default values are all 0s.
5. make a prediction via Prediction_instance.result( ).
6. return predicted label and associated probabilities.

# Package Dependencies
* > Python 2.7 (not tested with Python 3).
* urllib2
* json 
* ast
* numpy 

# Input to Predictor
*Note*: Please look up state_code.txt for input **state**.

<table>
<tr>
  <th><b>Factor<b></th>
  <th><b>Input Name<b></th>
  <th><b>Data Type<b></th>
  <th><b>Value (min, max)<b<</th>
</tr>
<tr>
  <td>Annual Payroll (mean)</td>
  <td>APayroll_mean</td>
  <td>numeric</td>
  <td>(35, 600,000)<td>
</tr>
<tr>
  <td>Annual Payroll (standard deviation)</td>
  <td>APayroll_std</td>
  <td>numeric</td>
  <td>(100, 400)<td>
</tr>
<tr>
  <td>Establishment (mean)</td>
  <td>Establishment_mean</td>
  <td>numeric</td>
  <td>(2, 650)<td>
</tr>
<tr>
  <td>Establishment (standard deviation)</td>
  <td>Establishment_std</td>
  <td>numeric</td>
  <td>(1, 2,500)<td>
</tr>
<tr>
  <td>Healthcare expenditure by a county government</td>
  <td>county_health_exp</td>
  <td>numeric</td>
  <td>(300, 7,000,000)<td>
</tr>
<tr>
  <td>Median income of a household</td>
  <td>income</td>
  <td>numeric</td>
  <td>(24,000, 117,680)<td>
</tr>
<tr>
  <td>Municipal healthcare expenditure</td>
  <td>municipal_health_exp</td>
  <td>numeric</td>
  <td>(80, 1,800,000)<td>
</tr>
<tr>
  <td>Poverty</td>
  <td>pov</td>
  <td>numeric</td>
  <td>(1,600, 9,900,000)<td>
</tr>
<tr>
  <td>General revenue of a county government</td>
  <td>revenue</td>
  <td>numeric</td>
  <td>(18,000, 71,000,000)<td>
</tr>
<tr>
  <td>State code where a county belongs</td>
  <td>state</td>
  <td>numeric</td>
  <td>(1, 50)<td>
</tr>
</table>

# Contact
For any information, please contact Shoko (s.ryu (at) go.wustl.edu)



