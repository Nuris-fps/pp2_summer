class Awper:
    def snipe(self):
        return "making difference with awp!"

class Rifler:
    def rifle(self):
        return "winning duels"

# Hybrid inherits from both Awper and Rifler
class Hybrid(Awper, Rifler):
    pass

Zywoo = Hybrid()
print(Zywoo.snipe())  # Output: making difference with awp!
print(Zywoo.rifle())  # Output: winning duels!
