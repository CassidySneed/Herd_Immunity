import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("logger.txt")

        # TODO: Store the virus in an attribute
        self.virus = virus
        # TODO: Store pop_size in an attribute
        self.pop_size = pop_size
        # TODO: Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        # TODO: Store initial_infected in a variable
        self.initial_infected = initial_infected
        self.people_dead = 0 
        self.vaccinated_people = 0
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        # self.people = self.create_population()
        self.people_population = people_population = []
        self.newly_infected = []
        self.infected = []

        self.logger.write_metadata (self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)


    def _create_population(self):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # TODO: Return the list of people
        
        not_infected = self.pop_size - self.initial_infected

        for i in range(self.initial_infected):
            person = Person(i, False, self.virus)
            self.people_population.append(person)
            self.infected.append(person)
        for i in range(not_infected):
            person = Person(i, False, None)
            self.people_population.append(person)
        return self.people_population


    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        
        

        for person in self.people_population: 
            if person.is_vaccinated: 
                self.vaccinated_people += 1
            elif person.is_alive == False:
                self.people_dead += 1

        if self.vaccinated_people == self.pop_size or self.people_dead == self.pop_size or len(self.infected) == 0:
            return False
        else: 
            print(f"Dead: {self.people_dead}, Vaxxed: {self.vaccinated_people}")

            return True

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        self.time_step_counter = 0
        self.time_step_number = 0
        should_continue = True

        while should_continue:
            self.time_step_counter += 1 
            should_continue = self._simulation_should_continue()
            if should_continue: 
                self.time_step()
                self.time_step_number += 1
        

    def time_step(self):
        unifected = []

        for person in self.people_population: 
            if person.infection:   
                self.infected.append(person)
            else: 
                unifected.append(person)
        
        for person1 in self.infected: 
            # print(person1._id)
            for i in range(100):
                person2 = random.choice(unifected)

                if person1.is_alive and person2.is_alive:
                    self.interaction(person1, person2)

            # print(person1.did_survive_infection())
            if person1.did_survive_infection() == True:
                
                self.logger.log_infection_survival(self.time_step_counter, self.pop_size, self.people_dead)
                self.infected.remove(person1)


                print("did survive returned false, person did not die")
            else:
                self.logger.log_infection_survival(self.time_step_counter, self.pop_size, self.people_dead)
                self.infected.remove(person1)
                self.people_dead += 1
                print(f"People Dead: {self.people_dead}")
                print("someone died")
                # self.total_dead +=1  
        
        self._infect_newly_infected()

        self.logger.log_time_step(self.time_step_number)


    def interaction(self, infected_person, random_person):
        # assert infected_person.is_alive == True
        assert random_person.is_alive == True
    
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        # if ((not random_person.is_vaccinated) and (not random_person.infection)):
        #     if (infected_person.virus.repro_rate >= random.random()):
        #         self.newly_infected.append(random_person)
        #         self.logger.log_interactions(interaction, len(self.newly_infected))
        #     else: 
                # self.logger.log_interactions(interaction, len(self.newly_infected))
                
        interaction = 0
        # print(random_person.is_vaccinated)
        if random_person.is_alive:
            if random_person.is_vaccinated:
                print("person is vaccinated")
                interaction +=1
                self.logger.log_interactions(interaction, len(self.newly_infected))
            elif random_person.infection:
                print("person is infected, nothing happens")
                interaction+=1
                self.logger.log_interactions(self.time_step_number, interaction, len(self.newly_infected))
            elif random_person.is_vaccinated is False and random_person.infection is False:
                random_number = random.random()
                if random_number < self.virus.repro_rate:
                    if random_person not in self.newly_infected:
                        self.newly_infected.append(random_person) 
                self.logger.log_interactions(self.time_step_number, interaction, len(self.newly_infected))

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = True
        self.newly_infected = []



if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.90
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 10
    vacc_percentage = 0.1
    initial_infected = 3

    # Make a new instance of the imulation
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus,pop_size, vacc_percentage, initial_infected)
    sim._create_population()

    sim.run()
    # params = sys.argv[1:]
    # virus_name = str(params[0])
    # repro_rate = float(params[1])
    # mortality_rate = float(params[2])

    # pop_size = int(params[3])
    # vacc_percentage = float(params[4])

    # if len(params) == 6:
    #     initial_infected = int(params[5])
    # else:
    #     initial_infected = 1

    # virus = Virus(virus_name, repro_rate, mortality_rate)
    # sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    # sim.run()
