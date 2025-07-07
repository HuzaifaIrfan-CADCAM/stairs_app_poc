

from stair_calculator import auto_stair_calculator, stair_calculator


from pprint import pprint

def main():
    print("Hello from stair-manufacturing!")

    result = auto_stair_calculator(
        total_rise=122,
        step_height=7.625,
        tread_thickness=1.0,
        tread_depth=11.5,
        mount_type="standard"
    )
    result["width_stair"] =36.75
    pprint(result)


if __name__ == "__main__":
    main()
