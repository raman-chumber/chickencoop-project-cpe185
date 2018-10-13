# README #

This repo is project for CPE 185 (Computer Interfacing) lab for Spring 2018 at Sac State University. This project involves designing and implementing a Smart Chicken Coop. The design requires sensors and communication systems to make it easy for someone who has limited time or experience to be able to house chickens safely. 
1. Temperature sensor will use controllers to determine the intensity of heat lamps.
2. Flow sensor that will be placed in conjunction with the automatic waterer to determine if there is a leak or a clog in the system.
3. Roof mounted solar panels that will charge a battery system to power all of these devices.
4. Weight sensor that when properly calibrated will inform the user if there is an egg.
5. Smoke detector that will activate a small sprinkler off of the waterer’s supply if smoke is detected as a fire safety device if the heat lamps fail. 
6. Motor will be used to spin an arm that spreads feed out at specified times.

# Video Demonstrations [click to view](https://youtu.be/nDml8yVoEi4)

## Main Sub-Functions ##

### 3.1 Water supply, feeder, and solar power system – Ramandeep ###
This part of the lab will control the active components. There will be the monitoring of the water
flow, which will change a valves position if too much or not enough water is flowing in a certain period. The next will be the feeder which will at specified times spread food out via a motor. The feed supply will be in a weighed compartment that will notify the owner the approximate % of food remaining. The final piece will be the solar system, which will include a sensor that informs the user about voltage of batteries.

### 3.2 Raspberry pi and web page – Gabriel Dominguez ###
The raspberry pi will be used to communicate with all the sensors. The pi will be used to create a web page that will update the user about if eggs have been laid as well as the status of food level, water flow, and temperature and humidity of the coop.
 
### 3.1 Weight sensor and construction – Justin Ellis ###
The weight sensor will require a specific change after a weight has been applied and removed to determine if an egg has been laid. There will have to be testing done so that there are no false positives from bedding. Also the construction of the physical coop.
