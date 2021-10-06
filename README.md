# NASAL CANNULA DATA  
  
Data and plots of variation of various parameters (SFM, DP, Prediction, PWM duty cycle) for different venturis and nasal cannulas are stored in this repository. Each folder in this repo. is named after the code of the venturi used. Inside each such folder will be multiple folders which are named after the cannula which has been used and will contain raw data collected during the operation of the circuit (named data.txt). The circuit is as follows:  <br/>
  
Laptop<->Mega->blower->venturi->connector->SFM4200->output  
<br/>
  
## List of venturis used  
  
|CODE             |     p1 (slope)     |     p2 (intercept)     |
|-----------------|-------------------:|-----------------------:|
|PK041021-G01     |4.47                |-0.56                   |
|PK041021-TW01    |2.86                |-0.49                   |  
  
For plotting individual plots, use plotter.py. For plotting and comparing various curves in one go, use subplotter.py. Its result will get stored in a folder named REPORT. 