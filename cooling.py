def calculate_cooling_load(building_type, occupants):
    if building_type.lower() == "residential":
        cooling_load = 100 * occupants
    elif building_type.lower() == "commercial":
        cooling_load = 150 * occupants
    else:
        raise ValueError("Invalid building type. Supported types are 'residential' and 'commercial'.")
    return cooling_load

def calculate_sensible_cooling_load(area, outdoor_temp, indoor_temp, building_type, occupants):
    u = 30  

   
    q_conduction = u * area * (outdoor_temp - indoor_temp)


    cooling_load = calculate_cooling_load(building_type, occupants)


    sensible_cooling_load = q_conduction + cooling_load

    return sensible_cooling_load

def main():
    try:
        area = float(input("Enter the area of the building (in square meters): "))
        occupants = int(input("Enter the number of occupants in the building: "))
        building_type = input("Enter the type of building (residential/commercial): ")
        outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
        indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))

        sensible_cooling_load = calculate_sensible_cooling_load(area, outdoor_temp, indoor_temp, building_type, occupants)

        print(f"The sensible cooling load for the building is {sensible_cooling_load} Watts.")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()