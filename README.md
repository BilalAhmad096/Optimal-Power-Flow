# Optimal-Power-Flow

Distribution System Optimal Power Flow

This repository contains code for performing optimal power flow (OPF) analysis on a 5-bus distribution system using pandapower.

## Overview

This project implements an optimal power flow solution for a small distribution system with 5 buses. It utilizes the pandapower library to model the network and solve the OPF problem.

## Features

- Models a 5-bus distribution system
- Performs optimal power flow analysis
- Uses pandapower for network modeling and OPF solution

## Requirements

- Python 3.7+
- pandapower
- numpy
- matplotlib (for visualization, if applicable)

## Installation

1. Clone this repository:

2. Install the required packages:

## Usage

Run the main script to perform the OPF analysis:

## Structure

- `main.py`: Main script to run the OPF analysis
- `network_model.py`: Contains the 5-bus network model
- `opf_solver.py`: Implements the OPF solver using pandapower
- `utils.py`: Utility functions for data processing and visualization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pandapower](https://www.pandapower.org/) - Power System Modeling and Analysis Tool
