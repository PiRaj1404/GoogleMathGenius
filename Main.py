import os
from dotenv import load_dotenv
from ImageTextDetector import ImageTextDetector
from TextTranslator import TextTranslator
from ProblemSolver import ProblemSolver

def main():
    load_dotenv()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    credential_path = os.path.join(current_dir, 'gcpKeys.json')
    api_key = os.getenv('GOOGLE_API_KEY')

    problems_folder = os.path.join(current_dir, 'Problems')
    
    # Instantiate the detector, translator, and solver
    text_detector = ImageTextDetector(credential_path)
    translator = TextTranslator()
    solver = ProblemSolver(api_key)

    # Iterate over all files in the Problems folder
    for filename in os.listdir(problems_folder):
        image_path = os.path.join(problems_folder, filename)
        try:
            # Detect text from image
            detected_text = text_detector.detect_text(image_path)
            if not detected_text:
                print(f"No text detected in {filename}.")
                continue

            # Translate detected text
            question = translator.translate_text(detected_text)
            print(f"Question from {filename}:\n{question}")

            # Solve the problem
            solution = solver.solve_problem(question)
            print(f"Solution for {filename}:\n{solution}\n")
        except Exception as e:
            print(f"An error occurred with {filename}: {e}")

if __name__ == '__main__':
    main()
