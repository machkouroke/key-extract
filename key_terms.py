import nltk
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import download
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def download_nltk_module():
    download('punkt')
    download('wordnet')
    download('omw-1.4')
    download('stopwords')


def preprocessing(story):
    legalize = WordNetLemmatizer()
    story = [legalize.lemmatize(x) for x in sorted(word_tokenize(story.lower()), reverse=True)]
    story = [x for x in story if x not in list(punctuation) + stopwords.words('english')
             and nltk.pos_tag([x])[0][1] == 'NN'
             ]
    return ' '.join(story)


def vectorization(story):
    vectorized = TfidfVectorizer()
    count = vectorized.fit_transform(story.values())
    vocabulary = vectorized.get_feature_names_out()
    densely = count.todense().tolist()
    df = pd.DataFrame(densely, columns=vocabulary)
    for x, i in zip(story, range(len(df))):
        story[x] = sorted(sorted(vocabulary, reverse=True), key=lambda y: df.loc[i, y], reverse=True)

    return story


def main():
    news = etree.parse('news.xml').getroot()
    output = {x[0].text: preprocessing(x[1].text) for x in news[0]}
    output = vectorization(output)
    for x, z in output.items():
        print(x + ':')
        print(*z[:5])


if __name__ == "__main__":
    download_nltk_module()
    print('***The most important terms for each paragraph is:***')
    main()
