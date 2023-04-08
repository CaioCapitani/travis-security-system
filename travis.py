know_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print ("Oi! Meu nome é Travis")
    name = input("Qual o seu nome?: ").strip().capitalize()

    if name in know_users:
        print("Olá {}!".format(name))
        remove = input("Você gostaria de ser removido do sistema (s/n)?: ").srtip().lower()

        if remove == "s":
            know_users.remove(name)
        elif remove == "n":
            print("Sem problemas")
         
    else:
        print("Hmmm acho que não te conheço ainda {}".format(name))
        add_me = input ("Você gostaria ser incluído no sistema (s/n)?: ").strip().lower()

        if add_me == "s":
            know_users.append(name)
        elif add_me == "n":
            print("Sem problemas")