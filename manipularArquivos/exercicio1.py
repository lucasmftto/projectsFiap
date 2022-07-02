import json


def createFile():
    with open("primeiro_arquivo.txt", "r") as arq:
        for line in arq.readlines():
            print(line)


def salvar(dicionario):
    with open("db.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write("\n" + chave + ":" + str(valor))


def invert(text):
    print(text[::-1])


def find(text, value):
    print(text[text.find(value) + 1:].find(value))
    print(text.split())


def openFileIris():
    irisItems = []
    with open("iris.data", "r") as irisFile:
        for line in irisFile.readlines():
            irisItems.append(line.split(","))

    return irisItems


def useJson():
    with open("bd.json", "r") as jsonFile:
        dic = json.load(jsonFile)
        for chave, dados in dic.items():
            print(chave + " " + str(dados))


def createJsonFile():
    dic = {
        "nome": "Lucas",
        "sobrenome": "Favaretto",
        "idade": "30"
    }
    with open("bd_create.json", "w") as jsonFile:
        json.dump(dic, jsonFile)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dic = {"teste2": ["Lucas2", "manja2", "python2"]}
    # salvar(dic)
    # invert("texto")
    # find("texto pronto", "o")
    # print(openFileIris())
    # useJson()
    createJsonFile()