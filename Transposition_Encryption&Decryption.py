encryptionMatrix = []
decryptionMatrix = []

def function(str, mat, lp):

for i in range(len(str)):
if i % lp == 0:
sub = str[i:i + lp]

lst = []
for j in sub:
lst.append(j)
mat.append(lst)
print(&#39; &#39;.join(lst))

def cypherText(matrix):
text = []
for i in range(len(matrix)):
for j in range(len(matrix[i])):
text.append(matrix[j][i])

return text

if __name__ == &#39;__main__&#39;:
text = str(input(&quot;Enter the text : &quot;))
newText = text.replace(&quot; &quot;, &quot;&quot;)
print(&quot;\n ************ Encryption *************\n newText&quot;)
num = int(len(newText))
function(newText, encryptionMatrix, 3)
eT = cypherText(encryptionMatrix)
print(eT)
encryptedText = &quot;&quot;

encryptedText = encryptedText.join(eT)
print(encryptedText)

print(&quot;\n\n************ Decryption *************\n&quot;)

function(encryptedText, decryptionMatrix, 3)
dT = cypherText(decryptionMatrix)
print(dT)

decryptedText = &quot;&quot;
decryptedText = decryptedText.join(dT)
print(decryptedText)
