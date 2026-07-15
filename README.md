# Orbital-Calculator
A Python tool used to calculate basic orbital metrics for equatorial circular orbits using the vis-viva equation.

## What it does

Given an orbital altitude above Earth's equator, this calculator outputs:
- Orbital velocity (m/s and km/h)
- Orbital period (hours and minutes)

## Physics

This calculator uses the vis-viva equation to determine orbital velocity.

**v = √(GM/r)**

Where:
- G = gravitational constant (6.67×10⁻¹¹ m³/(kg·s²))
- M = Earth's mass (5.972×10²⁴ kg)
- r = orbital radius (Earth's radius + altitude)

With velocity and orbital circumference, we calculate the period: **T = 2πr / v**

## How to Use

Run the script: 
```bash
python orbital_calculator.py
```
When prompted, enter an altitude in meters. Example: 

Orbital Altitude (m): 200000

```bash
---Orbital Metrics at 200km---
  
  Orbital Velocity: 7781.73 m/s (28014.21 km/h)

  Orbital Period: 1.5 hours (88.5 minutes)
```
## Validation

This calculator has been validated against real orbital data:

| Orbit | Altitude | Calculator Output | Actual | Error |
|-------|----------|-----------|--------|-------|
| ISS | 200 km | 7,781 m/s | 7,661 m/s | 1.57% |
| GEO | 35,786 km | 3,073 m/s | 3,075 m/s | 0.07% |

## Limitations

- Assumes circular equatorial orbits only
- Ignores atmospheric drag, solar radiation pressure, and gravitational perturbations
- Uses mean Earth radius; real orbits vary by latitude
- Does not account for Earth's oblateness (J2 perturbations)

## Future Improvements

- Add Hohmann transfer calculations (delta-v between two orbits)
- Support inclined orbits
- Validate against simulations
