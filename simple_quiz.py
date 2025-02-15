import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

def ask_question(index, question, options):
  print(f'Question {index}: {question}')
  for option in options:
    print(option)

  return input('Your answer: ').upper().strip()  

def run_quiz(quiz):
  random.shuffle(quiz)

  score = 0

  for index, item in enumerate(quiz, 1):
    answer = ask_question(index, item[QUESTION], item[OPTIONS])

    if answer == item[ANSWER]:
      cprint('Correct!', 'green')
      score += 1
    else:
      cprint(f'Wrong! The correct answer is {item[ANSWER]}', 'red')
    
    print()

  print(f'Quiz over! Your final score is {score} out of {len(quiz)}')


def main():  
  quiz = [
    {
      QUESTION: 'What is the capital of France?',
      OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
      ANSWER: 'C'
    },
    {
      QUESTION: 'Which planet is known as the red planet?',
      OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
      ANSWER: 'B'
    },
    {
      QUESTION: 'What is the largest ocean on Earth?',
      OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
      ANSWER: 'D'
    },
    {
      QUESTION: ' Which element has the chemical symbol "O"? ',
      OPTIONS: ['A. Gold','B. Oxygen','C. Osmium','D. Hydrogen'],
      ANSWER: 'B'
    },
    {
      QUESTION: 'What is the boiling point of water at sea level in Celsius? ',
      OPTIONS: ['A. 90°C', 'B. 100°C', 'C. 120°C', 'D. 80°C'],
      ANSWER: 'B'
    },
    {
      QUESTION: ' Who painted the Mona Lisa? ',
      OPTIONS: ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Claude Monet'],
      ANSWER: 'C'
    },
    {
      QUESTION: '  In which year did the Titanic sink? ',
      OPTIONS: ['A. 1905','B. 1912','C. 1920','D. 1915'],
      ANSWER: 'B'
    }
  ]  
  run_quiz(quiz)

if __name__ == '__main__':
  main()