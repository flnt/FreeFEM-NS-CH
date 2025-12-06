# Withdrawing Plate Simulation

## Overview

This FreeFEM solver simulates a 2D withdrawing plate problem where a flat liquid-gas interface deforms as the left boundary moves upward with velocity `V_s = sqrt(Ca)`. The simulation tracks the contact line position on the left wall over time.

## Files

- **PFsolver_NSandCH_withdrawingPlate.edp** - Main FreeFEM solver
- **include_postProc.idp** - Postprocessing utilities
- **data/** - Output directory for results

## Key Features

✓ **Flat initial interface** at y = 3.5  
✓ **Moving left wall** with velocity V_s ≈ 0.374 upward  
✓ **Gravity** acting downward (grav = -1.25)  
✓ **Square domain** 10 × 10  
✓ **Optimized for speed** - larger time step, coarser mesh, less frequent adaptation  
✓ **Wetting boundary condition** on left wall (90° contact angle)  
✓ **Contact line tracking** - extracts y-position on left boundary  
✓ **Mesh adaptivity** - automatic refinement at the interface  
✓ **No-slip right wall** - for proper meniscus formation  

## Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Ca | 0.14 | Capillary number |
| eps (Cn) | 0.05 | Cahn number (interface thickness) |
| angle_eq | π/2 | Equilibrium contact angle (90°) |
| V_s | sqrt(Ca) ≈ 0.374 | Withdrawal velocity |
| L | 10.0 | Domain width (square) |
| h₀ | 10.0 | Domain height (square) |
| yInterface | 3.5 | Initial interface position |
| grav | -1.25 | Gravity (downward) |
| dt | 0.005 | Time step (optimized) |
| tfin | 10.0 | Final time |
| n | 7 | Mesh resolution (optimized) |
| dref | 50 | Mesh adapt frequency (optimized) |

## Running the Simulation

```bash
cd /home/tf/FreeFEM-NS-CH/withdrawingPlate
FreeFem++ PFsolver_NSandCH_withdrawingPlate.edp
```

## Output

- **stats.txt** - Contact line position vs time (t, y_CL)
- **data/out_*.vtk** - VTK files for ParaView visualization
- **data/out_*.msh** - Mesh files
- **data/out_*.dat** - Solution data for restart

## Expected Physics

The simulation models the dynamic balance between:
- **Wall motion** pulling the contact line upward
- **Gravity** pulling the interface downward  
- **Surface tension** and **wetting** setting the contact angle

The contact line should rise over time, forming a meniscus near the left wall while the bulk interface remains relatively flat.

## Boundary Conditions

| Boundary | Label | BC Type | Values |
|----------|-------|---------|--------|
| Bottom | 1 | No-slip | u=0, v=0 |
| Right | 2 | No-slip | u=0, v=0 |
| Top | 3 | Stress-free | Neumann |
| Left | 4 | Moving wall | u=0, v=V_s |

**Wetting BC** applied on labels 1 (bottom) and 4 (left wall) with zero contact line friction.

## Contact Line Extraction

The contact line position is found by binary search for the y-coordinate where `c(0,y) = 0` on the left boundary (x=0). Updated every time step and saved to `stats.txt`.
