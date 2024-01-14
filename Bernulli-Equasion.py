import math

def calculate_flow_rate(p1, p2, density, area, viscosity):
    """
    Calculate fluid flow rate using Bernoulli's equation.

    :param p1: Initial pressure (Pa)
    :param p2: Final pressure (Pa)
    :param density: Fluid density (kg/m^3)
    :param area: Cross-sectional area of the flow (m^2)
    :param viscosity: Fluid viscosity (Pa*s)
    :return: Flow rate (m^3/s)
    """
    if None in (p1, p2, density, area, viscosity):
        # Calculate the missing parameter, if possible
        if p1 is None:
            p1 = p2 + (8 * viscosity * flow_rate) / (math.pi * area**4)
        elif p2 is None:
            p2 = p1 - (8 * viscosity * flow_rate) / (math.pi * area**4)
        elif density is None:
            # Density is needed to calculate flow rate, so we can't proceed without it
            return None
        elif area is None:
            # Area is needed to calculate flow rate, so we can't proceed without it
            return None
        elif viscosity is None:
            # Viscosity is needed to calculate flow rate, so we can't proceed without it
            return None

    delta_p = p1 - p2
    flow_rate = (math.pi * delta_p * area**4) / (8 * viscosity)
    return flow_rate

def main():
    # Input parameters
    p1 = float(input("Enter initial pressure (Pa, or None if unknown): ") or "None")
    p2 = float(input("Enter final pressure (Pa, or None if unknown): ") or "None")
    density = float(input("Enter fluid density (kg/m^3, or None if unknown): ") or "None")
    area = float(input("Enter cross-sectional area (m^2, or None if unknown): ") or "None")
    viscosity = float(input("Enter fluid viscosity (Pa*s, or None if unknown): ") or "None")

    # Calculate flow rate
    flow_rate = calculate_flow_rate(p1, p2, density, area, viscosity)

    if flow_rate is not None:
        print(f"Fluid Flow Rate: {flow_rate} m^3/s")
    else:
        print("Insufficient information to calculate flow rate.")

if __name__ == "__main__":
    main()

