import numpy as np


class SimplexMethod:
    def __init__(self, Zfunc, matrix_coefs, constants):
        """
        Решение для особого ввода данных, приведенных ограничений и на максимизацию
        # TODO обощить ввод данных (использовать re и регулярные выражения)
        # TODO реализовать решение минимизации / привести задачу к максимизации
        # TODO реализовать приведение к ограничениям
        # TODO ещё сильнее обобщить ввод данных, которые содержат пропуски в x_i
        
        :param Zfunc: Коэффициенты целевой функции (вектор)
        :param matrix_coefs: Матрица ограничений (матрица)
        :param constants: Вектор правой части ограничений (вектор)
        """
        self.Zfunc = -1 * np.array(Zfunc)
        self.matrix_coefs = np.array(matrix_coefs)
        self.constants = np.array(constants)
        self.num_variables = len(Zfunc)
        self.num_constants = len(constants)
        self.matrix = np.hstack((self.constants.reshape(-1, 1), self.matrix_coefs))

        self.initial_output()
        self.matrix = self.add_fic_basis()
        # print(self.matrix)
        # print(self.Zfunc)


    def initial_output(self):
        print("=" * 10 * self.num_variables)
        print(f'Целевая:', *self.Zfunc)
        print('Марица:')
        print(self.matrix)
        print("=" * 10 * self.num_variables)


    def add_fic_basis(self):
        E = np.eye(self.num_variables, self.num_variables)
        E = np.hstack((self.matrix, E))
        self.Zfunc = np.pad(self.Zfunc, (0, E.shape[1] - len(self.Zfunc)), mode='constant')
        self.Zfunc = np.roll(self.Zfunc, 1)
        return np.vstack((E, self.Zfunc))


    def solve(self):
        """
        Метод для решения задачи симплекс-методом
        """
        print(self.matrix)
        print('='*44)
        while min(self.Zfunc) < 0:
            index_bottom = np.where(self.Zfunc == min(self.Zfunc))[0][0]
            column = self.matrix[:-1, index_bottom]
            div = (self.matrix[:-1, 0] / (column + 10**-8))
            min_elem = np.min(div[div > 0])
            index_left = np.where(div == min_elem)[0][0]

            elem = self.matrix[index_left, index_bottom]
            print(f'Разрешающий элемент: {elem:.2f}, имеющий корды {index_left, index_bottom}')

            actual_line = self.matrix[index_left, :]
            for i in range(self.num_constants + 1):
                if i != index_left:
                    self.matrix[i, :] = (-1 * self.matrix[i, index_bottom]) * actual_line / elem + self.matrix[i, :]
            self.Zfunc = (-1 * self.Zfunc[index_bottom] * actual_line) / elem + self.Zfunc
            self.matrix[index_left, :] = self.matrix[index_left, :] / elem

            self.print_solution()


    def print_solution(self):
        """
        Метод для вывода решения
        """
        print(self.matrix)
        print('='*44)


with open('input.txt', 'r') as file:
    Zfunc = np.fromstring(file.readline(), sep=' ')
    matrix = np.loadtxt(file)

np.set_printoptions(precision=2, suppress=True)

constants = matrix[:, -1]
matrix_coefs = matrix[:, :-1]

simplex_solver = SimplexMethod(Zfunc, matrix_coefs, constants)
simplex_solver.solve()
simplex_solver.print_solution()
print('Solved')

# with open('input.txt', 'r') as file:
#     Zfunc = np.fromstring(file.readline(), sep=' ')
#     matrix_coefs = np.loadtxt(file)
#

# print("Objective Coefficients:", Zfunc)
# print("Constraint Matrix:\n", matrix_coefs)


