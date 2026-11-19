with open("input.txt","r",encoding="utf-8") as f:
    text = f.read()

class tokenizer:
    def __init__(self,text):
        self.voacb = sorted(set(text))
        self.voacb_size = len(self.voacb)

        self.ch_to_id = {}
        for id,ch in enumerate(self.voacb):
            self.ch_to_id[ch] = id
        self.id_to_ch = {}
        for id,ch in enumerate(self.voacb):
            self.id_to_ch[id] = ch

    def encoding(self,text):
        ides = []
        for ch in text:
            if ch in self.ch_to_id:
                ides.append(self.ch_to_id[ch])
        return ides
    def decoding(self,ids):
        chracter = []
        for i in ids:
            chracter.append(self.id_to_ch[i])
        return "".join(chracter)


words = tokenizer(text)
ides = words.encoding("hello my name is arman")
chracter = words.decoding(ides)
print(ides)
print(chracter)
         