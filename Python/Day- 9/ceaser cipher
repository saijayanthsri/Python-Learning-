direction= input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Type shift number:\n"))
def encode(text,shift):
    alphabets= [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
    message = list(text)
    n = len(message)
    new_list = []

    for i in range(n):
        if message[i] in alphabets:
            position = alphabets.index(message[i])
            new_position = position +shift
            if new_position >=26:
                new_position = (position + shift) % 26
            new_list.append(alphabets[new_position])
        else:
            new_list.append(message[i])
            
    new_word = "".join(new_list)
    return new_word
    


def decode(text,shift):
    alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
    message = list(text)
    n =len(message)
    new_list = []

    for i in range(n):
        if message[i] in alphabets:
            position = alphabets.index(message[i])
            new_position =(position - shift) % 26
            new_list.append(alphabets[new_position])
        else:
            new_list.append(message[i])

    new_word = "".join(new_list)
    return new_word

if direction == "encode":
    print(encode(text,shift))
elif direction == "decode":
    print(decode(text,shift))
