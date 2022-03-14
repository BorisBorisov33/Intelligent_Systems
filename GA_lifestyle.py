import random
import datetime
import joblib
import numpy as np


class GA:

    def __init__(self, n_generation, pop_size, mutation_rate, starting_score):
        self.generation = n_generation
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.model = joblib.load('finalized_model.joblib')
        self.starting_score = starting_score

    def initial_pop(self):
        date = datetime.datetime(1900, 1, 2)
        initial_pop = []
        target_score = 60
        if self.starting_score < 20:
            target_score = 77
        while len(initial_pop) < (self.pop_size):
            temp_pop = []
            time_in_bed = random.randint(7200, 43200)
            time_go_bed = 76500
            time_wake_up = date + datetime.timedelta(seconds=time_in_bed)
            time_wake_up = (86400 - (date - time_wake_up).total_seconds())
            number_of_steps = random.randint(2000, 10000)
            external_fact = random.choice([0, 1])
            temp_pop.append([time_in_bed, time_go_bed, time_wake_up, number_of_steps, external_fact])
            if target_score < self.model.predict(temp_pop):
                initial_pop.append([time_in_bed, time_go_bed, time_wake_up, number_of_steps, external_fact])

        return initial_pop

    def fitness(self, pop):

        fitness = dict()
        for i in pop:
            X = np.array(i)
            X = X.reshape(1, -1)
            fitness_val = self.model.predict(X)[0]
            i = tuple(i)
            fitness[i] = fitness_val

        return fitness

    def selection(self, fitness):
        # sorted_pop= dict(sorted(fitness.items(),key=lambda x :x[1],reverse=True))
        temp_dict = fitness.copy()
        selected_pop = []
        selected_dict = dict()
        population_fitness = sum(fitness.values())
        for i in fitness:
            i_prob = fitness[i] / population_fitness
            fitness[i] = i_prob
        selected_pop = (np.random.choice(list(temp_dict.values()), p=list(fitness.values()), size=50))
        dict_keys = list(temp_dict.keys())
        dict_values = list(temp_dict.values())
        for i in selected_pop:
            val_index = dict_values.index(i)
            myKey = dict_keys[val_index]
            selected_dict[myKey] = i

        return selected_dict

    def crossover(self, selected):
        dict_keys = list(selected.keys())
        child = []
        for i in range(50):
            parent_1, parent_2 = random.choices(dict_keys, k=2)

            child_val = []
            for j in range(len(parent_1) - 1):
                child_val.append(int(parent_1[j] + parent_2[j]) / 2)
            child_val.append(random.choice([0, 1]))
            child.append(child_val)
            child_val = []

        child_fit = self.fitness(child)
        new_pop = selected | child_fit

        return new_pop

    def mutation(self, new_pop):
        dict_keys = list(new_pop.keys())
        dict_keys = np.array(dict_keys)
        for i in range(len(dict_keys)):
            r = random.random()
            if (2 * r < self.mutation_rate):
                n = random.randint(0, 4)
                if n < 4:
                    dict_keys[i][n] = dict_keys[i][n] + dict_keys[i][n] * 0.1
                else:
                    if dict_keys[i][n] == 1:
                        dict_keys[i][n] = 0
                    else:
                        dict_keys[i][n] = 1

        return dict_keys

    def runGA(self):
        initial_pop = self.initial_pop()
        gen = 0
        while gen < self.generation:
            fitness = self.fitness(initial_pop)
            selected = self.selection(fitness)
            crossover = self.crossover(selected)
            mutation = self.mutation(crossover)
            initial_pop = mutation
            gen = gen + 1

        final_pop = self.fitness(initial_pop)
        sorted_pop = dict(sorted(final_pop.items(), key=lambda x: x[1], reverse=True))
        return sorted_pop
