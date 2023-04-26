<!DOCTYPE html>
<html>
<head>
	<title>Random-Search-for-Optimization</title>
</head>
<body>
	<h1>Random-Search-for-Optimization</h1>
	<p>Random search (RS) is a family of numerical optimization methods that do not require the gradient of the problem to be optimized. This repository contains the implementation in Python of various optimization algorithms:</p>
	<ul>
		<li>Linear Regression with Simulated Annealing</li>
		<li>Particle Swarm Optimization for Linear Regression</li>
		<li>TSP using Genetic Algorithm</li>
		<li>TSP using Nearest Neighbor Algorithm</li>
		<li>TSP using Simulated Annealing Algorithm</li>
	</ul>
	<h2>Pre-Installed Packages</h2>
	<p>The following packages need to be pre-installed before running the code:</p>
	<ol>
		<li>gifsicle: To create animated GIFs of the optimization process.</li>
		<p><code>sudo apt install gifsicle</code></p>
		<li>imagemagick: To create an image of the optimization process.</li>
		<p><code>sudo apt install imagemagick</code></p>
	</ol>
	<h2>How to Use</h2>
	<p>Clone the repository</p>
	<pre><code>git clone https://github.com/&lt;username&gt;/Random-Search-for-Optimization.git</code></pre>
	<p>Navigate to the directory</p>
	<pre><code>cd Random-Search-for-Optimization</code></pre>
	<p>Install the required packages</p>
	<pre><code>pip install -r requirements.txt</code></pre>
	<p>Run the Python scripts</p>
	<pre><code>python linear_regression_simulated_annealing.py</code></pre>
	<pre><code>python linear_regression_particle_swarm_optimization.py</code></pre>
	<pre><code>python tsp_genetic_algorithm.py</code></pre>
	<pre><code>python tsp_nearest_neighbor_algorithm.py</code></pre>
	<pre><code>python tsp_simulated_annealing_algorithm.py</code></pre>
	<h2>Examples</h2>
	<p>Here's an example of running the TSP using Simulated Annealing Algorithm:</p>
	<p>Navigate to the directory</p>
	<pre><code>cd Random-Search-for-Optimization</code></pre>
	<p>Run the Python script</p>
	<pre><code>python tsp_simulated_annealing_algorithm.py</code></pre>
	<p>The program will output an animated GIF file called tsp_simulated_annealing.gif and an image file called tsp_simulated_annealing.png showing the optimization process.</p>
	<img src="tsp_simulated_annealing.gif">
</body>
</html>
