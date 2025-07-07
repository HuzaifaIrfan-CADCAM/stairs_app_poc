
# https://www.mycarpentry.com/stair-calculator.html


from typing import Literal
import math

from pprint import pprint

# Manual Stair Calculator
# Input:
# Total Rise [A] (ex. 56.75)	
#  (in)	 
# Total Run [G] (ex. 90.5)	
#  (in)	 
# Number of Steps (Risers)	
 
# Tread Thickness [C]	
#  (in)
# stairCalc()

def stair_calculator(
    total_rise: float,
    total_run: float,
    num_steps: int,
    tread_thickness: float,
    mount_type: Literal["standard", "flush"] = "standard"
) -> dict:
    """
    Calculate stair dimensions based on input parameters.

    Args:
        total_rise: Total vertical height between floors (inches, 12-500)
        total_run: Total horizontal depth of stairway (inches, 12-1200)
        num_steps: Number of steps (2-200)
        tread_thickness: Thickness of each tread (inches, 0.5-4)
        mount_type: Stringer mount type ("standard" or "flush")

    Returns:
        Dictionary containing all calculated stair dimensions
    """

    print(f"stair_calculator total_rise:{total_rise} total_run:{total_run} num_steps:{num_steps} tread_thickness:{tread_thickness} mount_type:{mount_type}")
    # Validate inputs
    if not (12 <= total_rise <= 500):
        raise ValueError("Total Rise must be between 12 and 500 inches")
    if not (12 <= total_run <= 1200):
        raise ValueError("Total Run must be between 12 and 1200 inches")
    if not (2 <= num_steps <= 200):
        raise ValueError("Number of Steps must be between 2 and 200")
    if not (0.5 <= tread_thickness <= 4):
        raise ValueError("Tread Thickness must be between 0.5 and 4 inches")
    if mount_type not in ("standard", "flush"):
        raise ValueError("Mount Type must be either 'standard' or 'flush'")

    # Calculate basic dimensions
    if mount_type == "standard":
        num_treads = num_steps - 1
    else:
        num_treads = num_steps

    run_per_step = total_run / num_treads
    rise_per_step = total_rise / num_steps

    # Calculate stringer parameters
    if mount_type == "standard":
        stringer_parameter = rise_per_step + tread_thickness
    else:
        stringer_parameter = tread_thickness

    first_step_height = rise_per_step - tread_thickness

    # Calculate stringer length
    if mount_type == "standard":
        vertical = rise_per_step * (num_steps - 2) + first_step_height
        horizontal = run_per_step * (num_steps - 1)
    else:
        vertical = rise_per_step * (num_steps - 1) + first_step_height
        horizontal = run_per_step * num_steps

    stringer_length = math.sqrt(vertical**2 + horizontal**2)

    # Calculate angle
    angle_rad = math.atan(rise_per_step / run_per_step)
    angle_deg = math.degrees(angle_rad)

    # Prepare results
    results = {
        "total_rise": total_rise,
        "total_run": total_run,
        "num_steps_risers": num_steps,
        "tread_thickness": tread_thickness,
        "mount_type": mount_type,
        "rise_per_step": round(rise_per_step, 2),
        "run_per_step": round(run_per_step, 2),
        "first_step_riser_height": round(first_step_height, 2),
        "stringer_placement": round(stringer_parameter, 2),
        "stringer_length": round(stringer_length, 2),
        "stair_angle": round(angle_deg, 1),
        "num_treads": num_treads,
    }

    return results






# Automatic Stair Calculator

# Input:
# Total Rise [A] (ex: 56.75)	
#  (in)	
# Target Step Height [F]	
# 7.00
#  (in)	 
# Tread Thickness [C]	
# 1.50
#  (in)	
# Tread Depth [B]	
# 10.5
#  (in)
# AutoCalcStairRise()


def auto_stair_calculator(
    total_rise: float,
    step_height: float,
    tread_thickness: float,
    tread_depth: float,
    mount_type: Literal["standard", "flush"] = "standard"
) -> dict:
    """
    Automatically calculate stair dimensions based on optimal step height.
    
    Args:
        total_rise: Total vertical height between floors (inches, 12-500)
        step_height: Optimal step height (inches)
        tread_thickness: Thickness of each tread (inches, 0.5-4)
        tread_depth: Depth of each tread (inches)
        mount_type: Stringer mount type ("standard" or "flush")
        
    Returns:
        Dictionary containing all calculated stair dimensions
    """
    print(f"auto_stair_calculator total_rise:{total_rise} step_height:{step_height} tread_thickness:{tread_thickness} tread_depth:{tread_depth} mount_type:{mount_type}")
    # Validate inputs
    if not (12 <= total_rise <= 500):
        raise ValueError("Total Rise must be between 12 and 500 inches")
    if step_height <= 0:
        raise ValueError("Step height must be positive")
    if not (0.5 <= tread_thickness <= 4):
        raise ValueError("Tread Thickness must be between 0.5 and 4 inches")
    if tread_depth <= 0:
        raise ValueError("Tread depth must be positive")
    if mount_type not in ("standard", "flush"):
        raise ValueError("Mount Type must be either 'standard' or 'flush'")

    # Calculate number of steps
    raw_num_steps = total_rise / step_height
    integer_part = int(raw_num_steps)
    fractional_part = raw_num_steps - integer_part
    
    if fractional_part >= 0.5:
        num_steps = integer_part + 1
    else:
        num_steps = integer_part
    
    actual_step_height = total_rise / num_steps
    
    # Calculate number of treads based on mount type
    if mount_type == "standard":
        num_treads = num_steps - 1
    else:
        num_treads = num_steps
    
    # Calculate first step height
    first_step_height = actual_step_height - tread_thickness
    
    # Calculate stringer parameters
    if mount_type == "standard":
        last_step_parameter = actual_step_height + tread_thickness
    else:
        last_step_parameter = tread_thickness
    
    # Calculate total run
    if mount_type == "standard":
        total_run = num_treads * tread_depth
    else:
        total_run = num_steps * tread_depth
    
    # Calculate stringer length
    if mount_type == "standard":
        vertical = actual_step_height * (num_steps - 2) + first_step_height
        horizontal = tread_depth * (num_steps - 1)
    else:
        vertical = actual_step_height * (num_steps - 1) + first_step_height
        horizontal = tread_depth * num_steps
    
    stringer_length = math.sqrt(vertical**2 + horizontal**2)
    
    # Calculate stair angle
    angle_rad = math.atan(actual_step_height / tread_depth)
    angle_deg = math.degrees(angle_rad)
    
    # Prepare results
    results = {
        "total_rise": total_rise,
        "optimal_step_riser_height": step_height,
        "actual_step_riser_height": round(actual_step_height, 2),
        "num_steps_risers": num_steps,
        "num_treads": num_treads,
        "tread_thickness": tread_thickness,
        "tread_depth": tread_depth,
        "mount_type": mount_type,
        "first_step_riser_height": round(first_step_height, 2),
        "stringer_placement_last_step_parameter": round(last_step_parameter, 2),
        "total_run": round(total_run, 2),
        "stringer_length": round(stringer_length, 2),
        "stair_angle": round(angle_deg, 1),
    }
    
    return results



def main():
    print("Hello from stair-calculator!")


    result = auto_stair_calculator(
        total_rise=120,
        step_height=8.5,
        tread_thickness=2.5,
        tread_depth=12.0,
        mount_type="flush"
    )
    pprint(result)

if __name__ == "__main__":
    main()
