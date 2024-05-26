usuarios = {}
print(usuarios)

usuarios = {
    "chaves": ["Chaves do 8", "24/12/2017", "Recep_01"],
    "quico": ["Chico das flores", "20/12/2017", "Raiox_03"]
}
print(usuarios)

usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]
print(usuarios)

print("####---------####")
print(usuarios.get("quico"))