#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for evenword in st.split():
    if len(evenword)%2==0:
        print(evenword+ ' has an even length')
        