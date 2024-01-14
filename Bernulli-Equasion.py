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
    delta_p = p1 - p2
    flow_rate = (math.pi * delta_p * area**4) / (8 * viscosity)
    return flow_rate

def main():
    # Input parameters
    p1 = float(input("Enter initial pressure (Pa): "))
    p2 = float(input("Enter final pressure (Pa): "))
    density = float(input("Enter fluid density (kg/m^3): "))
    area = float(input("Enter cross-sectional area (m^2): "))
    viscosity = float(input("Enter fluid viscosity (Pa*s): "))

    # Calculate flow rate
    flow_rate = calculate_flow_rate(p1, p2, density, area, viscosity)

    print(f"Fluid Flow Rate: {flow_rate} m^3/s")

if __name__ == "__main__":
    main()
