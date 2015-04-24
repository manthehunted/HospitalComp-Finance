# HospitalComp-Finance
##Objectives
This is a preliminary prediction analysis of hospital performance (county-wise) based on regional financial status, Year 2012.  Data is obtained from [census.gov](http://www.census.gov/) and [medicare.gov](http://www.medicare.gov/).

#### Data contained in folder, *data* 
*Finance Related*
* **COG_2012_LGF002.csv**: local government finances by type of government and state (found in folder, COG_2012_LGF002).
* **cbp12co.txt**: county business pattern (available [here](https://www.census.gov/econ/cbp/download/)).
* **allpovu_copy.csv**: Estimated population in poverty universe.
* **est13ALL_copy.csv**: Poverty and Median Household Income Estimates.

*Hospital Related*
* **Outcome of Care Measures.csv**: outcome of care measure per hospital (found in folder, HOSArchive_Revised_Flatfiles_20131001).

*Supplimentray*
* **state_abb.txt**: abbrebiation table for state name.
* **national_county_code.txt**:  FIPS (Federal Information Processing Standard) code.

# Make Prediction - 3 Categories
Based on financial data, expected hospital performance can be predicted using module <code>Prediction.py</code>.

Expected performance is categorized in:

1. Better: better than national average
2. Nominal: national average
3. Worse: worse than national average

# How to Use <code>Prediction.py</code>
**Warning**: Please obtain API key from me to use the module. 

1. obtain API key.
2. edit Prediction.py as noted in the file.
3. import <code>Prediction.py</code>
4. intiate with Prediction( ) with the inputs listed in section, **Input to Predictor**. The default values are all 0s.
5. make a prediction via *prediction_instance*.result( ).
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
  <th><b>Input Name<b></th>
  <th><b>Description<b></th>
  <th><b>Data Type<b></th>
  <th><b>Unit<b></th>
  <th><b>Value (min, max)<b<</th>
</tr>
<tr>
  <td>APayroll_mean</td>
  <td>Annual Payroll (mean)</td>
  <td>numeric</td>
  <td>$1,000</td>
  <td>(35, 600,000)<td>
</tr>
<tr>
  <td>APayroll_std</td>
  <td>Annual Payroll (standard deviation)</td>
  <td>numeric</td>
  <td>($1,000)<sup>2</sup></td>
  <td>(100, 400)<td>
</tr>
<tr>
  <td>Establishment_mean</td>
  <td>Establishment (mean)</td>
  <td>numeric</td>
  <td>Count</td>
  <td>(2, 650)<td>
</tr>
<tr>
  <td>Establishment_std</td>
  <td>Establishment (standard deviation)</td>
  <td>numeric</td>
  <td>(Count)<sup>2</sup></td>
  <td>(1, 2,500)<td>
</tr>
<tr>
  <td>county_health_exp</td>
  <td>Healthcare expenditure by a county government</td>
  <td>numeric</td>
  <td>$1,000</td>
  <td>(300, 7,000,000)<td>
</tr>
<tr>
  <td>income</td>
  <td>Median income of a household</td>
  <td>numeric</td>
  <td>$1</td>
  <td>(24,000, 117,680)<td>
</tr>
<tr>
  <td>municipal_health_exp</td>
  <td>Municipal healthcare expenditure</td>
  <td>numeric</td>
  <td>$1,000</td>
  <td>(80, 1,800,000)<td>
</tr>
<tr>
  <td>pov</td>
  <td>Poverty</td>
  <td>numeric</td>
  <td>population</td>
  <td>(1,600, 9,900,000)<td>
</tr>
<tr>
  <td>revenue</td>
  <td>General revenue of a county government</td>
  <td>numeric</td>
  <td>$1,000</td>
  <td>(18,000, 71,000,000)<td>
</tr>
<tr>
  <td>state</td>
  <td>State code where a county belongs</td>
  <td>numeric</td>
  <td>N/A</td>
  <td>(1, 50)<td>
</tr>
</table>

# Contact
For any information, please contact Shoko (s.ryu (at) go.wustl.edu)



