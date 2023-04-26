<!DOCTYPE html> <html> <head> <title>Random-Search-for-Optimization</title> </head> <body> <h1>Random-Search-for-Optimization</h1> <p>Random search (RS) is a family of [numerical optimization](poe://www.poe.com/_api/key_phrase?phrase=numerical%20optimization&prompt=Tell%20me%20more%20about%20numerical%20optimization.) methods that do not require the gradient of the problem to be optimized. This repository contains the implementation in [Python](poe://www.poe.com/_api/key_phrase?phrase=Python&prompt=Tell%20me%20more%20about%20Python.) of various [optimization algorithms](poe://www.poe.com/_api/key_phrase?phrase=optimization%20algorithms&prompt=Tell%20me%20more%20about%20optimization%20algorithms.):</p>
xml
Copy
<ul>
	<li>[Linear Regression](poe://www.poe.com/_api/key_phrase?phrase=Linear%20Regression&prompt=Tell%20me%20more%20about%20Linear%20Regression.) with [Simulated Annealing](poe://www.poe.com/_api/key_phrase?phrase=Simulated%20Annealing&prompt=Tell%20me%20more%20about%20Simulated%20Annealing.)</li>
	<li>[Particle Swarm Optimization](poe://www.poe.com/_api/key_phrase?phrase=Particle%20Swarm%20Optimization&prompt=Tell%20me%20more%20about%20Particle%20Swarm%20Optimization.) for Linear Regression</li>
	<li>[TSP](poe://www.poe.com/_api/key_phrase?phrase=TSP&prompt=Tell%20me%20more%20about%20TSP.) using [Genetic Algorithm](poe://www.poe.com/_api/key_phrase?phrase=Genetic%20Algorithm&prompt=Tell%20me%20more%20about%20Genetic%20Algorithm.)</li>
	<li>TSP using [Nearest Neighbor Algorithm](poe://www.poe.com/_api/key_phrase?phrase=Nearest%20Neighbor%20Algorithm&prompt=Tell%20me%20more%20about%20Nearest%20Neighbor%20Algorithm.)</li>
	<li>TSP using [Simulated Annealing Algorithm](poe://www.poe.com/_api/key_phrase?phrase=Simulated%20Annealing%20Algorithm&prompt=Tell%20me%20more%20about%20Simulated%20Annealing%20Algorithm.)</li>
</ul>

<h2>Pre-Installed Packages</h2>
<p>The following packages need to be pre-installed before running the code:</p>

<ul>
	<li>gifsicle: To create [animated GIFs](poe://www.poe.com/_api/key_phrase?phrase=animated%20GIFs&prompt=Tell%20me%20more%20about%20animated%20GIFs.) of the optimization process.</li>
	<pre><code>[sudo apt install](poe://www.poe.com/_api/key_phrase?phrase=sudo%20apt%20install&prompt=Tell%20me%20more%20about%20sudo%20apt%20install.) gifsicle</code></pre>
	<li>imagemagick: To create an image of the optimization process.</li>
	<pre><code>[sudo apt](poe://www.poe.com/_api/key_phrase?phrase=sudo%20apt&prompt=Tell%20me%20more%20about%20sudo%20apt.) install imagemagick</code></pre>
</ul>

<h2>How to Use</h2>
<ol>
	<li>Clone the repository</li>
	<pre><code>git clone https://github.com/&lt;username&gt;/Random-Search-for-Optimization.git</code></pre>
	<li>Navigate to the directory</li>
	<pre><code>cd Random-Search-for-Optimization</code></pre>
	<li>Install the required packages</li>
	<pre><code>pip install -r requirements.txt</code></pre>
	<li>Run the Python scripts</li>
	<pre><code>python linear_regression_simulated_annealing.py</code></pre>
	<pre><code>python linear_regression_particle_swarm_optimization.py</code></pre>
	<pre><code>python tsp_genetic_algorithm.py</code></pre>
	<pre><code>python tsp_nearest_neighbor_algorithm.py</code></pre>
	<pre><code>python tsp_simulated_annealing_algorithm.py</code></pre>
</ol>

<h2>Examples</h2>
<p>Here's an example of running the TSP using [Simulated](poe://www.poe.com/_api/key_phrase?phrase=Simulated&prompt=Tell%20me%20more%20about%20Simulated.) Annealing Algorithm:</p>

<ol>
	<li>Navigate to the directory</li>
	<pre><code>cd Random-Search-for-Optimization</code></pre>
	<li>Run the Python script</li>
	<pre><code>python tsp_simulated_annealing_algorithm.py</code></pre>
</ol>

<p>The program will output an animated GIF file called <code>tsp_simulated_annealing.gif</code> and an image file called <code>tsp_simulated_annealing.png</code> showing the optimization process.</p>
<img src="https://user-images.githubusercontent.com/1234567/12345678-tsp_simulated_annealing.gif" alt="tsp_simulated_annealing">
</body> </html>
