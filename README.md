# nernst_ghk
A Python-based oscilloscope simulator for the Nernst and Goldman-Hodgkin_Katz equations

Dependcies: matplotlib (and anything that matplotlib depends on). You also need an interactive backend. (e.g., apt install python3-tk). 

Based on https://matplotlib.org/stable/gallery/animation/strip_chart.html and lots of consultation with ChatGPT :)

Dec 3, 2023: ver. 0.1 uploaded (ghk.py). Shows a plot of membrane potential (Vm) as a function of Na, K, and Cl ion intracellular and extracellular concentrations, which can all be altered using interactive sliders. Other parameters that can be changed include relative permeability and temperature. Also shows real time updates of equilibrium potentials of each ion. 

Nov. 30, 2023: first version (nernst_k.py) works! This is a Nernst equation simulator that will plot the equilibrium potential of K+ (potassium cations) based on K[in] and K[out] values that the user can change via interactive sliders. 
