There are 5 folders containing the next files:

1_geom_opt - Geometry optimization of an HBQ molecule
	HBQ.inp - CP2K input file
	HBQ.coord - initial geomerty of HBQ
	BASIS - file with cc-TZ basis functions for H, C, O and N
	POTENTIALS - PBE potentials for the same elements

2_GS_traj - Ground state trajectory
	input.ceon - NEXMD input file

3_single_point - Single point calculations
	header - generator of the input files for single point calculations

4_NAMD - Non-adiabatic molecular dynamics
	header - generator of the input files for NAMD calculations

5_Strong_coupling
	HBQ_neutral.inp - CP2K input file for a neutral HBQ molecule
	HBQ.inp	- CP2K input file for a HBQ anion
        BASIS - file with cc-TZ basis functions for H, C, O and N
        POTENTIALS - PBE potentials for the same elements
	Strong_coupling.ipynb - Jupyter Notebook file for creaction the energy profiles along the reaction coordinate under strong coupling
	energy_ground_exc.txt - energy profiles (ground, excited)
