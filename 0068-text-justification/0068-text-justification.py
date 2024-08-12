class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_text(sentences, max_width):
            justified_sentences = []

            for i, sentence in enumerate(sentences):
                words = sentence.split()
                num_words = len(words)
                total_chars = sum(len(word) for word in words)
                total_spaces = max_width - total_chars

                # Last line or single-word line should be left-justified
                if num_words == 1 or i == len(sentences) - 1:
                    justified_sentence = ' '.join(words).ljust(max_width)
                else:
                    space_between_words = total_spaces // (num_words - 1)
                    extra_spaces = total_spaces % (num_words - 1)

                    for j in range(extra_spaces):
                        words[j] += ' '

                    justified_sentence = (' ' * space_between_words).join(words)

                justified_sentences.append(justified_sentence)

            return justified_sentences

    
        st=""
        lst=[]
        for i in range(len(words)):
            
                if len(st+words[i])<=maxWidth:
                    st=st+words[i]+" "
                    # while len(st)<maxWidth:
                    #     j=0
                    #     while(j<len(st)):
                    #         if st[i]==" ":

                else :
                    lst.append(st)
                    st=words[i]+" "
                    
        lst.append(st)
        return justify_text(lst,maxWidth)
        # print(lst)
            
