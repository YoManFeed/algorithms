from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from simlex_method import SimplexMethod

import numpy as np


class SimplexApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.create_matrix_input()
        self.create_z_function_input()

        submit_button = Button(text="Submit", on_press=self.submit_inputs)
        self.layout.add_widget(submit_button)

        return self.layout

    def create_matrix_input(self):
        matrix_label = Label(text="Enter Matrix (space-separated values, rows separated by \\n):")
        self.matrix_input = TextInput(multiline=True)
        self.layout.add_widget(matrix_label)
        self.layout.add_widget(self.matrix_input)

    def create_z_function_input(self):
        z_function_label = Label(text="Enter Z-function (space-separated values):")
        self.z_function_input = TextInput()
        self.layout.add_widget(z_function_label)
        self.layout.add_widget(self.z_function_input)

    def submit_inputs(self, instance):
        matrix_text = self.matrix_input.text
        z_function_text = self.z_function_input.text

        matrix = [list(map(float, row.split())) for row in matrix_text.split('\n')]
        matrix = np.array(matrix)
        z_function = list(map(float, z_function_text.split()))
        z_function = np.array(z_function)

        self.run_simplex_method(matrix, z_function)

    def run_simplex_method(self, matrix, Zfunc):

        np.set_printoptions(precision=2, suppress=True)
        constants = matrix[:, -1]
        matrix_coefs = matrix[:, :-1]
        simplex_solver = SimplexMethod(Zfunc, matrix_coefs, constants)

        simplex_solver.solve()
        simplex_solver.print_solution()
        print('Solved')


if __name__ == '__main__':
    SimplexApp().run()
