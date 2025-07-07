

from stair_calculator import auto_stair_calculator, stair_calculator


from pprint import pprint

def main():
    print("Hello from stair-manufacturing!")

    result = auto_stair_calculator(
        total_rise=120,
        step_height=7.5,
        tread_thickness=1.0,
        tread_depth=10.0,
        mount_type="standard"
    )
    pprint(result)

if __name__ == "__main__":
    main()
