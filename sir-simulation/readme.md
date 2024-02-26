
# Overview

These scripts can be used to generate a random geometric graph that can be supplied to a simulation of the SIR epidemic model. Additionally, the diameter of the generated graph can be approximated.

## Environment

The code is written in Python and requires at least Python 3.8.
Jupyter notebook is required to execute the included scripts for visualization.
The code was tested with Python 3.8.0 and Jupyter Notebook 7.1.0

# Usage
## First: Generate A Random Geometric Graph

### Step 1 -- Place Nodes

First, we randomly place our $n$ points on the play field (square with side length $\sqrt{n}$) by executing

```
py generate-nodes.py n k
```

where $k$ represents the number of points which are initially marked as infected 
(only relevant for the SIR simulation later on -- for diameter computation an arbitary value may be selected e.g., 1).
We note that these $k$ points are the ones that are the nearest to the middle of the play field. 
This command creates a file called 'points' which can be supplied as an input in the following step.

### Step 2 -- Insert Edges

After generating the nodes on our play field, we can now generate a random geometric graph by using

```
py generate-links.py input_points_file n r a include_long_range
```

The parameters are described by:
- $n$: number of points
- $r$: radius
- $a$: alpha
- $include$ \_ $long$ \_ $range$: either 0 or 1 to specify whether long-range edges should be generated or not

## Execute the SIR Simulation

A SIR simulation on a generated geometric graph can be executed by issuing the following command:

```
py sir-simulation.py graph_input_file n alpha beta gamma u
```

where $\alpha$ is the long-range parameter of the given graph, $\beta$ is the probability for an infectious node to infect a random neighbour if it is susceptible and $\gamma$ represents the probability that an infectious node recovers after each simulation round. 
The parameter $u$ specifies how often the SIR simulation should be repeated. 
The program outputs the number of rounds required to reach an outbreak ($\geq0.3$ fraction of all nodes in (I)nfective or \(R\)ecovered state) or $\infty$ in case no outbreak is reached.

## Compute Graph Diameter

Approximates the diameter of a given random geometric graph by executing the $4$-Sweep algorithm

```
py graph-diameter.py graph_input_file u
```

The $u$ parameter specifies the number of times the $4$-Sweep algorithm is repeated.
Larger values increase the accuracy of the approximation. 
We used $u=30$, however, smaller values also work for testing purposes.


# Visualization

## SIR Simulation

The file `sir-simulation-3d-visualization.ipynb` may be used to generate the 3-D plot presented in the Supplementary Information of the paper. It displays the number of rounds required for an outbreak for various combinations of $\alpha$ and $\beta$.  
As an input it requires a .csv file with the outcome of multiple SIR simulation runs, created following the approach outlined above. The file `sir-simulation-results.csv` contains the data we obtained throughout our experiments and is also included in the directory. We considered a geometric graph with $n=1,000,000$ nodes and radius $r=1.5$ as well as $k=20$ initially infected nodes. The parameter $\gamma$ was fixed to $0.3$ in all runs.

## Diameter

We used the file `graph-diameters.ipynb` to generate a figure illustrating how the diameter of a random geometric graph changes when supplied with long-range edges that follow the parameter $\alpha$.
As an input it requires a .csv file that lists diameters for the $\alpha$ values of interest. The values generated in our experiments can be found in `graph-diameters.csv`. We considered a graph of $n=1,000,000$ nodes and performed 30 runs of the $4$-sweep algorithm for each $\alpha$.


