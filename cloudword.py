import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# This is the uploader widget

def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)


_upload()


def calculate_frequencies(file_contents):
    # List of uninteresting words to process your text

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are",
                           "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at",
                           "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few",
                           "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    file = file_contents.split() # Create a word list seperated by space
    word_frequency = {}
    
    '''Create a dictionary with each word count by ignoring words in uninteresting words'''
    def create_word_dict(word):
        if word not in uninteresting_words:
            if word in word_dict:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    
    '''check for word only with alpha characters'''
    for word in file:
        if word.isalpha():
            create_word_dict(word.lower())
        else:
            aplha_word = ''
            for char in word:
                if char.isalpha():
                    aplha_word += char
            create_word_dict(aplha_word.lower())

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequency)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()



