def answer(population, x, y, strength):

	if strength >= population[y][x] and population[y][x] != -1:
		population[y][x] = -1

		if x < len(population[0]) - 1:
			population = answer(population, x + 1, y, strength)
		if x > 0:
			population = answer(population, x - 1, y, strength)
		if y < len(population) - 1:
			population = answer(population, x, y + 1, strength)
		if y > 0:
			population = answer(population, x, y - 1, strength)

	return population