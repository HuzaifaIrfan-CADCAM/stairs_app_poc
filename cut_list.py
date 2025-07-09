
from pdf_tools import create_cut_list


def main():
    print("Hello from stair-manufacturing!")


    cut_list_data = [
        ["Part", "Qty", "Material", "Dimension"],
        ["Treads", "15", '1" Plywood', '36 3/4"'],
        ["Risers", "15", '3/8" Plywood', '36 3/4"'],
        ["Top Riser", "1", '5/8" Plywood', '36 3/4"'],
        ["Stringers", "2", 'LSL or 2x12', '122"'],
    ]

    create_cut_list(output_folder="output/", job_name="Crestmont", builder_name="admi", total_rise="122", width="36 3/4",riser_height="7 5/8", num_riser="16", num_tread="15", tread_depth="11 1/2", total_run="172 1/2",cut_list_data=cut_list_data)

if __name__ == "__main__":
    main()
