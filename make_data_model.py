import spacy


nlp = spacy.load('en_core_web_sm')
nlp.to_disk('my_model')

# Makes model exist on our Disk for quick access 