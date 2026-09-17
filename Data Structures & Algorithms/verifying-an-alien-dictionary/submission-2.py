class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for i,ch in enumerate(order):
            mapping[ch] = i
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        translated = []
        for word in words:
            new_word = []
            for ch in word:
                index = mapping[ch]
                new_word.append(alphabet[index])
            translated.append(new_word) 
        
        print(f"translated {translated}, words {words}")
        return sorted(translated) == translated
           