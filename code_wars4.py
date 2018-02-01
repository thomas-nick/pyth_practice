
def decrypt(encrypted_text, n):
    for k in range(n):
        t = encrypted_text + encrypted_text
        string = [None] * len(encrypted_text)
        for i in range(0, int(len(encrypted_text) / 2), 1):
            string[i * 2 + 1] = str(t[i])
        j = 0
        for i in range(int(len(encrypted_text) / 2), int(len(encrypted_text)), 1):
            string[j] = str(t[i])
            j += 2
        encrypted_text = ''.join(string)
    return encrypted_text


def encrypt(text, n):
    for i in range(n):
        if(len(text) % 2 == 0):
            t = text + " " + text
        else:
            t = text + text
        string = ''
        for i in range(len(t)):
            if(i % 2 != 0):
                string += str(t[i])
        text = string

    return text
