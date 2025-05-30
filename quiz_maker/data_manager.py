# Data Manager

class QuizDataManager:
    def __init__(self, filename = "quiz_maker_data.txt"):
        self.filename = filename

    def save_question(self, question_text, option_dict, correct_answer_letter):
        try:
            with open(self.filename, "a") as file:
                file.write(f"Question: {question_text}\n")
                file.write(f"a) {options_dict['a']}\n")
                file.write(f"b) {options_dict['b']}\n")
                file.write(f"c) {options_dict['c']}\n")
                file.write(f"d) {options_dict['d']}\n")
                file.write(f"Correct Answer: {correct_answer_letter}\n")
                file.write("-" * 40 + "\n")
        except Exception as error:
            print(f"Error on saving the data.")