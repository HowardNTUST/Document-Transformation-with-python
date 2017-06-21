
#first install pocketsphinx
#https://stackoverflow.com/questions/36523705/python-pocketsphinx-requesterror-missing-pocketsphinx-module-ensure-that-pocke

#then install
'''apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig'''
'pip install textract'

import textract
import glob

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


# make a list


def document_to_text(filename):
    
    if filename[-4:] == ".doc":
        #return textract.process(filename).decode('utf-8').replace('\n\n','||').replace('\n','').replace('||','\n\n')
        return textract.process(filename).decode('utf-8').replace('\n','').replace('\u3000','').replace('\t','\n')
    
    elif filename[-5:] == ".docx":
        return textract.process(filename).decode('utf-8').replace('\n','').replace('\u3000','').replace('\t','\n')
    
    elif filename[-4:] == ".odt":
        return textract.process(filename).decode('utf-8').replace('\n','').replace('\u3000','').replace('\t','\n')
    
    elif filename[-4:] == ".pdf":
        return textract.process(filename).decode('utf-8').replace('\x0c','').replace('\n','').replace('\u3000','').replace('\t','\n')


len_doc=[]
for doc in glob.iglob("*"):
    len_doc.append(doc)

l = len(len_doc)
i=0
txt=[]

for doc in glob.iglob("*"):
    txt.append(document_to_text(doc))
    i += 1
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    
len(txt)

gg='/n/n'.join(txt)
len(gg)
