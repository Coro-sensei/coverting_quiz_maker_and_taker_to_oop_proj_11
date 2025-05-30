# Data Manager
class QuizManager:
    def __init__(self, file_path="quiz_maker_data.txt"):
        self.file_path = file_path

    def save_question(self, question_text, options_dict, correct_answer_letter):
        try:
            with open(self.file_path, "a") as file:
                file.write(f"Question: {question_text}\n")
                file.write(f"a) {options_dict['a']}\n")
                file.write(f"b) {options_dict['b']}\n")
                file.write(f"c) {options_dict['c']}\n")
                file.write(f"d) {options_dict['d']}\n")
                file.write(f"Correct Answer: {correct_answer_letter}\n")
                file.write("-" * 40 + "\n")
            return True
        except Exception as error:
            print(f"Failed to save: {error}")
            return False
