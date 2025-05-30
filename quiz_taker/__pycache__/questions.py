# Question loader

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options  # Dictionary like {'a': 'Option A', ...}
        self.correct_answer = correct_answer.lower()

    def is_valid(self):
        return (
            self.text and
            all(option for option in self.options.values()) and
            self.correct_answer in ['a', 'b', 'c', 'd']
        )

    def to_text(self):
        lines = [
            f"Question: {self.text}",
            f"a) {self.options['a']}",
            f"b) {self.options['b']}",
            f"c) {self.options['c']}",
            f"d) {self.options['d']}",
            f"Correct Answer: {self.correct_answer}",
            "-" * 40
        ]
        return "\n".join(lines) + "\n"
