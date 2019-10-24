from fag import Fag
from student import Student

per = Student("Per")
lisa = Student("Lisa")
mat1001 = Fag("mat1001")
inf = Fag("in1000")
ast1010 = Fag("ast1010")
# Per skal ta MAT1001 og IN1000
per.leggTilFag(mat1001)
mat1001.leggTilStudent(per)
per.leggTilFag(in1000)
in1000.leggTilStudent(per)

# Lisa skal ta IN1000 og AST1010
lisa.leggTilFag(in1000)
in1000.leggTilStudent(lisa)
lisa.leggTilFag(ast1010)
ast1010.leggTilStudent(lisa)

print(per.hentStudentNavn() + " tar " + str(per.hentAntallFag()) + " fag")
print(per.skrivFagPaaStudent())
print(Lisa.hentStudentNavn() + " tar " + str(lisa.hentAntallFag()) + " fag")
print(lisa.skrivFagPaaStudent())

