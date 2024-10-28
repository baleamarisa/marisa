sir=(" Horoscop 21 octombrie 2024! ")
print(sir)
nr_caractere_sir=len(sir)
jumatate=(nr_caractere_sir//2)
jumatate1=sir[:jumatate]
jumatate2=sir[jumatate:]
jumatate1=jumatate1.upper().strip()
jumatate2=jumatate2.capitalize()
jumatate2=jumatate2[::-1]
jumatate2=jumatate2.replace('!','')
print(jumatate1+jumatate2)


