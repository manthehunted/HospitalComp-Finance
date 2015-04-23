# HospitalComp-Finance
This is a preliminary analysis of hospital readmission rate (county-wise) based on regional financial status.  Data is taken from [data.gov](http://www.data.gov/).

### Contained data in folder, *data* 
* **state_abb.txt**: abbrebiation table for state name
* **national_county_code.txt**:  FIPS (Federal Information Processing Standard) code
* **allpovu_copy.csv**: Estimated population in poverty universe
* **est13ALL_copy.csv**: Poverty and Median Household Income Estimates
* **Outcome of Care Measures.csv**: outcome of care measure per hospital (found in folder, HOSArchive_Revised_Flatfiles_20131001)
* **COG_2012_LGF002.csv**: local government finances by type of government and state (found in folder, COG_2012_LGF002)
* **cbp12co.txt**: county business pattern (available [here](https://www.census.gov/econ/cbp/download/))


# Input to Predictor


<table>
<tr>
  <td><b>Factor<b></th>
  <td><b>Input Name<b></th>
  <td><b>Data Type<b></th>
</tr>
<tr>
  <td>Annual Payroll (mean)</td>
  <td>APayroll</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Annual Payroll (standard deviation)</td>
  <td>APayroll_std</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Establishment (mean)</td>
  <td>Establishment_mean</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Establishment (standard deviation)</td>
  <td>Establishment_std</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Healthcare expenditure by a county government</td>
  <td>county_health_exp</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Median income of a household</td>
  <td>income</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Municipal healthcare expenditure</td>
  <td>municipal_health_exp</td>
  <td>numeric</td>
</tr>
<tr>
  <td>Poverty</td>
  <td>pov</td>
  <td>numeric</td>
</tr>
<tr>
  <td>General revenue of a county government</td>
  <td>revenue</td>
  <td>numeric</td>
</tr>
<tr>
  <td>State where a county belongs</td>
  <td>state</td>
  <td>Categorical</td>
</tr>
</table>





