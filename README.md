# Intracellular Transport Simulation

## Overview
This project simulates the **intracellular transport mechanisms** of motor proteins such as **kinesin**, **dynein**, and **myosin**. These motor proteins move along **cytoskeletal tracks** (microtubules for kinesin and dynein, actin filaments for myosin) to transport cargo within the cell. The simulation models these proteins’ dynamics, ATP consumption, interactions with cytoplasmic obstacles (crowding), and bidirectional motion as a result of tug-of-war dynamics between motors. 

This model provides insights into how cellular transport operates under different conditions, such as varying levels of cytoplasmic crowding, obstacle presence, and energy availability.

---

## Why This is Important

Intracellular transport is crucial for cellular function and is vital for:
- **Organelle positioning**: Proper functioning of cells depends on efficient transport of vesicles, organelles, and protein complexes.
- **Neuronal function**: In neurons, transport over long distances (e.g., along axons) is necessary for cell communication and survival.
- **Disease models**: Transport dysfunction is implicated in diseases like Alzheimer's, Huntington's, and ALS. Understanding how motors behave under different conditions could yield insights into treatment strategies.

By simulating these transport dynamics, this project helps us explore:
- **Energy efficiency**: How ATP consumption varies under different transport conditions.
- **Cytoplasmic crowding**: The effects of a crowded cellular environment on motor protein efficiency and transport speed.
- **Bidirectional transport**: How motors compete in tug-of-war scenarios, such as kinesin and dynein moving cargo in opposite directions.

---

## How It Works

### **Key Functionality**:

### 1. **Motor Protein Simulation**:
- The program simulates three types of motor proteins:
  - **Kinesin**: Moves along microtubules toward the positive end (outward from the nucleus).
  - **Dynein**: Moves along microtubules toward the negative end (toward the nucleus).
  - **Myosin**: Operates along actin filaments.
  
- Each motor protein has properties such as:
  - **Speed**: How fast the motor moves along the cytoskeletal track.
  - **Step size**: The distance covered per step (e.g., kinesin takes steps of 8 nm).
  - **ATP consumption**: The amount of energy consumed for each step.

### 2. **Cytoskeletal Tracks**:
- The simulation has two types of tracks:
  - **Microtubules** for kinesin and dynein.
  - **Actin filaments** for myosin.

- The motor proteins bind to these tracks and move stochastically based on their properties.

### 3. **ATP Consumption**:
- ATP is the energy source for motor protein movement. The simulation tracks how much ATP each motor consumes over time. This helps visualize energy usage during transport, particularly under different conditions such as cytoplasmic crowding or collisions.

### 4. **Cytoplasmic Crowding**:
- The simulation introduces obstacles on the cytoskeletal tracks to simulate a crowded intracellular environment.
- Motors that encounter obstacles will change direction or be delayed. This feature models the complexity of real cellular environments, where motor proteins are rarely moving in isolation.

### 5. **Bidirectional Transport**:
- The program models the tug-of-war dynamics between kinesin and dynein, as they often pull in opposite directions. This is a real phenomenon in cellular transport where multiple motor proteins can be attached to the same cargo.

### **How to Use the Simulation**:

1. Install the necessary dependencies:
    ```bash
    pip install numpy matplotlib
    ```

2. Run the simulation with the following command:
    ```bash
    python src/simulation/motor_protein_dynamics_with_actin.py
    ```

3. Adjust parameters such as the number of simulation steps, track length, or the number of obstacles to observe different behaviors.

### **Visualization**:
- The simulation outputs a **plot showing ATP consumption** over time for each motor protein. This helps visualize how efficiently motor proteins use energy while transporting cargo across the cytoplasm.

---

## Example Scenario

Let’s say we want to observe how motors respond to cytoplasmic crowding. In this scenario:
- **Kinesin** will move outward from the nucleus along a microtubule.
- **Dynein** will pull the cargo in the opposite direction.
- **Myosin** moves along actin filaments.
  
The simulation introduces obstacles along the tracks, and the motors will either reverse direction or be delayed when they encounter these obstacles. The output will show how much energy each motor consumed during the simulation and provide insights into how the crowded environment impacted their efficiency.

---

## Improvements for Future Iterations

While this project already covers the basics of intracellular transport, there are several potential improvements:

### 1. **Advanced Collision Handling**:
- Currently, when a motor encounters an obstacle, it reverses direction. Future iterations could model more complex behavior, such as rerouting around obstacles or experiencing temporary delays before continuing.

### 2. **Force-Based Dynamics**:
- Instead of simple stochastic binding and unbinding, future iterations could introduce **force-based models** where the cargo experiences forces from multiple motors. This would allow for more accurate modeling of tug-of-war dynamics and load sharing between motors.

### 3. **Multiple Cargo Types**:
- Extend the model to simulate transport of multiple cargo types (e.g., vesicles, organelles) with different sizes, shapes, and transport requirements. Each type could experience different crowding effects and force dynamics.

### 4. **Realistic Cytoplasmic Environments**:
- Add features such as **viscous drag** or **variable cytoplasmic density**, which would affect motor movement in a more realistic manner.
  
### 5. **Disease Models**:
- Model specific mutations or defects in motor proteins to simulate diseases like Huntington’s or ALS, where transport is disrupted. These models could help explore how defective transport mechanisms lead to cellular dysfunction.

### 6. **3D Transport**:
- Currently, the simulation operates in 1D along predefined tracks. Future versions could simulate **3D transport** within the cell, modeling more complex interactions between motors and cytoskeletal structures.

---

## Contributing

Feel free to fork the repository and submit pull requests. We welcome contributions, whether for bug fixes, new features, or improvements to existing code.

---

## License

This project is licensed under the MIT License.
