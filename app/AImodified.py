import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, pipeline
from nltk.tokenize import sent_tokenize

class CVTextProcessor:
    def __init__(self):
        self.t5_model = T5ForConditionalGeneration.from_pretrained('j5ng/et5-typos-corrector')
        self.t5_tokenizer = T5Tokenizer.from_pretrained('j5ng/et5-typos-corrector')
        self.typos_corrector = pipeline(
            "text2text-generation",
            model=self.t5_model,
            tokenizer=self.t5_tokenizer,
            device=0 if torch.cuda.is_available() else -1,
            framework="pt",
        )

    def typos_correction(self, text):
        corrected_text = self.typos_corrector("맞춤법 수정: " + text,
                                              max_length=128,
                                              num_beams=5,
                                              early_stopping=True)[0]['generated_text']
        return corrected_text

    def process_cv_text(self, text):
        sentences = sent_tokenize(text)
        corrected_sentences = []

        for sentence in sentences:
            corrected_sentence = self.typos_correction(sentence)
            corrected_sentences.append(corrected_sentence)

        corrected_text = ' '.join(corrected_sentences)
        return corrected_text, len(text)