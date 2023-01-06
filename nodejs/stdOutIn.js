const questions = [
  'O que aprendi hoje?',
  'O que me deixou aborrecido? E o que eu pderia fazre para melhorar?',
  'O que me deixou feliz hoje?',
  'Quantos pessoas ajudei hoje?',
];

const answers = [];

const ask = (index = 0) => {
  process.stdout.write(questions[index] + '\n');
};

ask();

process.stdin.on('data', data => {
  answers.push(data.toString().trim());
  if (answers.length < questions.length) {
    ask(answers.length);
  } else {
    process.exit();
  }
});

process.on('exit', () => {
  process.stdout.write('\n');
  for (let i = 0; i < questions.length; i++) {
    process.stdout.write(`${i + 1} - ${questions[i]}\n${answers[i]}\n`);
  }
});
