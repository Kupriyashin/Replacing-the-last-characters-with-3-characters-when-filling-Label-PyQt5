import random

from loguru import logger


class Sentence:
    @logger.catch()
    def random_moew_sentence(self) -> str:
        try:

            _words = ['мяу'] * random.randint(3, 10)
            logger.info(_words)

            _words[-1] = _words[-1] + str(random.choice(['.', '!', '?']))

            for _ in range(0, len(_words) - 1):

                if random.random() < 0.01:
                    _words[_] = _words[_] + str(random.choice(['😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']))

                if random.random() < 0.1:
                    _words[_] = _words[_] + str(random.choice([',', ':', ' -', '']))

            _sentence = ' '.join(_words)
            _sentence = _sentence.capitalize()
            logger.info(f'Сформированное сообщение random_moew_sentence: {_sentence}')

            return str(_sentence)

        except Exception as process_file_err:
            logger.error(f'Произошла ошибка в преобразовании предложения в meow: {process_file_err}')

    @logger.catch()
    def sentence(self) -> str:
        try:
            _outsectence = []
            if random.random() > 0.5:
                _outsectence.append(self.random_moew_sentence())
            elif random.random() < 0.01:
                for a in range(6):
                    _outsectence.append(self.random_moew_sentence() + ' ')
            elif random.random() < 0.1:
                for b in range(5):
                    _outsectence.append(self.random_moew_sentence() + ' ')
            elif random.random() < 0.2:
                for c in range(4):
                    _outsectence.append(self.random_moew_sentence() + ' ')
            elif random.random() < 0.3:
                for d in range(3):
                    _outsectence.append(self.random_moew_sentence() + ' ')
            elif random.random() < 0.4:
                for f in range(2):
                    _outsectence.append(self.random_moew_sentence() + ' ')
            elif random.random() < 0.5:
                for g in range(1):
                    _outsectence.append(self.random_moew_sentence() + ' ')

            _output = ''.join(_outsectence)
            logger.info(f'Сформированное сообщение sentence: {_output}')

            return _output

        except Exception as err_sentence:
            logger.error(err_sentence)
            return 'Мяу мяу мяу мяу, мяу мяу мяу мяу мяу?'
