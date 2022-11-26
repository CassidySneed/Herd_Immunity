# Final Project: Herd Immunity Simulation

_Imagine you have been hired at a new startup focused on health and medicine --- and the World Health Organization needs your skills as programmatic pandemic simulation specialist!_

**Your job is to create a simulation of herd immunity by modeling how a virus moves through a population where some (but not all) of a population is vaccinated against a virus.**

## Table of Contents

- [**Goals**](#%67%6F%61%6C%73)
  - [Rules](#%72%75%6C%65%73)
  - [Answer These Questions](#%61%6E%73%77%65%72%2D%74%68%65%73%65%2D%71%75%65%73%74%69%6F%6E%73)
- [**Getting Started**](#%67%65%74%74%69%6E%67%2D%73%74%61%72%74%65%64)
  - [Repository Setup](#%72%65%70%6F%73%69%74%6F%72%79%2D%73%65%74%75%70)
  - [Running the Program](#%72%75%6E%6E%69%6E%67%2D%74%68%65%2D%70%72%6F%67%72%61%6D)
  - [Basic Structure](#%62%61%73%69%63%2D%73%74%72%75%63%74%75%72%65)
- [**Tips for Success**](#%74%69%70%73%2D%66%6F%72%2D%73%75%63%63%65%73%73)
- [**Project Completion**](#%70%72%6F%6A%65%63%74%2D%63%6F%6D%70%6C%65%74%69%6F%6E)
- [**Stretch Challenges**](#%73%74%72%65%74%63%68%2D%63%68%61%6C%6C%65%6E%67%65%73)
- [**FAQs**](#%66%61%71%73)

## Goals

- Finish the code in these files to create a working simulation that logs it's results.
- Design your program to follow the [rules](#rules) of the simulation.
- Get your data for virus name, mortality rate, and reproductive rate from [this Guardian article](https://www.theguardian.com/news/datablog/ng-interactive/2014/oct/15/visualised-how-ebola-compares-to-other-infectious-diseases).
- During every time step of the simulation, **every sick person** should randomly interact with **100 other people** in the population. The chance of a sick person infecting a person that they interact with is the virus's reproductive rate. Example: if a virus has a reproductive rate of 15, then, on average, a sick person should infect 15 of the 100 people they interact with during that time step.

### Rules

1. A sick person only has a chance at infecting uninfected, unvaccinated people they encounter.
2. An infected person cannot infect a vaccinated person. This still counts as an interaction.
3. An infected person cannot infect someone that is already infected. This still counts as an interaction.
4. At the end of a time step, an infected person will either die of the infection or get better. The chance they will die is the percentage chance stored in `mortality_rate`.
5. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change `is_vaccinated` to `True` when this happens.
6. Dead people can no longer be infected, either. Any time an individual dies, we should also change their `infected` attribute to `False`.
7. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.
8. During the interactions, make note of any new individuals infected on this step. After the interactions are over, we will change the `infected` attribute of all newly infected individuals to `True`.
9. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.
10. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation. We will use this logfile to determine final statistics and answer questions about the simulation.

### Answer These Questions

Once you have successfully run a simulation, use your python skills to **analyze the simulation results**:

1. What were the **inputs** you gave the simulation? (Population size, percent vaccinated, virus name, mortality rate, reproductive rate)
2. What percentage of the population became **infected** at some point before the virus burned out?
3. What percentage of the population **died** from the virus?
4. Out of all interactions sick individuals had during the entire simulation, **how many times, in total, did a vaccination save someone from potentially becoming infected**?

_When you have answered these questions, please put your answers in a file called 'answers.txt' and commit this to your repo._

## Getting Started

‼️ **IMPORTANT:** Please follow these instructions _exactly_. 

If you skip a step or do them out of order, it may not work correctly or you may not earn credit towards your GitHub commit streak.

### Repository Setup

Set up your local clone of this project repo on your computer.

1. **Clone** (do not _fork_) this repo on GitHub onto your local computer.

  - First open your terminal and navigate into the folder where you keep your projects: `cd ~/MakeSchool/Projects` (or something similar for your folders)
  - Then run this command to _clone_ the course repo: `git clone https://github.com/Tech-at-DU/Herd-Immunity-Simulation.git`
  - Now navigate into the new folder Git just created: `cd Herd-Immunity-Simulation`

2. [**Create a new empty repo** on GitHub](https://github.com/new) also named `Herd-Immunity-Simulation` and **do not** initialize it with a ReadMe. (Creating a _new_ repo instead of a _fork_ allows you to earn credit towards your GitHub commit streak.)

3. **Set the `origin` remote's URL** on your local repo to point to your new repo on GitHub: `git remote set-url origin https://github.com/<your-username>/Herd-Immunity-Simulation.git`

4. **Push your local repo** to your _remote_ GitHub repo to link your `master` branch to your `origin` remote: `git push -u origin master`

5. **Commit your code** to your local repo frequently (each time you've made meaningful progress).

6. **Push your commits** to your remote GitHub repo when you want to publish and backup your code: `git push` (the `-u` in the previous command lets you omit `origin master` afterward).

**Let's get coding!** You'll find instructions for what you need to do marked within the files themselves. Anything that you explicitly need to code should be marked with a comment that starts with `#TODO`.

### Running the Program

The program is designed to be run from the command line. You can do this by running

```python
python3 simulation.py
```

followed by the command line arguments in the following order, separated by spaces: {population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected (default is 1)}

Let's look at an example:

- Population Size: 100,000
- Vaccination Percentage: 90%
- Virus Name: Ebola
- Mortality Rate: 70%
- Reproduction Rate: 25%
- People Initially Infected: 10

  Then I would type:

  ```python
  python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10
  ```

  in the terminal.

### Basic Structure

The program consists of 4 classes: `Person`, `Virus`, `Simulation`, and `Logger`.

- `Simulation`: Highest level of abstraction. The main class that runs the entire simulation.
- `Person`: Represents the people that make up the population that the virus is spreading through.
- `Virus`: Models the properties of the virus we wish to simulate.
- `Logger`: A helper class for logging all events that happen in the simulation.

When you run `simulation.py` with the corresponding command-line arguments necessary for a simulation, a simulation object is created. This simulation object then calls the `.run()` method. This method should continually check if the simulation needs to run another step using a helper method contained in the class, and then call `.time_step()` if the simulation has not ended yet. Within the `time_step()` method, you'll find all the logic necessary for actually simulating everything--that is, once you write it. As is, the file just contains a bunch of method stubs, as well as numerous comments for explaining what you need to do to get everything working.

## Tips for Success

First, take a look at each of the files. Get a feel for the methods and attributes in each. Feel overwhelmed? Don't panic. Instead, get out a piece of paper or a whiteboard and try to diagram what needs to happen and when using each of the objects and methods. Draw out the data flow.

### Not Sure? Talk to Classmates & Ask for Help

Ask your classmates and teachers for clarification/help/code reviews as needed, or drop in to tutoring hours. Share your questions and insights in the course Slack channel, or book some time to get help from Justin and Phyllis, the course teaching assistants. Collaboration is encouraged, but be sure that you typed in all the code yourself and the final project is your own!

### Found a Bug or Problem? 

Contact the course instructor or a teaching assistant!

If you think something doesn't make sense, double check with your classmates or the instructor. If you feel the need to modify the template code to make it work another way, that's totally fine! The template code is there to help you, but it isn't a requirement that you use all of it.

### Write Tests!

Starting by thinking about your test cases and aiming for good test coverage is a great way to vaccinate yourself against any pre-existing bugs in the template. 
 
 Not sure how to write tests? Look at the tests for the Super Hero project and utilize some strategies from those tests.

## Project Completion

**For the project to be considered done, you must**:

- Complete classes for `logger.py`, `simulation.py`, and `person.py`.
- Add at least 2 additional tests to the `virus.py` file.
- Add at least 3 additional tests to the `person.py` file.
- Add at least 1 log file generated from running your simulation.
- A `simulation_test.py` file should be created that allows for testing the simulation.
- A `logger_test.py` file should be created that allows for the testing of the logger class.
- Your answers to the [questions asked above](#answer-these-questions) listed in a file named `answers.txt`.
- Include a `.gitignore`
- Submit your completed repo to Gradescope

## Stretch Challenges

_You'll find some of the smaller, individual stretch challenges contained with the comments of the code on the logger class. Other stretch challenges include:_

1. Extending the functionality so that we can **test the spread of multiple viruses through a given population** at the same time. (Difficulty Level: Hard)
1. **Create a visualization of the simulation**. You can do this with Pygame. Create a number of sprites equal to the the number of people in your simulation. 

   - Show their status as color: `Red = infected`, `Blue = uninfected`, `Green = vaccinated`, `black = deceased`.
   - If you try this challenge you can change the interaction system to measure infections between sprites that collide.
   - You could also display this as a static image.

1. **Graph the visualization using `matplotlib`**. This is a library used to draw graphs and charts. You could use it to graph the results of the finished simulation.
1. Use an **alternative calculation for figuring infections**, like: mask compliance percentage, incubation time, etc. Consider the following when applying:

   - The project must be done on time.
   - Running the simulation must still work the same. If there are any new required parameters these must be fully documented.
   - The output must adhere to the project description.

## FAQs

### Q: Should we include the number of new infections at each step in the logged output?

**A**: Yes, include the number of new infections that happened each step in your log

### Q: Should the initially infected group test their mortality against the virus?
   
**A**: This is up to you; it is not specified in the requirements. If the initially infected group tests their mortality, they probably should do sp at the end of the first time step.

### Q: Should I simulate different stages of the virus? 

_(example: infected, incubation, self quarantine. Infectious time period)_
   
**A**: It's up to you. I recommend getting a basic simulation working first using simple rules before adding this since it will be more work. It's more important to get the work done on time than it is to add new features.

### Q: Should create a UI for a pygame simulation?

**A**: Pygame doesn't include any UI controls. This makes it a lot of work to add a user interface. If you choose to use Pygame (its a stretch challenge) you can include variables at the top of your main.py that the researchers can adjust for each run of the simulation.

### Q: What should the logger output look like?

**A**: Include a header, a step for for each step the simulation ran, and a footer showing the final state of the populatio. Here are some details:
   
#### Before Simulation Begins: Display Introduction

- Initial size of the population
- Initial number of infected people
- Name of the virus
- Stats for the virus
- Date the simulation was run

#### While Simulation Runs: Display  Every Iteration

- The number of new infections
- The number of deaths
- Statistics for the current state of the population:
 
    - Total number of living people
    - Total number of dead people
    - Total number of vaccinated people
             
 #### After Simulation Ends: Summary
 
 - Total living
 - Total dead
 - Number of vaccinations
 - Why the simulation ended
 - Total number of interactions that happened in the simulation
 - Number of interactions that resulted in vaccination
 - Number of interactions that resulted in death
# Herd_Immunity
# Herd_Immunity
