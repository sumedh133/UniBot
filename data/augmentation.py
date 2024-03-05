import nlpaug.augmenter.word as naw
import nlpaug.augmenter.char as nac
import json

with open('data/intents.json', 'r') as file:
    intents_data = json.load(file)

def augment_intent(intent):
    # Char Augmentation: OCR error
    ocr_aug = nac.OcrAug()
    
    # Char Augmentation: Keyboard typos
    keyboard_aug = nac.KeyboardAug()
    
    # Word Augmentation: Spelling augmenter
    spell_aug = naw.SpellingAug()
    
    # Word Augmentation: Synonym replacement
    synonym_aug = naw.SynonymAug()
    
    # Word Augmentation: Split augmentation
    split_aug = naw.SplitAug()

    # Word Augmentation: Random augmentation
    random_aug1 = naw.RandomWordAug(action="swap")
    random_aug2 = naw.RandomWordAug(action="delete")

    augmented_patterns = set()  # Use a set to store unique augmented patterns

    for original_pattern in intent['patterns']:
        augmented_patterns.update(synonym_aug.augment(original_pattern, n=3))
    
    return list(augmented_patterns)

for intent in intents_data['intents']:
    augmented_patterns = augment_intent(intent)
    intent['patterns'].extend(augmented_patterns)

augmented_intents_filename = 'data/augmented_intents.json'
with open(augmented_intents_filename, 'w') as augmented_file:
    json.dump(intents_data, augmented_file, indent=2)

print(f"Augs have been saved to {augmented_intents_filename}")
