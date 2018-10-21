from tokenizer.extractor import Extractor
from tokenizer.splitter import Splitter
from processing.processor import Processor
from spelling.checker import SpellChecker
from spelling.repetition import RepetitionChecker
from parsing.stackparser import StackParser

WORDLISTS = [  
  'wordlists/manual.csv',
  'wordlists/verbosregulares.csv',]


class CompaFactory():
  def __init__(self):
    self.extractor = Extractor()
    self.splitter = Splitter()
    self.processor = Processor(lists=WORDLISTS)
    self.spellcheck = SpellChecker()
    self.repetition = RepetitionChecker()
    
  def execute(self, word):
    # Extrai os Tokens da Frase
    extracted = self.extractor.extract(word)
    # Faz a Checagem Gramatical e retorna os erros encontrados
    errors_spelling = self.spellcheck.from_tokenizer(extracted)
    # Atualiza os tokens extraidos com as correções
    extracted = self.spellcheck.autocorrect(extracted)
    # Atualiza os tokens removendo as duplicadas
    repetitions, extracted =  self.repetition.repetition(extracted)

    # Processa a lista de tokens e adiciona as tags de parte-de-fala
    tagged = self.processor.process(extracted)
    # PARSING


    stack = StackParser(tagged).stack
    print(tagged)
    print("REPETI")
    print(repetitions)


    return errors_spelling, repetitions, stack