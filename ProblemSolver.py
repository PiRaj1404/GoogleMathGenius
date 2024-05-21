import google.generativeai as genai

class ProblemSolver:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)

    def solve_problem(self, prompt):
        gen_response = genai.generate_text(prompt=prompt)
        return gen_response.result
