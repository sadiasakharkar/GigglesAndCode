from orbit_simulator import plot_orbits, plot_space_missions, plot_sky_map_option

def main():
    print("Welcome to the Solar System Simulator!")
    print("Choose an option:")
    print("1. 3D Orbit Visualization")
    print("2. Interactive Orbit Visualization")
    print("3. Track Space Missions (Mars Rover Example)")
    print("4. Customizable Time Range for Orbit Visualization")
    print("5. Animate Orbits")
    print("6. Sky Map Visualization")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        plot_orbits()
    elif choice == '2':
        plot_interactive_orbits()
    elif choice == '3':
        plot_space_missions()
    elif choice == '4':
        plot_orbit_time_range()
    elif choice == '5':
        animate_orbits()
    elif choice == '6':
        plot_sky_map_option()
    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
